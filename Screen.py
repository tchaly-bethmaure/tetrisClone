from Piece import Piece
import random

class Screen:
    def __init__(self):
        self.grid = []
        self.largeur = 12
        self.hauteur = 40
        self.pieces = []
        for ligne in range(0,self.hauteur):
            cases = []
            for case in range(0,self.largeur):
                cases.append('')
            self.grid.append(cases)

    def draw(self):
        x, y = 0, 0
        for ligne in self.grid:
            for case in ligne:
                self.grid[y][x] = ' '
                x += 1
            x = 0
            y += 1
        for piece in self.pieces:
            for square in piece.squares:
                self.grid[square.coordx][square.coordy] = square.ico

        dessin = ""
        for ligne in self.grid:
            for case in ligne:
                dessin += case
            dessin += "\n"

        print(dessin)
        print("------")

    def spawnPiece(self):
        p = Piece(random.randint(1,7))
        self.pieces.append(p)
        return p

    def spawnPieceWithId(self, id):
        p = Piece(id)
        self.pieces.append(p)
        return p

    def makePieceFall(self):
        for piece in self.pieces:
            if piece.currentControl == 1:
                piece.fall()
