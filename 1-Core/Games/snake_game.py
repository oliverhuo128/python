import pygame
import random

# Initialize the game
pygame.init()

# Set up the game window
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Set up colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up game variables
snake_size = 20
snake_speed = 15

# Initialize the snake position and direction
snake_x = window_width // 2
snake_y = window_height // 2
snake_dx = 0
snake_dy = 0

# Initialize the snake's body
snake_body = []
snake_length = 1

# Initialize the food position
food_x = random.randint(0, window_width - snake_size) // snake_size * snake_size
food_y = random.randint(0, window_height - snake_size) // snake_size * snake_size

# Set up clock to control the game's frame rate
clock = pygame.time.Clock()

# Function to display the snake and food on the window
def draw_snake_and_food():
    window.fill(BLACK)
    for segment in snake_body:
        pygame.draw.rect(window, GREEN, (segment[0], segment[1], snake_size, snake_size))
    pygame.draw.rect(window, RED, (food_x, food_y, snake_size, snake_size))
    pygame.display.update()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Change the direction of the snake based on arrow key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dy != snake_size:
                snake_dx = 0
                snake_dy = -snake_size
            elif event.key == pygame.K_DOWN and snake_dy != -snake_size:
                snake_dx = 0
                snake_dy = snake_size
            elif event.key == pygame.K_LEFT and snake_dx != snake_size:
                snake_dx = -snake_size
                snake_dy = 0
            elif event.key == pygame.K_RIGHT and snake_dx != -snake_size:
                snake_dx = snake_size
                snake_dy = 0

    # Update the snake's position
    snake_x += snake_dx
    snake_y += snake_dy

    # Check for collision with the food
    if snake_x == food_x and snake_y == food_y:
        food_x = random.randint(0, window_width - snake_size) // snake_size * snake_size
        food_y = random.randint(0, window_height - snake_size) // snake_size * snake_size
        snake_length += 1

    # Update the snake's body
    snake_body.append([snake_x, snake_y])
    if len(snake_body) > snake_length:
        del snake_body[0]

    # Check for self-collision
    if [snake_x, snake_y] in snake_body[:-1]:
        running = False

    # Check for collision with the window boundaries
    if snake_x < 0 or snake_x >= window_width or snake_y < 0 or snake_y >= window_height:
        running = False

    # Draw the snake and food on the window
    draw_snake_and_food()

    # Control the game's frame rate
    clock.tick(snake_speed)

# Quit the game
pygame.quit()