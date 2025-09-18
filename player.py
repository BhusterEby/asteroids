import pygame
from circleshape import *
from constants import *
from shot import *

# defining a new Player class, inheriting from CircleShape
class Player(CircleShape):
    # setting up the constructor
    def __init__(self, x, y):
        # calling upon the parent's constructor, and passing in variables
        super().__init__(x, y, PLAYER_RADIUS)
        # setting a rotation variable
        self.rotation = 0
        # setting up a timer variable, to act as a cooldown for shooting
        self.cooldown = 0
    
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
    
    # a rotate method
    def rotate(self, dt):
        # adds the turn speed to the current rotation
        self.rotation += PLAYER_TURN_SPEED * dt
    
    # a moving method
    def move(self, dt):
        # again, boot.dev helped me not do math, but I can explain this one
        # ==tl;dr==
        # we draw a vector straight up
        # rotate it to match the player's orientation
        # multiply speed and dt (bigger vectors create faster movements)
        # add the new vector to our player
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    # an update method, which gives controls to the player
    def update(self, dt):
        # maps the key that gets pressed to a variable
        keys = pygame.key.get_pressed()

        # ROTATE: checks to see if "a" or "d" gets pressed
        if keys[pygame.K_a]:
            # rotate counter-clockwise
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # rotate clockwise
            self.rotate(dt)
        
        # MOVING: checks to see if "w" or "s" gets pressed
        if keys[pygame.K_w]:
            # move forward
            self.move(dt)
        if keys[pygame.K_s]:
            # move backward
            self.move(-dt)
        
        # SHOOTING: checks to see if "space" gets pressed
        if keys[pygame.K_SPACE]:
            # check if the cooldown timer is still active
            if self.cooldown > 0:
                # don't shoot
                pass
            else:
                # if the timer isn't active, shoot bullet
                self.shoot()
                # set the cooldown
                self.cooldown = PLAYER_SHOOT_COOLDOWN
        
        # decrease the cooldown timer
        self.cooldown -= dt
    
    # a method to shoot bullets with
    def shoot(self):
        # creating a new shot object at player position
        bullet = Shot(self.position.x, self.position.y)
        # get the player's rotation and applying it to a vector
        blast = pygame.Vector2(0, 1).rotate(self.rotation)
        # scaling up the velocity of the vector
        bullet.velocity += blast * PLAYER_SHOOT_SPEED
