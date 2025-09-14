# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import everything from constants.py into the current file
from constants import *
# importing the other files into this one
from circleshape import *
from player import *

def main():
    # initialize the pygame import
    pygame.init()
    # creating a clock object
    game_clock = pygame.time.Clock()
    # set up the delta variable
    dt = 0
    # sets up the screen using the static variables from the constants import
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # setting up the player
    gamer = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
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
        # draw the player
        gamer.draw(screen)
        # display.flip refreshes the screen; should always be called last
        pygame.display.flip()
        # calling the .tick() method, setting fps to 60, and translating that time to seconds and capturing it in dt
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()