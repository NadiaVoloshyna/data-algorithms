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

print(fib(7))
"""
{1} Clear Python coding, good effort! A few suggestions to follow.
{2} ...singly_linked_list.py code: consider moving everything as from line 101 into a function.  
    Call the function linked_list_demo() (or something similar) and call the function, in order to demonstrate the characteristics of your linked list.
{3} Unit testing:  it appears that you have understood the principles, and you have documented this well (the SinglyLinkedList_test.png screen shot is perfect!).
{4} 2D array: consider writing a second version of the twoDimensionalList() function, maybe with 3 parameters: startx, starty, fieldsize.  
    The "field size" parameter would add some flexibility to your function (as you would allow the caller to determine the size of the chess board fields), 
    and you would get rid of the "magic number" 40 in your code.
{5} For loop versus while loop: in principle, consider using _for_ if you know how many iterations will take place.  
    Use a _while_ if you don't know the number of iterations in advance.  For the 2D array (known: 8 by 8 layout), you could probably use 2 for loops, 
    maybe in combination with 2 constant values: the number of rows and the number of columns.
{6} class Field: try to find descriptive names for your variables and parameters (so that you don't need to explain in a comment what the names mean :-) - in this case: a, b, c, d )  
{7} function drawChessBoard(): your current solution contains nested while loops - you appear to say: "I don't know how many iterations we need here.".  
    But you do know: we need 8 * 8 -> I'd use 2 nested for loops, one for x, one for y, starting with appropriate x/y values, step width: 40.  
    (And for switching the field colours, you can introduce a variable that starts at 0, increases by 1 at every iteration, and use % 2 for "oszillating" between 0 and 1).	
{8} One tiny niggle: in Python, function names should be written in lower case (with underscores if need be).  This seems to be a general consensus in the Python community.  
    Be consistent when naming your functions; eg avoid something like getList() (should probably be: get_list).  See: https://peps.python.org/pep-0008/#naming-conventions
"""
"""
{2} Tasks 1 & 2: consider factoring out the actual _search_ code ie have a dedicated linear_ and binary_ search function, respectively (they can be called from search_steps..)
{3} Task 2: is_sorted() - this is good!  However, remember that Python allows you to write brief code ... eg one of your colleagues had just coded this as a one-liner:  
def is_sorted(data): return sorted( data ) == data
{4} Task 2: checking for duplicates - hint: a Python set allows unique values (only)
"""
"""
{2} Resist the temptation of _printing_ in the sorting function.  You can return a tuple ie several names, eg return _list, passes, swaps , and the print on the "client side".
{3} Bubble sort test data: the task was: to _generate_ the test data. (I thought that you'd have preferred this over typing in the 3 different lists.)
"""