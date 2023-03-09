# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
from collections import Counter


def fib(n):
    counter = Counter()
    return fib_helper(n, dict({3: 2, 4: 3, 5: 5}), counter)


def fib_helper(n, d, counter=None):
    counter["calls"] += 1
    print(counter)
    if n < 3:
        return 1
    else:
        if n in d:
            return d.get(n)
        else:
            sum = fib_helper(n - 1, d, counter) + fib_helper(n - 2, d, counter)
            d[n] = sum
            return sum


print(fib(20))
