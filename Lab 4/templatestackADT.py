"""
Lab 4: stackADT
cs107 Introduction to Computer Science & Data Structures
Haverford College
Danylo Shudrenko

Initial test cases:

>>> stk = stackADT()
>>> assert stk.empty()
>>> stk.push("omega")
>>> assert not stk.empty()
>>> assert stk.top() == "omega"

My tests:
>>> stknew = stackADT() #new stack
>>> assert stknew.empty()
>>> stknew.top() #exception for top method
The stack is empty
>>> stknew.pop() #exception for pop method
The stack is empty
>>> stknew.push("haha")
>>> assert stknew.top() == "haha" #checking wheteher push and top are working
>>> stknew.pop()
>>> assert stknew.empty() #checking whether pop works

"""

from templatelistADT import listADT


class stackADT:
    def __init__(self):
        self.rep = listADT() #our representaion is listADT

    # precondtion
    # method "empty" doesn't take anything
    def empty(self): #O(1)
        return self.rep.empty()
    # postcondition
    # method empty returns True iff the stack is empty
    # false in other cases

    # precondtion
    # method "top" doesn't take anything
    def top(self): #O(1)
        if self.empty(): # precondtion
            print("The stack is empty")
        else:
            return self.rep.head()
    #postcondtion
    #the method top return the top elemnt of stachADT
    #or print "The stack is empty" if it is impossible

    # precondtion
    # method "push" take the object to add to the stack
    def push(self, x): #O(1)
        self.rep = listADT(x, self.rep)
    # postcondtion
    # method push mutates the stack to add x at the top

    # precondtion
    # method "pop" doesn't take anything
    def pop(self): #O(1)
        if self.empty(): # precondtion
            print("The stack is empty")
        else:
            self.rep = self.rep.rest()
    #posctondtion method pop delete the lest element from stack
    #or print "The stack is empty" if it is impossible

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print("doctests completed")
