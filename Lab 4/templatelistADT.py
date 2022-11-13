"""
Lab 4: ListADT
cs107 Introduction to Computer Science & Data Structures
Haverford College
Danylo Shudrenko

Initial test cases:
>>> lst = listADT()
>>> assert lst.empty()
>>> lst = listADT("alpha", lst)
>>> assert not lst.empty()
>>> assert lst.rest().empty()
>>> assert lst.head() == "alpha"

My tests:
>>> lst = listADT("beta", lst) # adding one more element to the list

>>> lst1 = listADT("beta", listADT("alpha", listADT())) #creating identical list to lst

>>> assert lst1 == lst # two list equal

>>> lst1 = listADT("beta", lst1) #adding one more element
>>> assert not lst1 == lst #two list are not equal because of the size

>>> lst2 = listADT("a", listADT("b", listADT()))
>>> assert not lst2 == lst #two list are not equal because of the elements

>>> lstempty = listADT() #creating empty listADT
>>> lstempty.head() #exception for head method
The list is empty

>>> lstempty = listADT()
>>> lstempty.rest() #exception for rest method
The list is empty

>>> assert lst1.rest() == listADT("beta", listADT("alpha", listADT())) #checking the rest method

"""

class listADT:
    def __init__(self, head = None, rest = None):
        if head == None:            # empty constructor
            self.rep = []
        else:                       # extending constructor
            self.rep = [head] + rest.rep

    #precondtion
    #method "empty" doesn't take anything
    def empty(self):
        if len(self.rep) > 0:
            return False
        else:
            return True
    #postcondition
    #method return False if listADT is empty
    #if not, return True

    # precondtion
    # method "head" doesn't take anything
    def head(self):
        if self.empty(): #precondition
            print("The list is empty")
        else:
            return self.rep[0] #in our abstraction the head is the first element, so
            #the function return the first element of python list representation
    #postcondtion
    #return the first element of listADT
    # or print "The list is empty" if it is impossible

    # precondtion
    # method "rest" doesn't take anything
    def rest(self):
        if self.empty(): #precondtion
            print("The list is empty")
        else:
            temp = listADT()
            temp.rep = self.rep[1:]
            return temp #in our abstraction rest are all elements except for the fist one
            #therefore i return all elements from index one of python list representation
    #postcondtion
    #method reurn the rest of listADT
    # or print "The list is empty" if it is impossible

    # precondtion
    # method "__eq__" take another listADT
    def __eq__(self, other):
        if len(self.rep) != len(other.rep):#precondtion
            return False
        else:
            for i in range(len(self.rep)):
                if self.rep[i] != other.rep[i]:
                    return False #if we find at least one not same element it means that two listADT() are not equal
            return True
    #postcondtion
    #method return true if object self equals to another listADT given to the method
    #return False in all other cases

    def __str__(self):              # "abstraction function" (to text)
        return str(self.rep)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")

    
