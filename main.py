import sys
import pygame
from constants import *

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()

    height = SCREEN_HEIGHT
    width = SCREEN_WIDTH

    screen = pygame.display.set_mode((width, height))

    clock = pygame.time.Clock()
    running = True

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)

    player = Player(width/2, height/2)

    delta_time = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatable.update(delta_time)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    new_asteroids = asteroid.split()
                    asteroids.add(*new_asteroids)



        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        delta_time = clock.tick(60) / 1000


    pygame.quit()


if __name__ == "__main__":
    main()