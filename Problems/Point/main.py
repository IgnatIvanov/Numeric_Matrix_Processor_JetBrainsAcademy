class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, p):
        return pow(pow(self.x - p.x, 2) + pow(self.y - p.y, 2), 0.5)