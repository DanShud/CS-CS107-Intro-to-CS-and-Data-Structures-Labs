"""
Lab 5: Symbol Table (general)
cs107 Introduction to Computer Science & Data Structures
Haverford College

Danylo Shudrenko

Intial test cases:
>>> t = ST()       # empty symbol table
>>> t.set('x', 5)
>>> t.set('y', 3)
>>> t.set('z', t.get('x'))
>>> assert t.get('z') == t.get('x')
>>> assert not t.get('z') == t.get('y')
>>> print(t)
{'x': 5, 'y': 3, 'z': 5}

My test cases:
>>> a = ST()
>>> a.set('xxx','20') #setting non one digit strings
>>> a.set(1, 5) # setting number as a key
>>> a.set("", 2) #setting empty string as a key
>>> assert a.get(1) + a.get("") == 7 # checking the function get
>>> a.get("abc") #if we don't have the element in ST
It is a silly key. The Symbol Table doesn't contain it
>>> print(a)  #checking the representation
{'xxx': '20', 1: 5, '': 2}
>>> a.set('xxx', 5) #reseting the value in symbol table
>>> assert a.get('xxx') == a.get(1)
>>> print(a)  #checking the new representation
{'xxx': 5, 1: 5, '': 2}
"""


class ST:                   # symbol table
    def __init__(self):             # construct an empty ST
        self.rep = {}

    def set(self, where, what):     # setter (mutator)
        self.rep[where] = what

    def get(self, where):           # getter (accessor)
        if where in self.rep: #preconditions
            return self.rep[where]
        else:
            print("It is a silly key. The Symbol Table doesn't contain it")

    def __str__(self):              # abstract to text
        return str(self.rep)
#postcondtions
#class ST is a class which representaion is dictionary
#and it works analogicaly as dineery, but with different methods

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
