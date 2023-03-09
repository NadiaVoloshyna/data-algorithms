from random import randint
from math import sqrt

class Point(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.X = 0
        self.Y = 0
        self.dist = 0

    def set(self):
        self.x = randint(1, 10)
        self.y = randint(1, 10)

    def distance(self, p2):
        p2.set()
        self.X = p2.x
        self.Y = p2.y
        self.dist = round(sqrt((self.x - self.X) ** 2 + (self.y - self.Y) ** 2), 2)

    def __str__(self):
        return "x: " + str(self.x) + "\ny: " + str(self.y) + "\nX: " + str(self.X) + "\nY: " + str(self.Y) + "\ndistance: " + str(self.dist)


p = Point()
p.set()
p2 = Point()
p.distance(p2)
print(p.__str__())
