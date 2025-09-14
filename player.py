import pygame
from circleshape import *
from constants import *

# defining a new Player class, inheriting from CircleShape
class Player(CircleShape):
    # setting up the constructor
    def __init__(self, x, y):
        # calling upon the parent's constructor, and passing in variables
        super().__init__(x, y, PLAYER_RADIUS)
        # setting a rotation variable
        self.rotation = 0
    
    # method for drawing the triangle over the hitbox
    def triangle(self):
        # don't ask me, boot.dev wrote this so that I don't have to math out how to draw a triangle
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # drawing the player
    def draw(self, screen):
        # takes the screen object, color (white), the three points from the Triangle method, and a line width of 2
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)