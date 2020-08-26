# import the pygame module, so you can use it
import pygame
from Screen import Screen
from Piece import Piece
from Square import Square
from pygame.locals import *

def on_event(pygame, running, screen_model):
    rotationMoveAllowed = 5
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        pygame.event.pump()
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                cantMove = False
                for square in screen_model.current_piece.squares:
                    if square.coordx -1 < 0:
                        cantMove = True
                if cantMove == False:
                    screen_model.current_piece.move((-1,0))
            elif event.key == pygame.K_RIGHT:
                cantMove = False
                for square in screen_model.current_piece.squares:
                    if square.coordx +1 > screen_model.largeur:
                        cantMove = True
                if cantMove == False:
                    screen_model.current_piece.move((1,0))
            elif event.key == pygame.K_UP:
                if rotationMoveAllowed > 0:
                    screen_model.makePieceRotate(1)
                rotationMoveAllowed -= 1
            elif event.key == pygame.K_DOWN:
                if rotationMoveAllowed > 0:
                    screen_model.makePieceRotate(0)
                rotationMoveAllowed -= 1
def on_loop(pygame, screen_model):
    collision = False
    # is current controlled piece touch other pieces ?
    for piece in screen_model.pieces:
        if piece != screen_model.current_piece:
            for square in piece.squares:
                for current_square in screen_model.current_piece.squares:
                    if current_square.coordy +1 == square.coordy and current_square.coordx == square.coordx:
                        collision = True # yes
    # Current controlled piece touch the ground
    for square in screen_model.current_piece.squares:
        if square.coordy +1 >= screen_model.hauteur:
            collision = True

    if collision == False:
        screen_model.makePieceFall()
    else:
        screen_model.spawnPiece()

    # Do we have scored lines
    screen_model.calcGrid()
    lines = []
    for y in range(0, screen_model.hauteur):
        tempLine = []
        for x in range(0, screen_model.largeur):
            if screen_model.grid[y][x] != 0:
                tempLine.append(screen_model.grid[y][x])
            if len(tempLine) == screen_model.largeur:
                # we got a line
                lines.append(tempLine)
    # delete line plus fall each pieces down
    if lines:
        tresholdY = None
        for line in lines:
            for square in line:
                tresholdY = square.coordy
                screen_model.pieces[screen_model.pieces.index(square.piece)].squares.remove(square)
                del square
        for piece in screen_model.pieces:
            for s in piece.squares:
                if s.coordy < tresholdY:
                    s.fall()

def on_render(pygame, screen, screen_model):
    screen.fill(pygame.Color(255,255,255))
    pygame.draw.line(screen, pygame.Color(0,0,0), (0,0), (0,screen_model.hauteur*19),10)
    pygame.draw.line(screen, pygame.Color(0,0,0), (0,screen_model.hauteur*19), (screen_model.largeur*19,screen_model.hauteur*19),10)
    pygame.draw.line(screen, pygame.Color(0,0,0), (screen_model.largeur*19,0), (screen_model.largeur*19,screen_model.hauteur*19),10)

    for piece in screen_model.pieces:
        for square in piece.squares:
            pygame.draw.rect(screen, piece.color, (square.coordx*(19),square.coordy*(19),20,20))
    for square in screen_model.nextPieceToCome.squares:
        pygame.draw.rect(screen, screen_model.nextPieceToCome.color, ((screen_model.largeur+5+square.coordx)*(19),(int(screen_model.hauteur/2)+square.coordy)*(19),20,20))
    font = pygame.font.SysFont(None, 24)
    img = font.render('Next piece :', True, pygame.Color(0,0,0))
    screen.blit(img, ((screen_model.largeur+5)*19, (int(screen_model.hauteur/2)+square.coordy-5)*(19)))
    pygame.display.update()

# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    pygame.display.set_caption("Tetris Clone")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((640,480))
    screen_model = Screen()
    screen_model.spawnPiece()

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        pygame.time.delay(350)
        on_event(pygame, running, screen_model)
        on_loop(pygame, screen_model)
        on_render(pygame, screen, screen_model)

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
