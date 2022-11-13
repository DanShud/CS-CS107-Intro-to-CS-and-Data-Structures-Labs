"""
Lab 0: The Power Function
cs107 Introduction to Computer Science & Data Structures
Haverford College

Danylo Shudrenko

Recall: 2^3 == 2*2*2 == 8   AND   3^2 == 3*3 == 9 ...

Compute base to the exp power, for integer exp and real/float base.

There are much more efficient algorithms for exponentiation,
but our emphasis here is on simplicity rather than speed.

Examples of the power function:
>>> power(3, 3)
27

>>> power(3.0, 3)  # note that the ".0" is retained in the answer
27.0

>>> power(1.5, 2)   # 3/2 squared is 9/4
2.25

>>> power(2, 0)   # 2^0 == 1
1

>>> power(2, -2)   # 2^(-2) == 1/4 == 0.25
0.25

>>> power (-1, 4) # -1^4 == 1
1

>>> power (2, -3) # 2^(-3) == 1/8 = 0.125
0.125

>>> power (0, 2) # 0^2 == 0
0



When we don't want to write out _all_ the digits of the answer,
we put the "# doctest: +ELLIPSIS" at the end of the example question, like so
>>> power(0.9, 5)  # doctest: +ELLIPSIS
0.5904900...
"""

# make Python look in the right place for logic.py
import sys

sys.path.append('/home/courses/python')


# from Logic import *


def power(base: float, exp: int):
    # precondition
    assert base != 0 or exp !=0 #Math typicaly descirbes 0^0 as undefined
    assert isinstance(base, float) or isinstance(base, int)
    assert isinstance(exp, int)

    res = 1
    if exp != 0:
        if exp > 0:
            for i in range(exp):
                res *= base
        else:
            for i in range(-exp):
                res /= base

    #postcondition if the function input is two float numbers base and exp
    #the function would return the base^exp
    assert isinstance(res, float) or isinstance(res, int)

    return res


def simple_power_ui():
    # doctest use, as per http://docs.python.org/lib/module-doctest.html
    import doctest
    print("First, trying out tests from the initial comment in power.py...")
    doctest.testmod()

    print(" ")  # get a blank line
    print("Now you try one!")
    users_base = float(input("Enter the base: "))
    users_exp = int(input("Enter the exponent: "))
    if (type(users_exp) == type(1)):
        print(power(users_base, users_exp))
    else:
        print("Sorry, the exponent must be an integer!")


# run the user interface only if we're not importing this for some other program
# I copied this from http://docs.python.org/lib/module-doctest.html
if __name__ == "__main__":
    simple_power_ui()
