from math import sqrt
import matplotlib.pyplot as plt

class Point(object):
    """This class represents a coordinate."""
    def __init__(self, num1, num2):
        self.x = num1
        self.y = num2

    def distance(self, p2):
        dx = self.x - p2.x
        dy = self.y - p2.y
        return sqrt(dx * dx + dy * dy)

    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y)

def point_test():
    p1 = Point(1, 1)
    p2 = Point(3, 3)
    print(f" p1: {p1}")
    print(f" p2: {p2}")
    print( f"distance p1 <-> p2 { p1.distance(p2) }")

point_test()

y_list = [20,93,72,35,54,95,25,37,29,72,65,66,49,43,35,61,97,66,64,22,83,69,19,21,69,40,35,81,15,41,74,12,3,65,
          31,12,48,68,41,40,99,13,70,30,20,35,84,96,1,93,61,83,24,27,93,86,96,43,10,51,27,87,40,35,83,44,15,89,
          71,79,25,84,43,49,66,0,88,80,4,3,74,10,41,45,75,34,41,44,50,99,41,37,26,6,94,94,76,48,32,42]

def generate():
    """generates 100 Point objects"""
    l = []
    for item, el in zip(range(1, 101), y_list):
        p = Point(item, el)
        l.append(p)
    return l

def neighbours(origin, distance):
    """finds neighbours of a particular point (object) in the coordinate system"""
    l = generate()
    neighbours = []
    for el in l:
        dist = origin.distance(el)
        if dist <= distance:
            neighbours.append(el)
            print(f"p1: {origin} \np2: {el} \ndistance = {dist}")

    return neighbours

neighbours(Point(1,20), 20)

def plot_xy():
    x = [x + 1 for x in range(100)]
    y = y_list
    plt.scatter( x, y )
    plt.grid(True)
    plt.show()

# plot_xy()