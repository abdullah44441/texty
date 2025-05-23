import pygame
import os
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Texty")

# Colors
Black = (0, 0, 0)
White = (255, 255, 255)

# Functions
Font = pygame.font.SysFont("Arial", 30)
def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# Variables
text = [""]

# Main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("result.txt", "w") as f:
                f.write("\n".join(text))
            run = False
        if event.type == pygame.TEXTINPUT:
            text[-1] += event.text
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text[-1] = text[-1][:-1]
            elif event.key == pygame.K_RETURN:
                text.append('')

    # Clear screen
    screen.fill(White)  # White background
    for row, line in enumerate(text):
        draw_text(line, Font, Black, 10, 10 + row * 30)  # Adjusted to display lines properly

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
