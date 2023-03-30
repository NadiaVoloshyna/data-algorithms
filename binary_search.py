import random
from linear_search import test_data

def is_sorted(l):
    """checks if the data is sorted"""
    count = 0
    for i in range(len(l) - 1):
        if l[i] <= l[i+1]:
            count += 1
            if count == len(l) - 1:
                return True
        else:
            return False

def check_duplicates(l):
    """checks if the data contains duplicates"""
    if is_sorted(l):
        for i in range(len(l) - 1):
            if l[i] == l[i+1]:
                return True
        return False

def binary_search_steps(runs,elements):
    """creates a list with the amount of steps to find (or: not find) a target value"""
    results = []

    for i in range(runs):
        target = round(random.random() * elements) + 2
        print(f'target: {target}') ###
        l = list(test_data(elements))
        random.shuffle(l) ###
        print(l) ###
        left = 0
        right = len(l) - 1
        steps = 0
        flag = False

        while left <= right:
           midpoint = (left + right) // 2
           steps += 1
           if target == l[midpoint]:
              flag = True
              results.append(steps)
              print(f'target index is: {midpoint}') ###
              break
           elif l[midpoint] > target:
              right = midpoint - 1
           elif l[midpoint] < target:
              left = midpoint + 1
        if not flag:
            results.append(steps)

    print(f'number of steps, binary search: {results}')
    print(f'average number of steps:        {sum(results) / runs}')

binary_search_steps(4,10)
print('------------------------------')

def tests():
    print('10 elements:')
    binary_search_steps(4,10)
    print('100 elements:')
    binary_search_steps(4,100)
    print('1,000 elements:')
    binary_search_steps(4,1000)
    print('10,000 elements:')
    binary_search_steps(4,10000)
    print('100,000 elements:')
    binary_search_steps(4,100000)
    print('1,000,000 elements:')
    binary_search_steps(4,1000000)

#tests()
