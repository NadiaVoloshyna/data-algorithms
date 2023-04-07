import hashlib
from math import sqrt

y_list = [20,93,72,35,54,95,25,37,29,72,65,66,49,43,35,61,97,66,64,22,83,69,19,21,69,40,35,81,15,41,74,12,3,65,
          31,12,48,68,41,40,99,13,70,30,20,35,84,96,1,93,61,83,24,27,93,86,96,43,10,51,27,87,40,35,83,44,15,89,
          71,79,25,84,43,49,66,0,88,80,4,3,74,10,41,45,75,34,41,44,50,99,41,37,26,6,94,94,76,48,32,42]

# string containing all y values
y_values = "209372355495253729726566494335619766642283691921694035811541741236531124868414099137030203584961936183242793" \
           "86964310512787403583441589717925844349660888043741041457534414450994137266949476483242"

# SHA256 hash of y values
sha256_received = "5c14e4599f1d2a39abe6b487ac2a5415c894c6882f5fdd4a40e02c7dd628829a"

def test_data():
    m = hashlib.sha256()
    m.update(y_values.encode('ascii'))
    sha256_generated = m.hexdigest()

    return sha256_received == sha256_generated

print(test_data())

class Point(object):
    """represents a coordinate"""
    def __init__(self, num1, num2):
        self.x = num1
        self.y = num2

    def distance(self, p2):
        dx = self.x - p2.x
        dy = self.y - p2.y
        return sqrt(dx * dx + dy * dy)

    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y)

def generate():
    """generate 100 Point objects"""
    l = []
    for item, el in zip(range(1, 101), y_list):
        p = Point(item, el)
        l.append(p)
    return l

def lookup(l):
    for el in l:
        print(el)

def neighbours():
    """find neighbours for each point in the coordinate system"""
    l = generate()
    neighbours_list = {}
    neighbours = []
    dist = 20

    for el in l:
        for j in l:
            d = el.distance(j)
            if d <= dist:
                neighbours.append(j)
        print(f"point: {el}")
        lookup(neighbours)
        neighbours_list[el] = neighbours
        neighbours = []
        #print(lookup(neighbours_list[el]))

    return neighbours_list

neighbours()

