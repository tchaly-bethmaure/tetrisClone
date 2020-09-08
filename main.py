# import the pygame module, so you can use it
import pygame
from Screen import Screen
from Piece import Piece
from Square import Square
from Score import Score
from pygame.locals import *

def collisionWhileFalling(screen_model):
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
    return collision

def detectPieceCollisionWhileMoving(screen_model, moveDirection):
    cantMove = False
    # Wall collision
    for square in screen_model.current_piece.squares:
        if moveDirection == -1:
            if square.coordx -1 < 0:
                cantMove = True
        else:
            if square.coordx +1 > screen_model.largeur -1:
                cantMove = True
    # Piece collision
    for square in screen_model.current_piece.squares:
        for piece in screen_model.pieces:
            if piece != screen_model.current_piece:
                for squareOfScreenModele in piece.squares:
                        if moveDirection == -1 and square.coordx -1 == squareOfScreenModele.coordx and square.coordy == squareOfScreenModele.coordy:
                            cantMove = True
                        elif moveDirection == 1 and square.coordx +1 == squareOfScreenModele.coordx and square.coordy == squareOfScreenModele.coordy:
                            cantMove = True
    return cantMove

def detectRotationCollision(screen_model):
    collision = False
    currentPieceRotated = screen_model.current_piece.rotationSimulation()
    for square in currentPieceRotated.squares:
        if square.coordx < 0 or square.coordx > screen_model.largeur -1:
            collision = True
    return (collision or screen_model.detectPieceCollision(currentPieceRotated))

def uniqueList(list):
    uniqueList = []
    for x in list:
        if x not in uniqueList:
            uniqueList.append(x)
    return uniqueList

def playMidi(pygame, soundName):
    s = pygame.mixer.Sound(soundName)
    s.play()

def on_event(pygame, running, screen_model, score):
    rotationMoveAllowed = 5
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        pygame.event.pump()
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False
            pygame.midi.quit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                cantMove = detectPieceCollisionWhileMoving(screen_model, -1)
                if cantMove == False:
                    screen_model.current_piece.move((-1,0))
                    playMidi(pygame, "Move.wav")
                    score.incScore(1)
            elif event.key == pygame.K_RIGHT:
                cantMove = detectPieceCollisionWhileMoving(screen_model, 1)
                if cantMove == False:
                    screen_model.current_piece.move((1,0))
                    playMidi(pygame, "Move.wav")
                    score.incScore(1)
            elif event.key == pygame.K_UP:
                canRotate = not detectRotationCollision(screen_model)
                if rotationMoveAllowed > 0 and canRotate:
                    screen_model.makePieceRotate(1)
                    playMidi(pygame, "Rotate.wav")
                    score.incScore(1)
                rotationMoveAllowed -= 1
            elif event.key == pygame.K_DOWN:
                while(collisionWhileFalling(screen_model) == False):
                    screen_model.makePieceFall()
                    score.incScore(15)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                screen_model.resetGame()
                screen_model.spawnPiece()
                score.resetScore()
def on_loop(pygame, screen_model, score):
    # Point count of the loop initialized to 0
    points = 0

    collision = collisionWhileFalling(screen_model)
    if collision == False:
        screen_model.makePieceFall()
        # piece fall : 1point
        points += 1
    else:
        # Do we have scored lines
        screen_model.calcGrid()
        linesToDelete = []
        for square in screen_model.current_piece.squares:
            squaresToDelete = 0
            coordXLigneAVerif = square.coordx
            for newX in range(0, screen_model.largeur):
                if screen_model.grid[square.coordy][newX] != 0:
                    squaresToDelete += 1
            if squaresToDelete == screen_model.largeur:
                linesToDelete.append(square.coordy)
        if len(linesToDelete) > 0:
            linesToDelete = sorted(uniqueList(linesToDelete))
            # We count lines player did.
            linesToDeleteChained = []
            prevLineNumber = None
            chainDelete = []
            for lineNumber in linesToDelete:
                if len(linesToDelete) > 1:
                    # line is a part of a block of lines
                    if prevLineNumber != None and prevLineNumber + 1 == lineNumber:
                        chainDelete.append(lineNumber)
                    # line is not a part of a block of lines
                    elif prevLineNumber != None and prevLineNumber +1 != lineNumber:
                        linesToDeleteChained.append(sorted(chainDelete)) # we save the lines block
                        chainDelete = []
                        chainDelete.append(lineNumber) # new lines block, current line added
                        prevLineNumber = None
                    # first line of the block, we store it
                    elif prevLineNumber == None:
                        prevLineNumber = lineNumber
                        chainDelete.append(lineNumber)
                else:
                    linesToDeleteChained.append([lineNumber])
            # Deletion of lines.
            for chainOfLineNumber in linesToDeleteChained:
                firstLineNumber = None
                i = 0
                for lineNumber in chainOfLineNumber:
                    for squareCoordx in screen_model.getAllSquareOnLineNumber(lineNumber):
                        screen_model.deleteSquare(squareCoordx, lineNumber)
                        if i == 0:
                            firstLineNumber = lineNumber
                        i += 1
                # We make pieces fall.
                for piece in screen_model.pieces:
                    for square in piece.squares:
                        if square.coordy < firstLineNumber:
                            for x in range(0, len(chainOfLineNumber)):
                                square.fall()
            # 4 lines : 1000 points, 3 : 500 points, 2 lines : 250 points, 1 line : 125 points
            points += len(linesToDeleteChained)*125
            playMidi(pygame, "Line.wav")
        # Collision with the ground or other piece, we span a new piece.
        screen_model.spawnPiece()
        playMidi(pygame, "HitGround.wav")
    score.incScore(points)

def on_render(pygame, screen, screen_model, score):
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
    img = font.render('Score :'+str(score.getScore()), True, pygame.Color(0,0,0))
    screen.blit(img, ((screen_model.largeur+5)*19, (int(screen_model.hauteur/2)+square.coordy-10)*(19)))
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
    score = Score()

    i = 0
    # main loop
    while running:
        pygame.time.delay(350)
        on_event(pygame, running, screen_model, score)
        on_loop(pygame, screen_model, score)
        on_render(pygame, screen, screen_model, score)
        if i == 0:
                playMidi(pygame, "GameBegin1.wav")
                pygame.time.delay(1000)
                playMidi(pygame, "GameBegin2.wav")
                playMidi(pygame, "Theme.wav")
        i += 1
    pygame.midi.quit()

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
