import pygame

# base class for game objects
class CircleShape(pygame.sprite.Sprite):
    # defining the class (it takes the x- and y- coordinates, and the size of the radius)
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        # stats to keep track of itself (location, movement, and size)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    # the method that detects collision: it takes another CircleShape object as its argument
    def collide(self, circle):
        # using the "distance_to" method from pygame.Vector2, calculates the distance between both CircleShapes
        dist = self.position.distance_to(circle.position)
        # determine whether the distance is greater or lesser than the combination of both radiuses of the CircleShapes
        if dist <= (self.radius + circle.radius):
            # if the distance is less than the two sets of radiuses, it is colliding
            return True
        else:
            # if it's greater instead, they're not (didn't use "elif" because that seems redundant)
            return False