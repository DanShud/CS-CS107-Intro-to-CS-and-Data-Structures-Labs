"""
Lab 1: Complex Numbers
cs107 Introduction to Computer Science & Data Structures
Haverford College

Danylo Shudrenko



>>> print(myComplex(4, 5))
4 + 5i

>>> print(myComplex(4, 5).add(myComplex(2,-2)))
6 + 3i

>>> print(myComplex(4, 5).add(myComplex(2,-2)).equals(myComplex(6, 3)))
True

>>> print(myComplex(6,9).equals(myComplex(6, 3)))
False



>>> print(myComplex(4, 5) + myComplex(2,-2))
6 + 3i

>>> print(myComplex(4, 5) + (myComplex(2,-2)) == (myComplex(6, 3)))
True

>>> print(myComplex(0, 0))
0 + 0i

>>> print(myComplex(1.6, 2.4).add(myComplex(1.5, 1.3)))
3.1 + 3.7i

>>> print(myComplex(1.5, 2.6).add(myComplex(1.5, 1.3)).add(myComplex(1.1, 1.1)))
4.1 + 5.0i

>>> myComplex(1.5, 2.7).add(myComplex(1.5, 1.3)).add(myComplex(1.1, 1.1)) == myComplex(4.1, 5.1)
True

>>> myComplex(1.5, 2.7).add(myComplex(1.5, 1.3)).add(myComplex(1.1, 1.1)) == myComplex(4.0, 5.1)
False

>>> (myComplex(1.5, 2.7) + myComplex(1.5, 1.3) + myComplex(1.1, 1.1)).equals(myComplex(4.1, 5.1))
True

>>> (myComplex(1.5, 2.7)+myComplex(1.5, 1.3) + myComplex(1.1, 1.1)).equals(myComplex(4.1, 5.0))
False
"""
# Lab 1 template    cs107   Fall 2022

class myComplex:            # basic complex number object/class
    def __init__(self, realpart, imagpart):
        #precondtions
        assert isinstance(realpart, float) or isinstance(realpart, int)
        assert isinstance(imagpart, float) or isinstance(imagpart, int)
        self.r = realpart
        self.i = imagpart
        #postcondtions create a class

    def add(self, other):   # addition of complex numbers
        # precondtions
        assert isinstance(self, myComplex) or isinstance(other, myComplex)
        return myComplex(self.r + other.r, self.i + other.i)
        #postconditions function adds two numbers


    def __add__ (self, other):
        # precondtions
        assert isinstance(self, myComplex) or isinstance(other, myComplex)
        return (self.add(other))
        #postconditions
        #redifining of "+" is from
        #https://www.geeksforgeeks.org/operator-overloading-in-python/

    def equals(self, other):
        # precondtions
        assert isinstance(self, myComplex) or isinstance(other, myComplex)
        return self.r == other.r and self.i == other.i
        #postcondition
        #returns true if the two complex numbers are equal


    def __eq__ (self, other):
        # precondtions
        assert isinstance(self, myComplex) or isinstance(other, myComplex)
        return (self.equals(other))
        #postcondtion
        # redifining of "==" is from
        # https://www.geeksforgeeks.org/operator-overloading-in-python/

    def __str__(self):      # display accessor
        # precondtions
        assert isinstance(self, myComplex) or isinstance(other, myComplex)
        return str(self.r)+' + '+str(self.i)+'i'
        #postconditions returns the  complex number

if __name__ == "__main__":
    # doctest use, as per http://docs.python.org/lib/module-doctest.html
    import doctest
    doctest.testmod()
    print("doctests complete")
