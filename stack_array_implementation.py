import array

class Stack():
    def __init__(self, size, type, value):
        self.size = size
        self.arr = array.array(type, [value]*self.size)
        self.top = -1

    def __str__(self):
        return str(self.arr)

    def push(self, x):
        if self.top  >= self.size - 1:
            print("Stack overflow")
        else:
            self.top = self.top + 1
            self.arr[self.top] = x

    def pop(self):
        if self.top == -1:
            print("Stack underflow")
        else:
            top = self.arr[self.top]
            self.arr[self.top] = 0
            self.top = self.top - 1
            return top

    def is_full(self):
        return self.top == self.size - 1

    def is_empty(self):
        return self.top == -1


s = Stack(3, 'i', 0)
reversed = Stack(3, 'i', 0)

s.push(3)
s.push(5)
s.push(7)
print(f"initial: {s}")

reversed.push(s.pop())
reversed.push(s.pop())
reversed.push(s.pop())
print(f"reversed: {reversed}")


integers = Stack(26, 'i', 0)
letters = Stack(26, 'u', 'A')

for i in range (65,91):
    integers.push(i)
print(f"integers: {integers}")

while integers.is_empty() == False:
    letters.push(chr(integers.pop()))
print(f"letters: {letters}")

