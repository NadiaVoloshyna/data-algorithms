class Stack():
    def __init__(self):
        self.l = []
        self.top = -1

    def __str__(self):
        return str(self.l)

    def push(self, val):
        self.top = self.top + 1
        self.l.append(val)

    def pop(self):
        if self.top == -1:
            print("Stack underflow")
        else:
            top = self.l[self.top]
            self.l.pop()
            self.top = self.top - 1
            return top

    def is_empty(self):
        return self.top == -1

def get_triangle():
    s = Stack()
    spaces = 11
    ast = 1

    for i in range(12):
        str = ' '*spaces + '*'*ast + ' '*spaces
        print(str)
        s.push(str)
        spaces = spaces - 1
        ast = ast + 2

    print("-----------------------")
    while s.is_empty() == False:
        print(s.pop())

    return s

get_triangle()


