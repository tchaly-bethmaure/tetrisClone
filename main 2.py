from Screen import Screen
from Piece import Piece
from Square import Square
from os import system, name
from time import sleep
import keyboard

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
s = Screen()
s.draw()

#p = s.spawnPiece()
p = s.spawnPieceWithId(2)
s.draw()
i=0
while(1):
    sleep(1)
    clear()
    for square in p.squares:
        if square.coordx > s.largeur or square.coordy > s.hauteur:
            p.currentControl = 0
            p = s.spawnPiece()

    if keyboard.is_pressed('a'):
        p.rotate()
    p.fall()
    s.draw()
    if len(s.pieces) > 4:
        break
