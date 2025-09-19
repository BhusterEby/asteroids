import pygame
import random
from circleshape import *
from constants import *

# defining a new Asteroid class, inheriting from CircleShape
class Asteroid(CircleShape):
    # setting up the constructor
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # drawing the asteroid
    def draw(self, screen):
        # takes screen object, color (white), the position and radius, and a line width of 2
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    # updating the asteroid's position
    def update(self, dt):
        # applying the delta time to the velocity, and adding that to the position
        self.position += (self.velocity * dt)
    
    # splitting the asteroids
    def split(self):
        # immediately destroy the main asteroid
        self.kill()
        # check the asteroids size
        if self.radius <= ASTEROID_MIN_RADIUS:
            # if it's smaller, return
            return
        else:
            # if it's bigger, split into two smaller asteroids
            # first off: generating a new rotation
            random_angle = random.uniform(20, 50)
            # create two new vectors
            velocity_1 = self.velocity.rotate(random_angle)
            velocity_2 = self.velocity.rotate(-random_angle)
            # generate new radius
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            # create the two asteroids
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            # apply the new vectors
            asteroid_1.velocity = velocity_1 * 1.2
            asteroid_2.velocity = velocity_2 * 1.2