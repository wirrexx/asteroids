import pygame
from constants import *


height = SCREEN_HEIGHT
width = SCREEN_WIDTH

screen = pygame.display.set_mode((width, height))
running = True

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")


    pygame.display.flip()





if __name__ == "__main__":
    main()