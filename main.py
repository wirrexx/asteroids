import pygame
from constants import *


height = SCREEN_HEIGHT
width = SCREEN_WIDTH

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
delta_time = 0
running = True

def main():
    global running, delta_time
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")


        pygame.display.flip()
        delta_time = clock.tick(60) / 1000




if __name__ == "__main__":
    main()