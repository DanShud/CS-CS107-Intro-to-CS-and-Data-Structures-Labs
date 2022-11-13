"""
Lab 2: F3 function
cs107 Introduction to Computer Science & Data Structures
Haverford College
Danylo Shudrenko

The function finds the n number in fibonacci sequence for 3 numbers. Please see algebraic formula below:
f3(n)   === 1  if n < 3
        === f3(n-1) + f3(n-2) + f3(n-3)

The functio allows not negative integers intergers.

>>> print(4, f3(4))
4 5

>>> print(10, f3(10))
10 193

# cases with initial numbers
>>> print(0, f3(0))
0 1

>>> print(2, f3(2))
2 1

#general case for 7 f(0) = 1, f(1) = 1, f(2) = 1, f(3) = 3, f(4) = 5, f(5) = 9, f(6) = 17, f(7) = 31
>>> print(7, f3(7))
7 31


"""

import time
import math


def f3(n: int) -> int:
    #preconditions
    assert isinstance(n, int)
    assert n >= 0

    #f3(n)   === 1  if n < 3
    if n < 3:
        return 1
    #to use less memory i will not recreate all sequence and will use only last three elements in sequence
    f_1 = 1
    f_2 = 1
    f_3 = 1

    #f3(n)  === f3(n-1) + f3(n-2) + f3(n-3)
    #in my code res = f_3 + f_2 + f_1
    for i in range(n - 2):
        res = f_1 + f_2 + f_3
        f_1 = f_2
        f_2 = f_3
        f_3 = res

    # postcondtions function return the positive integer number - the f3(n), where f3 - fibonacci sequence
    assert isinstance(f_3, int)
    assert f_3 > 0
    return f_3






inputs = [2, 4, 8, 16, 32, 64]

for n in inputs:
    start = time.time()
    for i in range(1000):
       f3(n)
    stop = time.time()
    print("elapsed time: ", stop - start)


if __name__ == "__main__":
    # doctest use, as per http://docs.python.org/lib/module-doctest.html
    import doctest
    doctest.testmod()
    print("doctests complete")
