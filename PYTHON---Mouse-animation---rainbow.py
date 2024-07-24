import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()

# Hide the default cursor
pygame.mouse.set_visible(False)

# Rainbow colors
colors = [
    (255, 0, 0),    # Red
    (255, 127, 0),  # Orange
    (255, 255, 0),  # Yellow
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (75, 0, 130),   # Indigo
    (143, 0, 255)   # Violet
]

# Main loop
clock = pygame.time.Clock()
angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Get mouse position
    x, y = pygame.mouse.get_pos()

    # Draw rainbow circles
    for i in range(7):
        radius = 20 - i * 2
        color_index = (i + int(angle)) % 7
        pygame.draw.circle(screen, colors[color_index], (x, y), radius)

    # Update the display
    pygame.display.flip()

    # Increase the angle for color rotation
    angle += 0.1

    # Cap the frame rate
    clock.tick(60)
