import pygame
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
    
    def update(self, dt):
        self.position += (self.velocity * dt)