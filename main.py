# import the pygame module, so you can use it
import pygame
from Screen import Screen
from Piece import Piece
from Square import Square
from pygame.locals import *

def on_event(pygame, running, screen_model, current_piece):
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        pygame.event.pump()
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False
        elif event.type == pygame.KEYUP:
            current_piece.rotate()
def on_loop(pygame, screen_model, current_piece):
    current_piece.fall()

def on_render(pygame, screen, screen_model):
    screen.fill(pygame.Color(255,255,255))
    for piece in screen_model.pieces:
        for square in piece.squares:
            pygame.draw.rect(screen, pygame.Color(0,0,0), (square.coordy*(19),square.coordx*(19),20,20))
    pygame.display.update()

# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    pygame.display.set_caption("Tetris Clone")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((640,480))
    screen_model = Screen()
    current_piece = screen_model.spawnPieceWithId(7)

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        pygame.time.delay(1000)
        on_event(pygame, running, screen_model, current_piece)
        on_loop(pygame, screen_model, current_piece)
        on_render(pygame, screen, screen_model)

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
