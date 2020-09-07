from Piece import Piece
import random

class Screen:
    def __init__(self):
        self.grid = []
        self.largeur = 10
        self.hauteur = 20
        self.pieces = []
        self.current_piece = None
        self.nextPieceToCome = None

    def reinitGrid(self):
        self.grid = []
        for ligne in range(0, self.hauteur):
            cases = []
            for case in range(0, self.largeur):
                cases.append(0)
            self.grid.append(cases)

    def calcGrid(self):
        self.reinitGrid()
        for piece in self.pieces:
            for square in piece.squares:
                self.grid[square.coordy][square.coordx] = square

    def makePieceRotate(self, direction):
        #dummyPiece = self.current_piece.rotateSimulation(direction)
        #rotationAllowed = True
        #for dummySquareTuple in dummyPiece:
        #    for piece in self.pieces:
        #        if self.current_piece != piece and :
        #            for square in piece.squares:
        #                if dummySquareTuple[0] == square.coordx or dummySquareTuple[1] == square.coordy:
        #                    #can't rotate
        #                    rotationAllowed = False
        #                    print("Not Allowed : "+str(dummySquareTuple)+" crossing "+str((square.coordx,square.coordy)))
        #if rotationAllowed == True:
        self.current_piece.rotate(direction)

    def spawnPiece(self):
        p = None
        if self.nextPieceToCome == None:
            p = Piece(random.randint(1,7))
        else:
            p = self.nextPieceToCome
        self.nextPieceToCome = Piece(random.randint(1,7))
        p.move((4,4))
        self.pieces.append(p)
        self.current_piece = p

    #for debug : def spawnPieceWithId(self, id):
    #    p = Piece(id)
    #    p.move((4,4))
    #    self.pieces.append(p)
    #    return p

    def makePieceFall(self):
        self.current_piece.fall()

    def getAllSquareOnLineNumber(self, lineNumber):
        squaresCoordXOnLine = []
        for piece in self.pieces:
            for square in piece.squares:
                if square.coordy == lineNumber:
                    squaresCoordXOnLine.append(square.coordx)
        return squaresCoordXOnLine

    def deleteSquare(self, squareToDeleteCoordx, squareToDeleteCoordy):
        for piece in self.pieces:
            for square in piece.squares:
                if square.coordx == squareToDeleteCoordx and square.coordy == squareToDeleteCoordy:
                    del piece.squares[piece.squares.index(square)]
