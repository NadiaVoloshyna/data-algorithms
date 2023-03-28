import random

def test_data(max_value):
    """generates numbers from 1 up to a specified maximum"""
    count = 1
    while count <= max_value:
        yield count
        count += 1

def linear_search_steps(runs, elements):
    """creates a list with the amount of steps to find (or: not find) a target value"""
    results = []

    for i in range(runs):
        target = round(random.random() * elements) + 2
        print(f'target: {target}')
        l = list(test_data(elements))
        random.shuffle(l)
        print(f'test data: {l}')
        steps = 0
        flag = False

        for el in range(len(l)):
            steps += 1
            if l[el] == target:
                flag = True
                results.append(steps)
                break
        if not flag:
            results.append(steps)

    print('--------------------------------------------------')
    print(f'number of steps: {results}')
    print(f'average number of steps: {sum(results) / runs}')

linear_search_steps(4,10)




