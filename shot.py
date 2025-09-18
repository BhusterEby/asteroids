import pygame
from circleshape import *
from constants import *

# defining a new Shot class, inheriting from CircleShape
class Shot(CircleShape):
    # setting up the constructor
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    # drawing the bullet
    def draw(self, screen):
        # takes screen object, color (white), the position and radius, and a line width of 2
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    # updating the bullet's position
    def update(self, dt):
        # applying the delta time to the velocity, and adding that to the position
        self.position += (self.velocity * dt)