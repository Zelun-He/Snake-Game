import pygame
from pygame.math import Vector2
import sys

# Initialize pygame
pygame.init()

title_font = pygame.font.Font(None,60)
score_font = pygame.font.Font(None, 40)

# Define colors
GREEN = (273, 204, 96)
DARK_GREEN = (43, 51, 24)

# Screen setup
cell_size = 30
number_of_cells = 25

# Food class
class Food:
    def __init__(self):
        self.position = Vector2(5,6)
        
    def draw(self):
        food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)
        screen.blit(food_surface, food_rect)
        
        
screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells))
pygame.display.set_caption("Retro Snake")

# Clock setup
clock = pygame.time.Clock()

food = Food()
food_surface = pygame.image.load("Graphics/food.png")

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #Drawing
    screen.fill(GREEN)
    food.draw()
    pygame.display.update()
    clock.tick(60)
