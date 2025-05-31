import pygame
from circleshape import CircleShape
import random
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, delta_time):
        self.position += self.velocity * delta_time

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        angle = random.uniform(20, 50)

        velocity_a = self.velocity.rotate(angle) * 1.2
        velocity_b = self.velocity.rotate(-angle) * 1.2

        new_asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_a.velocity = velocity_a

        new_asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_b.velocity = velocity_b

        return [new_asteroid_a, new_asteroid_b]