# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import everything from constants.py into the current file
from constants import *
# importing the other files into this one
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    # ==INITIALIZING==
    # initialize the pygame import
    pygame.init()
    # creating a clock object
    game_clock = pygame.time.Clock()
    # set up the delta variable
    dt = 0

    # ==MAIN SETUPS==
    # sets up the screen using the static variables from the constants import
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # creating a group for all objects requiring updates
    updatable = pygame.sprite.Group()
    # creating a group for all objects that get drawn
    drawable = pygame.sprite.Group()
    # putting the Player class into the "update" and "draw" groups
    Player.containers = (updatable, drawable)
    # creating a group for every asteroid
    asteroidable = pygame.sprite.Group()
    # putting the Asteroid class into the "update," "draw," and "asteroid" groups
    Asteroid.containers = (asteroidable, updatable, drawable)
    # putting the Asteroid Field class into the "update" group
    AsteroidField.containers = (updatable)
    # creating a group for every shot
    shootable = pygame.sprite.Group()
    # putting the Shot class into the "shot" group
    Shot.containers = (shootable, updatable, drawable)

    # ==SPECIAL SETUPS==
    # setting up the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # setting up the asteroid field
    field = AsteroidField()

    # ==GAMEPLAY LOOP==
    # the game loop; True refers to "while the game is on"
    while True:
        # for each event that occurs per iteration
        for event in pygame.event.get():
            # check if the action of quitting the game has commensed
            if event.type == pygame.QUIT:
                # a blank return, assumed to end the game loop, and thus stop the program without having to use Ctrl-C
                return
        # this fills the screen with a black background (0 red, 0 blue, 0 green)
        screen.fill((0, 0, 0))
        # update everything
        updatable.update(dt)
        # checking for player collision
        for rock in asteroidable:
            # if statement that checks the collision
            if rock.collide(player):
                # when it becomes true, print "Game over!" to the console and immediately exit the program
                print("Game over!")
                return
        # checking for bullet collision
        for rock in asteroidable:
            # check to see which bullet, if any, collided
            for shot in shootable:
                # do they collide?
                if shot.collide(rock):
                    # if true, KILL
                    rock.kill()
                    shot.kill()
        # render everything using a loop
        for item in drawable:
            # render this item
            item.draw(screen)
        # display.flip refreshes the screen; should always be called last
        pygame.display.flip()
        # calling the .tick() method, setting fps to 60, and translating that time (from ms to s) and capturing it in dt
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()