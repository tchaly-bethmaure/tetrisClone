class Square:
    def __init__(self, coordx, coordy, spinOrigin):
        self.coordx = coordx
        self.coordy = coordy
        self.ico = '#'
        self.spinOrigin = spinOrigin # 1 for yes, 0 for no

    def fall(self):
        self.coordx += 1

    def draw(self, screen):
        pass

    def undraw(self, screen):
        pass
