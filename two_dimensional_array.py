import turtle

sc = turtle.Screen()
pen = turtle.Turtle()
firstColumn = [[-320, 320], [-320, 280], [-320, 240], [-320, 200], [-320, 160], [-320, 120], [-320, 80], [-320, 40], [-320, 0]]
"""
2D array: consider writing a second version of the twoDimensionalList() function, maybe with 3 parameters: startx, starty, fieldsize.  
For the 2D array (known: 8 by 8 layout), you could probably use 2 for loops, maybe in combination with 2 constant values: the number of rows and the number of columns.
"""
def two_dimensional_list(firstColumn, fieldsize):
    """generates a 2-dimensional list"""
    twoDimensionalList = []
    for item in firstColumn:
        x = item[0]
        y = item[1]
        arr = [item]
        while x < 0:
            el = []
            el.append(x + fieldsize)
            el.append(y)
            arr.append(el)
            x += fieldsize
        twoDimensionalList.append(arr)
    return twoDimensionalList

coordinates = two_dimensional_list(firstColumn, 40)

class Field():
    """represents a field of the chess board"""
    def __init__(self, point_a, point_b, point_c, point_d, color):
        self.a = point_a
        self.b = point_b
        self.c = point_c
        self.d = point_d
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

    def draw_chess_board(self):
        """draws the chess board by looping through the 2d list of coordinates and using Field class"""
        while len(self.coordinates) > 1:
            arr1 = self.coordinates[-1]
            arr2 = self.coordinates[-2]
            a1 = list(arr1)
            a2 = list(arr2)
            start = []
            while len(a1) > 1 and len(a2) > 1:
                point_a = a1[-1]
                if point_a[0] == 0:
                    start.append(point_a)
                point_b = a1[-2]
                point_c = a2[-2]
                point_d = a2[-1]
                f = Field(point_a ,point_b, point_c, point_d, self.black)
                f.draw()
                del a1[-1]
                del a2[-1]
                self.black, self.red = self.red, self.black
            pen.goto(start[0])
            self.black, self.red = self.red, self.black
            del self.coordinates[-1]

c = ChessBoard(coordinates)
c.draw_chess_board()
