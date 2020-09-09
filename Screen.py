from Piece import Piece
import random
from datetime import datetime

class Screen:
    def __init__(self):
        self.grid = []
        self.largeur = 10
        self.hauteur = 20
        self.pieces = []
        self.current_piece = None
        self.nextPieceToCome = None

    def resetGame(self):
        self.__init__()

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
                self.grid[square.coordy][square.coordx] = 1

    def detectPieceCollision(self, piece):
            collision = False
            for pieceScreenModel in self.pieces:
                if pieceScreenModel.code != piece.code:
                    for square in piece.squares:
                        for squareScreenModele in pieceScreenModel.squares:
                            if square.coordy == squareScreenModele.coordy and square.coordx == squareScreenModele.coordx:
                                collision = True
            return collision

    def makePieceRotate(self, direction):
        pieceRotated = self.current_piece.rotationSimulation()
        self.current_piece.rotate(direction)

    def spawnPiece(self):
        p = None
        if self.nextPieceToCome == None:
            p = Piece(random.randint(1,7), datetime.timestamp(datetime.now()))
        else:
            p = self.nextPieceToCome
        self.nextPieceToCome = Piece(random.randint(1,7), datetime.timestamp(datetime.now()))
        p.move((4,0))
        self.pieces.append(p)
        self.current_piece = p

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
