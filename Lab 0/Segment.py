"""
Lab 0: The Circle Rectangle
cs107 Introduction to Computer Science & Data Structures
Haverford College

Danylo Shudrenko

The function segmentOverlap(x1, y1, x2, y2, x3, y3, x4, y4) checks whether two
segments intrecept based on their coordinates - x1, y1, x2, y2, x3, y3, x4, y4
x1, y1, x2, y2, x3, y3, x4, y4 have to be float

#an obvious intercept
>>> segmentOverlap(0, 0, 5, 5, 0, 5, 5, 0)
True

#an obvios miss
>>> segmentOverlap(0, 0, 5, 5, 0, 5, 1, 4)
False


#one of segment is dot and another segment contains it
>>> segmentOverlap(0, 0, 0, 0, -1, -1, 1, 1)
True

#One of segments is vertical and intercept another
>>> segmentOverlap(0,0, 0, 5, -1, 0, 3, 3)
True

#One segment is vertical and doesn't intercept another
>>> segmentOverlap(0,0, 0, 5, -1, 0, -3, -3)
False

#Both segments are vetical and intercept
>>> segmentOverlap(0, 0, 0, 5, 0, 3, 0, 6)
True

#Both segments are vertical and do not intercept
>>> segmentOverlap(0, 0, 0, 5, 1, 0, 1, 5)
False

#one of segment is a dot and another segment does not contain it
>>> segmentOverlap(0, 0, 0, 0, 0, 5, 10, 15)
False

#both segments are dots, but the different one
>>> segmentOverlap(0, 0, 0, 0, 1, 1, 1, 1)
False

#both segments are dots, and they are the same dot
>>> segmentOverlap(0, 0, 0, 0, 0, 0, 0, 0)
True

#segments are paralel but lies on different lines - obviously, do not intercept
>>> segmentOverlap(0, 0, 10, 10, 0, 5, 10, 15)
False

#segments are paralel lies on one line and don't intercept
>>> segmentOverlap(100,100,200,200,300,300,400,400)
False

#segments are paralel and intercept
>>> segmentOverlap(100, 100, 200, 200, 150, 150, 170, 170)
True


>>> segmentOverlap( 83 ,  259 ,  263 ,  110 ,  101 ,  191 ,  229 , 214 )
True

>>> segmentOverlap( 105 ,  270 ,  226 ,  86 ,  113 ,  219 ,  239 , 160 )
True

>>> segmentOverlap( 163 ,  260 ,  83 ,  205 ,  117 ,  326 ,  117 , 150 )
True
"""


from math import *    
from Logic import *

################## your code here ##############

#function which finds the distance between two dots

def DotDistance(x1: float, y1: float, x2: float, y2: float):
    #preconditons only float numbers
    assert isinstance(x1, float) or isinstance(x1, int)
    assert isinstance(x2, float) or isinstance(x2, int)
    assert isinstance(y1, float) or isinstance(y1, int)
    assert isinstance(y2, float) or isinstance(y2, int)

    res = sqrt((x1 - x2) * (x1 -x2) + (y1 -y2) *(y1 - y2))

    #postcondtions
    assert res >= 0

    return res
    #postconditions function finds the distance between two dots


