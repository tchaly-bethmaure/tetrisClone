class Square:
    def __init__(self, coordx, coordy, spinOrigin, piece):
        self.coordx = coordx
        self.coordy = coordy
        self.spinOrigin = spinOrigin # 1 for yes, 0 for no
        self.piece = piece
        self.color = piece.color

    def delete(self):
        del self

    def fall(self):
        self.coordy += 1

    def draw(self, screen):
        pass

    def undraw(self, screen):
        pass
