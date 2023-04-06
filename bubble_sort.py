l1 = ['TTT', 'TTG', 'TTC', 'TTA', 'TCT',  'TCC', 'GTT',  'GTG', 'GTC', 'GTA', 'GCT', 'GCG', 'GCC', 'GCA', 'CTT', 'CTG',
     'CTC', 'CTA', 'CCT', 'CCG', 'CCC', 'CCA', 'ATT', 'ATG', 'ATC', 'ATA', 'ACT', 'ACG', 'ACC', 'ACA' ]
l2 = ['ACA', 'ACG', 'ACC', 'ATA', 'ATG', 'ATT', 'ATC', 'ACT', 'GCA', 'GCG', 'GCT', 'GCC', 'TCT', 'TCC', 'GTA', 'GTG',
     'GTT', 'GTC', 'TTA', 'TTG', 'TTT', 'TTC', 'CCA', 'CCG', 'CCT', 'CCC', 'CTA', 'CTG', 'CTT', 'CTC']
l3 = ['ACA', 'ACC', 'ACG', 'ACT', 'ATA', 'ATC', 'ATG', 'ATT', 'CCA', 'CCC', 'CCG', 'CCT', 'CTA', 'CTC', 'CTG', 'CTT',
      'GCA', 'GCC', 'GCG', 'GCT', 'GTA', 'GTC', 'GTG', 'GTT', 'TCC', 'TCT', 'TTA', 'TTC', 'TTG', 'TTT']

#  exchange the positions of two items in the list
def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

# determine if a list is in descending order
def order_test(l):
    return all(l[i] >= l[i+1] for i in range(len(l)-1))

def bubble_sort(l):
    test = order_test(l)
    n = len(l)
    steps = 0
    swaps = 0
    swapped = False

    while n > 1:
        steps += 1
        for i in range(1, n):
            if l[i] < l[i - 1]:
                swap(l, i, i - 1)
                swaps += 1
                swapped = True
        if not swapped:
            print(f'best case O(n) - swaps: {swaps}, steps: {steps}')
            return l
        n -= 1

    if test:
        print(f'worst case O(n2) - swaps: {swaps}, steps: {steps}')
    else:
        print(f'average case O(n2) - swaps: {swaps}, steps: {steps}')
    return l

def test_bubble_sort():
    # the worst-case - the given list is in descending order
    print(bubble_sort(l1))
    # the average case
    print(bubble_sort(l2))
    # the best case - the given list is already sorted
    print(bubble_sort(l3))

test_bubble_sort()