def SSO(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float) -> bool:
    #preconditions all variables are float
    assert isinstance(x1, float) or isinstance(x1, int)
    assert isinstance(x2, float) or isinstance(x2, int)
    assert isinstance(y1, float) or isinstance(y1, int)
    assert isinstance(y2, float) or isinstance(y2, int)
    assert isinstance(x3, float) or isinstance(x3, int)
    assert isinstance(x4, float) or isinstance(x4, int)
    assert isinstance(y3, float) or isinstance(y3, int)
    assert isinstance(y4, float) or isinstance(y4, int)
    #lets create coordinates for the dot of intercept
    #lets check whether the first segment is a dot
    if x1 == x2 and y1 == y2:
        #if they are both dots
        if x3 == x4 and y3 == y4:
            # if it's one dot it means they intercept
            if x1 == x3 and y1 == y3:
                return True
            else:
                return False
        else:
        #if only one of the  segment is dot then we need to check whether it belongs to another segment
        #I will check whether distance from this dot to ends of the another segment is equal to the length of the second segment
            if DotDistance(x3, y3, x4, y4) == DotDistance(x1,y1, x3, y3) + DotDistance(x1,y1, x4, y4):
                return True
            else:
                return False

    #lets check whether the second segment is a dot

    if x3 == x4 and y3 == y4:
        #lets check whether it belong to the first segment analogically to the previous case(see above)
        if DotDistance(x1,y1, x2, y2) == DotDistance(x1, y1, x3, y3) + DotDistance(x2, y2, x3, y3):
            return True
        else:
            return False


    #lets find the equation of line A containing the fist segment y_a = k_a * x + cA
    # there is an exception if line is vertical:
    if x2 - x1 != 0:
        k_a = (y2 - y1) / (x2 - x1)
    else:
        k_a = 0
    c_a = y1 - k_a * x1

    #lets find the equation of line B for containing fist segment y_b = k_b * x + cB
    #there is an exception if line is vertical:
    if x4 - x3 != 0:
        k_b = (y4 - y3)/(x4 - x3)
    else:
        k_b = 0
    c_b = y3 - x3 * k_b

    #if line A and B are vertical
    if x2 == x1 and x3 == x4:
        #if it is different lines - obviously, it would be false
        if x1 != x3:
            return False
        else:
            # lets check whether they intercept by checking
            # whether one of the ends of the one segments belongs to another segment
            if DotDistance(x1, y1, x2, y2) == DotDistance(x1, y1, x3, y3) + DotDistance(x2, y2, x3, y3) or DotDistance(
                    x1, y1, x2, y2) == DotDistance(x1, y1, x4, y4) + DotDistance(x2, y2, x4, y4):
                return True
            if DotDistance(x3, y3, x4, y4) == DotDistance(x1, y1, x3, y3) + DotDistance(x1, y1, x4, y4) or DotDistance(
                    x3, y3, x4, y4) == DotDistance(x2, y2, x3, y3) + DotDistance(x2, y2, x4, y4):
                return True
            return False
            # if it is not the case it means the do not intercept
    #if only line A is vertical
    if x1 == x2:
        #lets find the dot of intercept of line A and B
        x_intercept = x1
        y_intercept = x1 * k_b + c_b
        # lets check whether it belongs to the segments
        # to do so we need to check whether distance from this dot
        # to both ends of each segment equals the length of the segments

        if DotDistance(x1, y1, x2, y2) == DotDistance(x1, y1, x_intercept, y_intercept) + DotDistance(x2, y2,
                                                                                                      x_intercept,
                                                                                                      y_intercept) and DotDistance(
                x3, y3, x4, y4) == DotDistance(x3, y3, x_intercept, y_intercept) + DotDistance(x4, y4, x_intercept,
                                                                                               y_intercept):
            return True
        else:
            return False

    #lets do the same if the line B is vertical
    if x3 == x4:
        x_intercept = x3
        y_intercept = x3 * k_a + c_a
        # lets check whether it belongs to the segments
        # to do so we need to chech whether distance from this dot
        # to both ends of each segment equals the length of the segments

        if DotDistance(x1, y1, x2, y2) == DotDistance(x1, y1, x_intercept, y_intercept) + DotDistance(x2, y2,
                                                                                                      x_intercept,
                                                                                                      y_intercept) and DotDistance(
                x3, y3, x4, y4) == DotDistance(x3, y3, x_intercept, y_intercept) + DotDistance(x4, y4, x_intercept,
                                                                                               y_intercept):
            return True
        else:
            return False


    #lets check if these lines are parallel lines
    #if yes, the segments overlap only in case they lie on the same line
    if k_a == k_b:
        if c_a == c_b:
            #lets check whether they intercept by checking
            #whether one of the ends of the one segments belongs to another segment
            if DotDistance(x1,y1, x2, y2) == DotDistance(x1, y1, x3, y3) + DotDistance(x2, y2, x3, y3) or DotDistance(x1,y1, x2, y2) == DotDistance(x1, y1, x4, y4) + DotDistance(x2, y2, x4, y4):
                return True
            if DotDistance(x3, y3, x4, y4) == DotDistance(x1,y1, x3, y3) + DotDistance(x1,y1, x4, y4) or DotDistance(x3, y3, x4, y4) == DotDistance(x2, y2, x3, y3) + DotDistance(x2, y2, x4, y4):
                return True
            #if it is not the case it means the do not intercept
            return False
        else:
            return False
    else:
        #lets find the dot of intercept of the lines
        x_intercept = (c_b - c_a) / (k_a - k_b)
        y_intercept = k_a * x_intercept + c_a


        #lets check whether it belongs to the segments
        #to do so we need to chech whether distance from this dot
        #to both ends of each segment equals the length of the segments

        if DotDistance(x1,y1,x2,y2) == DotDistance(x1, y1, x_intercept, y_intercept) + DotDistance(x2, y2, x_intercept, y_intercept) and DotDistance(x3,y3,x4,y4) == DotDistance(x3, y3, x_intercept, y_intercept) + DotDistance(x4, y4, x_intercept, y_intercept):
           return True
        else:
            return False
        #postcondtions function receives information about two segments(the function coonsiders dots as segments)
        #and check whether they intercept(for dots: if one dot belongs to another segments or it is the same dot)


################################################
            
def segmentOverlap(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float) -> bool:
    MODE: str = '2021'  # set to 'test samples' or 'mine'
    if MODE=='2021':
        return SSO(x1, y1, x2, y2, x3, y3, x4, y4)
    elif MODE == 'test samples':
        from SegmentSamples import segmentOverlapSamples
# the line below only works in the QuaCS lab computers
#        from sample_answers.cs105.Intersect.SegmentSamples import segmentOverlapSamples
        answer: bool = segmentOverlapSamples(x1, y1, x2, y2, x3, y3, x4, y4)
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
