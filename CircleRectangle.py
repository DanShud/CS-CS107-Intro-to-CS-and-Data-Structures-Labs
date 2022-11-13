"""
Lab 0: The Circle Rectangle
cs107 Introduction to Computer Science & Data Structures
Haverford College

Danylo Shudrenko

The function circleRectangleOverlap(centerX,centerY,radius,xmin,xmax,ymin,ymax) checks
whether the circle and rectangele overlap based on the coordinates of the circle center -
centerX,centerY and its radius - radius; and the left down coordinate an the right up coordinte
of the rectangle - centerX,centerY,radius,xmin,xmax,ymin,ymax

centerX,centerY,radius,xmin,xmax,ymin,ymax should be float
radius > 0


some examples:

# An obvious overlap:
>>> circleRectangleOverlap(100,20,8, 80,120, 18,25)
True

# An obvious miss:
>>> circleRectangleOverlap(100,20,8, 180,220, 18,25)
False

# An example when they only intercept
>>> circleRectangleOverlap(5, 7, 5, 10, 19, 4, 11)
False

# An example when circle contains rectangle
>>> circleRectangleOverlap(0, 0, 15, -4, 6, 1, 3)
True

# An example when rectangle contains circle
>>> circleRectangleOverlap(0, 0, 1, -5, 7, -4, 6)
True

"""

from math import *
from Logic import *

################## your code here ##############

def CRO(centerX: float,centerY: float,radius: float,xmin: float,xmax: float,ymin: float,ymax: float) -> bool:
    #preconditions
    assert isinstance(centerX, float) or isinstance(centerX, int)
    assert isinstance(centerY, float) or isinstance(centerY, int)
    assert isinstance(radius, float) or isinstance(radius, int)
    assert isinstance(xmin, float) or isinstance(xmin, int)
    assert isinstance(xmax, float) or isinstance(xmax, int)
    assert isinstance(ymin, float) or isinstance(ymin, int)
    assert isinstance(ymax, float) or isinstance(ymax, int)

    #lets check whether center of the circle between top and bottom side of the rectangle
    #of if one of the corner is between critical vertical dots of the circle
    verticalcheck = False
    if (xmin <= centerX <= xmax) or (centerX - radius < xmin and centerX + radius > xmin) or (centerX - radius < xmax and centerX + radius > xmax):
        verticalcheck = True
    #lets do the same with horizontal critical dots
    horizontalcheck = False
    if (ymin <= centerY <= ymax) or (centerY - radius < ymin < centerY + radius) or (centerY - radius < ymax < centerY + radius):
        horizontalcheck = True

    #if they are both true it means that the function is working
    if verticalcheck and horizontalcheck:
        return True
    else:
        return False

    # postcondtions if the function receives the information about a circle and rectangle
    # it would return True if they overlap and False if they not or if they only intercept

################################################
  
def circleRectangleOverlap(centerX: float,centerY: float,radius: float,xmin: float,xmax: float,ymin: float,ymax: float) -> bool:
    precondition(radius >= 0 and xmin <= xmax and ymin <= ymax)
    # postcondition: return true iff there exists x, y in both shapes...
    MODE:str = '2021'  # set to 'test samples', 'answer key', 'code review', or 'mine'
    
    if MODE=='mine':
        ####################### When writing circle-rectangle, write your code below #############
        # here's an example circle-rectangle algorithm that's a totally unsound idea but often works :-)
        if radius > 150:    # if the circle is Big
            return True        #  then it probably overlaps
        elif xmax-xmin > 150:     # also, if the rectangle is wide
            return True        #  then it probably overlaps
        elif ymax-ymin > 150:     # also, if the rectangle is tall
            return True        #  then it probably overlaps
        else:            # Otherwise, they're probably both small, so
            return False    #  let's hope they don't overlap
        ####################### When writing circle-rectangle, write your code above #############
    elif MODE=='2021':
        return CRO(centerX,centerY,radius,xmin,xmax,ymin,ymax)  # CALLING YOUR ALGORITHM ABOVE
        
    elif MODE=='code review':
        
        try:
            import circleRectangleToReview as review
        except:
            print("Your circleRectangleToReview.py file does not seem to be ready yet")
            return True
            
        return review.myCircleRectangleOverlap(centerX,centerY,radius,xmin,xmax,ymin,ymax)
        
    elif MODE=='answer key':
        return keyCircleRectangleOverlap(centerX,centerY,radius,xmin,xmax,ymin,ymax)
    elif MODE=='test samples':
        try:
            from CircleRectangleSamples import circleRectangleOverlapSamples
# the line below only works in the QuaCS lab computers
#           from sample_answers.cs105.Intersect.CircleRectangleSamples import circleRectangleOverlapSamples
            try:
                answer: bool = circleRectangleOverlapSamples(centerX,centerY,radius,xmin,xmax,ymin,ymax)
                return answer
            except:
                print("A sample solution had an error or failed a precondition.")
                print("This should have been caught by the lab files already, so please report it.")
                return True
        except:
            print("Hmmmm... can't find sample answers. This shouldn't happen on the CS teaching lab computers")
            print(" If you are running this program on another computer, you'll have to wait to check")
            print(" your test suite against the sample answers when you're back in the lab.")
            print(" (Remember to Team->Commit on your computer and Team->Update in the lab.)")
    
            return True  # Well, sometimes this is the right answer!            
    else:
        print('ERROR: You need to set MODE correctly in circleRectangleOverlap in circleRectangle.py')
        raise Exception
        return True

def keyCircleRectangleOverlap(centerX: float, centerY: float, radius: float, xmin: float, xmax: float, ymin: float, ymax: float) -> bool:

    return True  # The key will be released later, above this line

# The following gets the "doctest" system to check test cases in the documentation comments
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print(("Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!"))
    else:
        print("Rats!")

if __name__ == "__main__": _test()
