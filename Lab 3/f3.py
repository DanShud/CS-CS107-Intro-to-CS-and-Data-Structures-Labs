"""
Lab 3: complexity revisited -- recall ...
cs107 Introduction to Computer Science & Data Structures
Haverford College

Danylo Shudrenko

>>> print(4, f3(4))
4 5

>>> print(10, f3(10))
10 193

>>> print(0, f3(0)) #the case when fucntion doesn't start loop/recursion
0 1

# >>> print(-1, f3(1)) it wil raise assertion error

>>> print(5, f3(5))
5 9

"""

import time
import math

def f3loop(n: int) -> int:
    #precondtions
    assert isinstance(n, int)
    assert n >= 0

    if (n < 3):
        return 1
    f0 = 1 #the first out of three last fibonacci numbers
    f1 = 1 #the second out of three last fibonacci numbers
    f2 = 1 #the third out of three last fibonacci numbers
    for i in range(3, n + 1):
        fnew = f2 + f1 + f0 #the fibonacci number №i
        f0 = f1 #moving forward our last thee fibonacci numbers
        f1 = f2 #moving forward our last thee fibonacci numbers
        f2 = fnew #moving forward our last thee fibonacci numbers
    return f2
    #postconditions
    #functions return the №n fibonacci number, which are described algebraically as
    #f3(n)   === 1  if n < 3
    #    === f3(n-1) + f3(n-2) + f3(n-3)
    #function is implented using loop

def f3tail(n: int) -> int:
    # precondtions
    assert isinstance(n, int)
    assert n >= 0

    if (n < 3): # based on the definition of fibonacci numbers
        return 1

    def f3rec (n, pre1, pre2, pre3):
        #precondtions
        #functions receives 3 previous fibonacci numbers
        #and number of the next fibonacci numbers it needs to find

        if n < 3: #if the function  reached the number, it was searching for
            return pre3
        else:
            return f3rec(n - 1, pre2, pre3, pre1 + pre2 + pre3)
            #recursively calling the function again, and moving
            #the 3 previous numbers forward by the definintion of the fibonacci numbers
            #and decrease the number of the next fibonacci numbers we need to find

    #postconditions
    ## functions return the №n fibonacci number, which are described algebraically as
    # f3(n) === f3(n-1) + f3(n-2) + f3(n-3), n > 3
    # function is implented using tail recursion


    return f3rec(n, 1, 1, 1)
    # postconditions
    # functions return the №n fibonacci number, which are described algebraically as
    # f3(n)   === 1  if n < 3
    #    === f3(n-1) + f3(n-2) + f3(n-3)
    # function is implented using tail recursion

f3 = f3tail    # replace with name of function to execute/test


#if you want to time, remove comment delimiters

start = time.time()
for n in range(100, 999, 10):
    print(n, f3(n))
stop = time.time()
print("elapsed time: ", stop - start)


if __name__ == "__main__":
    # doctest use, as per http://docs.python.org/lib/module-doctest.html
    import doctest
    doctest.testmod()
    print("doctests complete")
