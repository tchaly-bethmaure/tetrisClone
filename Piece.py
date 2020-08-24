# Piece existante :
# ID; Nom Piece
# 1;Barre
# 2;s
# 3;s inverse
# 4;L
# 5;L inverse
# 6;carre
# 7;T
from Square import Square
import math

class Piece:
    def __init__(self, id):
        self.id = id
        self.coordx = 0
        self.coordy = 0
        self.currentControl = 1
        self.squares = [] # list Square with coord associated for making the piece
        if id == 1: # line
            self.squares.append(Square(0,0,1))
            self.squares.append(Square(0,1,0))
            self.squares.append(Square(0,2,0))
            self.squares.append(Square(0,3,0))
        elif id == 2: # S
            self.squares.append(Square(0,1,0))
            self.squares.append(Square(1,1,0))
            self.squares.append(Square(1,0,1))
            self.squares.append(Square(2,0,0))
        elif id == 3: # S inverse
            self.squares.append(Square(0,0,0))
            self.squares.append(Square(1,0,1))
            self.squares.append(Square(1,1,0))
            self.squares.append(Square(2,1,0))
        elif id == 5: # L inverse
            self.squares.append(Square(1,0,0))
            self.squares.append(Square(1,1,0))
            self.squares.append(Square(1,2,0))
            self.squares.append(Square(0,2,1))
        elif id == 4: # L
            self.squares.append(Square(0,0,0))
            self.squares.append(Square(0,1,0))
            self.squares.append(Square(0,2,0))
            self.squares.append(Square(1,2,1))
        elif id == 6: # square
            self.squares.append(Square(0,0,1))
            self.squares.append(Square(0,1,0))
            self.squares.append(Square(1,0,0))
            self.squares.append(Square(1,1,0))
        elif id == 7: # T
            self.squares.append(Square(1,0,0))
            self.squares.append(Square(0,1,0))
            self.squares.append(Square(1,1,1))
            self.squares.append(Square(2,1,0))
    def fall(self):
        for square in self.squares:
            square.fall()
    def rotate(self, origin, point, angle):
        """
        Rotate a point counterclockwise by a given angle around a given origin.

        The angle should be given in radians.
        """
        ox, oy = origin
        px, py = point

        qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
        qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
        return qx, qy

    def spin(self, direction):
        sOrigin = None
        origin = (0, 0)
        if direction == 1: # right
            for square in self.squares:
                if square.spinOrigin == 1:
                    sOrigin = square
                    origin = (sOrigin.coordx, sOrigin.coordy)
                    print("Origine : "+str(origin))
            for square in self.squares:
                if square != sOrigin:
                    point = (square.coordx, square.coordy)
                    print("Point a transformer : "+str(point))
                    newPoint = self.rotate(origin, point, math.radians(90))
                    square.coordx = int(newPoint[0])
                    square.coordy = int(newPoint[1])
                    print("Point transforme : "+str((square.coordx, square.coordy)))
        else: # left
            for square in self.squares:
                square.coordx = 0
                square.coordy = 0
    def move(self, vector):
        for square in self.squares:
            square.coordx += vector.x
            square.coordy += vector.y

    def deleteSquare(self, coordx, coordy):
        i = 0
        for s in self.squares:
            if s.coordx == coordx and s.coordy == coordy:
                del self.squares[i] # del s ?
            i+=1
