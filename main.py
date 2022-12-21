import pygame
import random

# Initialize pygame
pygame.init()

# Set the window size
window_size = (600, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title
pygame.display.set_caption('Snake')

# Set the frame rate
clock = pygame.time.Clock()

# Set the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Set the font
font = pygame.font.Font(None, 36)

# Set the snake starting position and velocity
snake_pos = [300, 300]
snake_vel = [4, 0]

# Set the starting length of the snake
snake_length = [snake_pos]

# Set the food position
food_pos = [random.randrange(1, (window_size[0]//10)) * 10, random.randrange(1, (window_size[1]//10)) * 10]
food_spawn = True
# Set the score
score = 0

# Set the game over flag
game_over = False

# Set the key press delay
key_delay = False

# Set the direction
direction = 'right'

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # Check for key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'down' and not key_delay:
                snake_vel = [0, -4]
                direction = 'up'
                key_delay = True
            if event.key == pygame.K_DOWN and direction != 'up' and not key_delay:
                snake_vel = [0, 4]
                direction = 'down'
                key_delay = True
            if event.key == pygame.K_LEFT and direction != 'right' and not key_delay:
                snake_vel = [-4, 0]
                direction = 'left'
                key_delay = True
            if event.key == pygame.K_RIGHT and direction != 'left' and not key_delay:
                snake_vel = [4, 0]
                direction = 'right'
                key_delay = True

    # Update the snake position
    snake_pos[0] += snake_vel[0]
    snake_pos[1] += snake_vel[1]

    # Check if the snake has collided with the wall
    if snake_pos[0] == -1 or snake_pos[0] == window_size[0] or snake_pos[1] == -1 or snake_pos[1] == window_size[1]:
        game_over = True

    # Check if the snake has eaten the food
    food_distance = ((snake_pos[0]-food_pos[0])**2+(snake_pos[1]-food_pos[1])**2)**(1/2)
    if food_distance <= 5:
        score += 1
        snake_length.append(list(snake_pos))
        food_spawn = False
    else:
        snake_length.pop()

   
    # Spawn new food
    if not food_spawn:
        food_pos = [random.randrange(1, (window_size[0]//10)) * 10, random.randrange(1, (window_size[1]//10)) * 10]
    food_spawn = True

    # Check if the snake has collided with itself
    for pos in snake_length[:-1]:
        if pos == snake_pos:
            game_over = True

    # Update the snake length
    snake_length.insert(0, list(snake_pos))

    # Clear the screen
    screen.fill(black)

    # Draw the snake
    for pos in snake_length:
        pygame.draw.rect(screen, white, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw the food
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Draw the score
    text = font.render('Score: ' + str(score), True, white)
    screen.blit(text, (5, 10))

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(10)

    # Reset the key delay
    key_delay = False

# Display the game over screen
text = font.render('Game Over', True, white)
text_rect = text.get_rect()
text_x = screen.get_width() // 2 - text_rect.width // 2
text_y = screen.get_height() // 2 - text_rect.height // 2
screen.blit(text, [text_x, text_y])
pygame.display.update()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
