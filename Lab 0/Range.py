"""
Range Overlap demo

>>> assert rangeOverlap(1,4,2,5)
>>> assert rangeOverlap(1,2,2,5)
>>> assert not rangeOverlap(1,2,2.1,5)
>>> assert rangeOverlap(1,6,2,5)

"""

from math import *

    
def rangeOverlap(min1:float,max1:float,min2:float,max2:float):
    assert min1 <= max1 and min2 <= max2
    # postcondition: return true iff there exists x,y in both circular regions, including being on the edge
    """postcondition: return true iff there exists x such that min1 <= x <= max1 and min2 <= x <= max2 """
    return min1<=max2 and min2<=max1

# The following gets the "doctest" system to check test cases in the documentation comments
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print("Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!")
    else:
        print("Rats!")

if __name__ == "__main__": _test()
