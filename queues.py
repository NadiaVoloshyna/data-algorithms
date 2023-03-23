from collections import deque

def queue_demo():
    d = deque(map(lambda x: x**2, range(1,11)))
    print(d)

    for el in range(len(d) - 1):
        d.popleft()
        print(d)

queue_demo()

def sort_deque():
    print("before using sorted(): ", type(deque([8, 93, 32, 90, 42, 93, 51, 14, 41])))

    """sorted() does not sort in-place, sorted(iterable) returns a new list containing all items from the iterable in ascending order."""
    sorted_deque = sorted(deque([8, 93, 32, 90, 42, 93, 51, 14, 41]))
    print(sorted_deque)
    print("after using sorted(): ", type(sorted_deque))

    # sorted_deque.popleft()
    print(sorted_deque.pop())
    print(sorted_deque.pop())
    print(sorted_deque.pop())

sort_deque()