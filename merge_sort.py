import random

def test_data(n):
    """generate a list containing n randomised integer numbers"""
    #l = [random.randint(1, 12) for _ in range(n)]
    l = list(x for x in range(1, 12))[:n]
    random.shuffle(l)
    return l

def bar_chart(l):
    """print a bar chart representation of a list"""
    for i in range(len(l)):
        print(l[i]*'*')

def merge(l1, l2):
    """merge two sublists"""
    i = j = 0
    merged = []

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1

    while i < len(l1):
        merged.append(l1[i])
        i += 1
    while j < len(l2):
        merged.append(l2[j])
        j += 1

    return merged

counter = -1
def merge_sort(l):
    global counter
    counter += 1
    if len(l) == 1:
        return l
    middle = int(len(l) / 2)
    first_half = l[:middle]
    second_half = l[middle:]
    half_a = merge_sort(first_half)
    half_b = merge_sort(second_half)

    return merge(half_a,half_b)

def test_merge_sort():
    l = test_data(6)
    print("# before merge_sort")
    bar_chart(l)
    sorted = merge_sort(l)
    print("# after merge_sort")
    bar_chart(sorted)
    print(f'number of recursive calls: {counter}')

test_merge_sort()
