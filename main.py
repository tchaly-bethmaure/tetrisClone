from Screen import Screen
from Piece import Piece
from Square import Square

s = Screen()
s.draw()

#p = s.spawnPiece()
p = s.spawnPieceWithId(2)
s.draw()
i=0
while(i<3):
    #p.fall()
    p.spin(1)
    s.draw()
    i+=1
