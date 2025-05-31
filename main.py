import pygame
from constants import *

from player import Player


height = SCREEN_HEIGHT
width = SCREEN_WIDTH

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
delta_time = 0
running = True

def main():
    global running, delta_time
    player = Player(width/2, height/2)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        delta_time = clock.tick(60) / 1000

        player.draw(screen)




        pygame.display.flip()




if __name__ == "__main__":
    main()