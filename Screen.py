from Piece import Piece
import random

class Screen:
    def __init__(self):
        self.grid = []
        self.largeur = 10
        self.hauteur = 20
        self.pieces = []
        self.current_piece = None

    def reinitGrid(self):
        self.grid = []
        for ligne in range(0,self.hauteur):
            cases = []
            for case in range(0,self.largeur):
                cases.append(' ')
            self.grid.append(cases)

    def draw(self):
        self.reinitGrid()
        for piece in self.pieces:
            for square in piece.squares:
                self.grid[square.coordx][square.coordy] = square.ico

        dessin = ""
        for ligne in self.grid:
            for case in ligne:
                dessin += case
            dessin += "\n"
        for x in range(0, self.largeur):
            dessin += "§"
        print(dessin)

    def spawnPiece(self):
        p = Piece(random.randint(1,7))
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
