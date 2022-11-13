""" point class from lecture

    Rajesh Kumar and John Dougherty
    Haverford College  cs107

>>> Point(5,9).showmydetails()
I look like: (5,9)


>>> Point(5,9).howfarfrom(Point(5,9))
0.0

>>> Point(5,9).howfarfrom(Point(-3, -6))
17.0

Extra tests

>>> Point(5.6,-0.7).showmydetails()
I look like: (5.6,-0.7)

>>> Point(0,0).howfarfrom(Point(0,0))
0.0
"""

import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x 
        self.y = y 
   
    def showmydetails(self):
        print("I look like: ({},{})".format(self.x, self.y))
    
    def move(self, newx, newy):
        self.x= newx
        self.y = newy
        
    def howfarfrom(self,theother):
        return math.sqrt((self.x-theother.x)**2+(self.y-theother.y)**2)


def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print("Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!")
    else:
        print("Rats!")

if __name__ == "__main__": _test()
