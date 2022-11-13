"""
Lab 0: The Circle Function
cs107 Introduction to Computer Science & Data Structures
Haverford College

Danylo Shudrenko

The function circleOverlap(x1, y1, r1, x2, y2, r2) checks whether two circles overlap
based on the coordintaes of their centers - x1, y1 and x2, y2
and the length of their radius r1, r2

x1, x2, y1, y2, r1, r2 should be float
We don't allow a circle with negative radius


# An obvious overlap (Sample answer #3 got this wrong):
>>> circleOverlap(100,100,30, 125,100,30)
True

# An obvious non-overlap (Sample answer #1 gets this one wrong):
>>> circleOverlap(100,100,30, 225,100,30)
False

# An example copied from the "Console" window during a run of overlap-test-graphics
>>> circleOverlap( 160 ,  152 ,  82.8070045346 ,  198 ,  167 ,  93.813645063 )
True

#An example when circle intercept
>>> circleOverlap(10, 17, 5, 20, 17, 5)
False

#An example if one circle inside of another
>>> circleOverlap(5, 6, 3, 0, 0, 12)
True

"""

from math import *


################## your code here ##############

def CircleCircle(x1: float, y1: float, r1: float, x2: float, y2: float, r2: float) -> bool:
    # preconditions
    assert isinstance(x1, float) or isinstance(x1, int)
    assert isinstance(x2, float) or isinstance(x2, int)
    assert isinstance(y1, float) or isinstance(y1, int)
    assert isinstance(y2, float) or isinstance(y2, int)
    assert isinstance(r1, float) or isinstance(r1, int)
    assert isinstance(r2, float) or isinstance(r2, int)
    assert r1 >= 0 and r2 >= 0

    # finding the distance between centers
    ans = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

    # if the distance is less than the sum of radius it means that circles overlap
    if ans < r1 + r2:
        return True
    else:
        return False
    # postcondtions if the function receive the information about two circle
    # it would return True if they overlap and False if they not or if they only intercept


################## your code here ##############


def circleOverlap(x1: float, y1: float, r1: float, x2: float, y2: float, r2: float) -> bool:
    assert (r1 >= 0 and r2 >= 0)
    # postcondition: return true iff there exists x,y in both circular regions, including being on the edge

    MODE: str = '2021'  # set to 'test samples' or 'mine'

    if MODE == '2021':
        return CircleCircle(x1, y1, r1, x2, y2, r2)
    elif MODE == 'test samples':
        from CircleSamples import circleOverlapSamples
        # the line below only works in the QuaCS lab computers
        #        from sample_answers.cs105.Intersect.Ci5rcleSamples import circleOverlapSamples
        answer: bool = circleOverlapSamples(x1, y1, r1, x2, y2, r2)
        return answer
    else:
        print('ERROR: You need to set MODE correctly in circleRectangleOverlap in circleRectangle.py')
        raise Exception


# The following gets the "doctest" system to check test cases in the documentation comments
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print("Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!")
    else:
        print("Rats!")


if __name__ == "__main__": _test()
