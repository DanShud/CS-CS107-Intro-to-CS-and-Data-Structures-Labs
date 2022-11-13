"""
Lab 1: The Circle Function
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

>>> circleOverlap(100,100,3, 125,100,3)
False

# An obvious non-overlap (Sample answer #1 gets this one wrong):
>>> circleOverlap(100,100,30, 225,100,30)
False

# An example copied from the "Console" window during a run of overlap-test-graphics
>>> circleOverlap( 160 ,  152 ,  82.8070045346 ,  198 ,  167 ,  93.813645063 )
True

>>> circleOverlap( 240 ,  260 ,  52.354560450833695 ,  160 ,  346 ,  85.95929269136641 )
True

>>> circleOverlap( 166 ,  92 ,  53.71219600798314 ,  288 ,  236 ,  52.009614495783374 )
False

#An example when circle intercept(only one dot of intercept)
>>> circleOverlap(10, 17, 5, 20, 17, 5)
True

#An example if one circle is inside of another
>>> circleOverlap(5, 6, 3, 0, 0, 12)
True

"""

from math import *
from point import *         # implemented in another file

################### work on the implementation oif this class #########

# sort of OO .. you should improve this implementation to use points appropriately 
class circle:
    def __init__(self, p: Point, r: float):
        # preconditions
        assert isinstance(p, Point)
        assert isinstance(r, float) or isinstance(r, int)
        assert r >= 0
        self.point = p
        self.r = r
        #postconditions
        #creating the class

    def getX(self) -> float:    # accessor
        # preconditions
        assert isinstance(self, circle)
        return self.point.x #postconditions returning X of the point of the circle center

    def getY(self) -> float:    # another accessor
        # preconditions
        assert isinstance(self, circle)
        return self.point.y #postconditions returning X of the point of the circle center

    def getRadius(self) -> float:   # yes, another accessor
        # preconditions
        assert isinstance(self, circle)
        return self.r #postconditions returning R of the circle

    def __str__(self) -> str:      # accessor for display
        return 'Circle with center at (' + str(self.point.x) + ', ' + str(self.y) + ') with radius ' + str(self.r)

    def overlap(self, other) -> bool:       # accessor again
        #preconditions
        assert isinstance(self, circle) and isinstance(other, circle)
        Rsum = self.r + other.r
        #deltaX = self.x - other.getX()              # <== you should look at these two lines, ...
        #deltaY = self.getY() - other.y              # <== .. what is going on?
        #I checnged the line above with build in function in Point for finding distance between two points
        distance = self.point.howfarfrom(other.point) #finding the distance between centers

        #if the distance between center equals or is less then sum of radius - circles overlap
        return distance <= Rsum
        #postconditions the function returns True if circles have at least one common point

########## rewrite the ABOVE class to improve degree of OO, and review below ############ 
        
def OOcircle(c1: circle, c2: circle) -> bool:       # handoff, connecting original to OOP
    return c1.overlap(c2)
    
def CircleCircle(x1: float,y1: float,r1: float,x2: float,y2: float,r2: float) -> bool:
   return OOcircle(circle(Point(x1, y1), r1), circle(Point(x2, y2), r2))

########## you should not NEED to view/change anything below ###############
    
def circleOverlap(x1: float,y1: float,r1: float,x2: float,y2: float,r2: float) -> bool:
    assert (r1 >= 0 and r2 >= 0)
    # postcondition: return true iff there exists x,y in both circular regions, including being on the edge

    MODE: str = '2022'  # set to 'test samples' or 'mine'
    
    if MODE =='2022':
        return CircleCircle(x1,y1,r1,x2,y2,r2)
    elif MODE =='test samples':
        from CircleSamples import circleOverlapSamples
# the line below only works in the QuaCS lab computers
#        from sample_answers.cs105.Intersect.Ci5rcleSamples import circleOverlapSamples
        answer: bool = circleOverlapSamples(x1,y1,r1,x2,y2,r2)
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
