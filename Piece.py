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
import copy

class Piece:
    def __init__(self, id, code):
        self.vecRotation = {
            1:[
                (0,0),
                (1,-1),
                (2,-2),
                (3,-3)
            ],
            2:[
                (2,0),
                (1,-1),
                (0,0),
                (-1,-1)
            ],
            3:[
                (1,1),
                (0,0),
                (1,-1),
                (0,-2)
            ],
            4:[
                (-1,3),
                (0,2),
                (1,1),
                (0,0)
            ],
            5:[
                (-3,1),
                (-2,0),
                (-1,-1),
                (0,0)
            ],
            6:[
                (-1,1),
                (-2,0),
                (-1,-1),
                (0,0)
            ],
            7:[
                (-1,1),
                (1,1),
                (0,0),
                (-1,-1)
            ]
        }
        self.id = id
        self.code = code
        self.coordx = 0
        self.coordy = 0
        self.squares = [] # list Square with coord associated for making the piece
        self.color = None
        self.nextRotationVecForPiece = self.vecRotation[self.id]
        if id == 1: # line
            self.color = (66, 221, 245)
            self.squares.append(Square(0,0,1,self))
            self.squares.append(Square(0,1,0,self))
            self.squares.append(Square(0,2,0,self))
            self.squares.append(Square(0,3,0,self))

        elif id == 2: # S
            self.color = (72, 245, 66)
            self.squares.append(Square(0,1,0,self))
            self.squares.append(Square(1,1,0,self))
            self.squares.append(Square(1,0,1,self))
            self.squares.append(Square(2,0,0,self))
        elif id == 3: # S inverse
            self.color = (245, 66, 66)
            self.squares.append(Square(0,0,0,self))
            self.squares.append(Square(1,0,1,self))
            self.squares.append(Square(1,1,0,self))
            self.squares.append(Square(2,1,0,self))
        elif id == 5: # L inverse
            self.color = (245, 147, 66)
            self.squares.append(Square(1,0,0,self))
            self.squares.append(Square(1,1,0,self))
            self.squares.append(Square(1,2,0,self))
            self.squares.append(Square(0,2,1,self))
        elif id == 4: # L
            self.color = (66, 90, 245)
            self.squares.append(Square(0,0,0,self))
            self.squares.append(Square(0,1,0,self))
            self.squares.append(Square(0,2,0,self))
            self.squares.append(Square(1,2,1,self))
        elif id == 6: # square
            self.color = (245, 245, 66)
            self.squares.append(Square(0,0,1,self))
            self.squares.append(Square(0,1,0,self))
            self.squares.append(Square(1,0,0,self))
            self.squares.append(Square(1,1,0,self))
        elif id == 7: # T
            self.color = (197, 66, 245)
            self.squares.append(Square(1,0,0,self))
            self.squares.append(Square(0,1,0,self))
            self.squares.append(Square(1,1,1,self))
            self.squares.append(Square(2,1,0,self))    
    def fall(self):
        for square in self.squares:
            square.fall()

    def rotate(self, direction):
        if self.id not in [6]:
            i = 0
            for square in self.squares:
                square.coordx += self.vecRotation[self.id][i][0]
                square.coordy += self.vecRotation[self.id][i][1]
                i += 1
            #We update the rotation vector for next rotation
            i=0
            for coord in self.nextRotationVecForPiece:
                coordx = coord[0]
                coordy = coord[1]
                self.nextRotationVecForPiece[i] = (coordy, -1*coordx)
                i += 1

    def rotationSimulation(self):
        dummyPieceToRotate = copy.deepcopy(self)
        if self.id not in [6]:
            i = 0
            for square in dummyPieceToRotate.squares:
                square.coordx += self.vecRotation[self.id][i][0]
                square.coordy += self.vecRotation[self.id][i][1]
                i += 1
        return dummyPieceToRotate

    def move(self, vector):
        for square in self.squares:
            square.coordx += vector[0]
            square.coordy += vector[1]

    def deleteSquare(self, coordx, coordy):
        i = 0
        for s in self.squares:
            if s.coordx == coordx and s.coordy == coordy:
                del self.squares[i] # del s ?
            i+=1
