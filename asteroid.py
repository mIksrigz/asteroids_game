import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_angle = random.uniform(20, 50)
        positive_velocity = self.velocity.rotate(new_angle)
        negative_velocity = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        second_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        first_asteroid.velocity = 1.2 * positive_velocity
        second_asteroid.velocity = 1.2 * negative_velocity