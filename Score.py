class Score:
    def __init__(self):
        self.score = [0]

    def incScore(self, scoreToAdd):
        self.score[0] += scoreToAdd

    def getScore(self):
        return self.score[0]
