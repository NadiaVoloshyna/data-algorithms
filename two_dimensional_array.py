import turtle

sc = turtle.Screen()
pen = turtle.Turtle()
firstColumn = [[-320, 320], [-320, 280], [-320, 240], [-320, 200], [-320, 160], [-320, 120], [-320, 80], [-320, 40], [-320, 0]]

def twoDimensionalList(firstColumn):
    """generates a 2-dimensional list"""
    twoDimensionalList = []
    for item in firstColumn:
        x = item[0]
        y = item[1]
        arr = [item]
        while x < 0:
            el = []
            el.append(x + 40)
            el.append(y)
            arr.append(el)
            x += 40
        twoDimensionalList.append(arr)
    return twoDimensionalList

coordinates = twoDimensionalList(firstColumn)

class Field():
    """
    represents a field of the chess board
    a, b, c, d - are the coordinates of the four quadrangle points
    """
    def __init__(self, a, b, c, d, color):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.color = color

    def draw(self):
        pen.hideturtle()
        pen.speed(7)
        pen.color(self.color)
        pen.begin_fill()
        pen.goto(self.a[0], self.a[1])
        pen.goto(self.b[0], self.b[1])
        pen.goto(self.c[0], self.c[1])
        pen.goto(self.d[0], self.d[1])
        pen.goto(self.a[0], self.a[1])
        pen.end_fill()

class ChessBoard():
    """represents the chess board"""
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.black = "black"
        self.red = "red"

    def drawChessBoard(self):
        """draws the chess board by looping through the 2d list of coordinates and using Field class"""
        while len(self.coordinates) > 1:
            arr1 = self.coordinates[-1]
            arr2 = self.coordinates[-2]
            a1 = list(arr1)
            a2 = list(arr2)
            start = []
            while len(a1) > 1 and len(a2) > 1:
                a = a1[-1]
                if a[0] == 0:
                    start.append(a)
                b = a1[-2]
                c = a2[-2]
                d = a2[-1]
                f = Field(a ,b, c, d, self.black)
                f.draw()
                del a1[-1]
                del a2[-1]
                self.black, self.red = self.red, self.black
            pen.goto(start[0])
            self.black, self.red = self.red, self.black
            del self.coordinates[-1]

c = ChessBoard(coordinates)
c.drawChessBoard()
