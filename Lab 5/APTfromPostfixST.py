"""
Lab 5: Arithmetic Parse Tree From Postfix Expression (Using ST)
cs107 Introduction to Computer Science & Data Structures
Haverford College

Danylo Shudrenko

I didn't create traversal method on my own as it is already the part of binary tree
I used to build APT

>>> st = ST()
>>> st.set("A", 4)
>>> st.set("B", 8)
>>> st.set("C", 3)
>>> print(GenAPT('A B C * +'))
'A''+''B''*''C'

>>> print(GenAPT('A B C * +').postorder())
'A''B''C''*''+'

>>> print(EvalApt(GenAPT('A B C * +'), st))
28

>>> st.set('x', 4)
>>> st.set('y', 3)
>>> print(GenAPT('x                  y +')) #even if there is too much space between
'x''+''y'
>>> print(GenAPT('x                  y +').postorder())
'x''y''+'
>>> assert (EvalApt(GenAPT('x                  y +'), st)) == 7
>>> assert GenAPT('x                  y +').size() == 3


>>> st.set('aa', 10)
>>> st.set('bbb', 100)
>>> st.set('C', 2)
>>> print(GenAPT("aa bbb + C *")) #for two+ digits numbers
'aa''+''bbb''*''C'
>>> print(GenAPT("aa bbb + C *").postorder())
'aa''bbb''+''C''*'
>>> assert (EvalApt(GenAPT("aa bbb + C *"),st)) == 220
>>> assert GenAPT("aa bbb + C *").size() == 5



>>> st.set('p', 3)
>>> st.set('r', 2)
>>> assert (EvalApt(GenAPT('p r /'),st)) == 1.5 #not floor division


#>>> t = ST()
#>>> t.set("A", 0)
#>>> t.set("B", 1)
#>>> print(EvalApt(GenAPT('B A /'))))
#Error
#it would be an error because we cannot divide numbers by zero

#>>> print(EvalApt(GenAPT('1 + 1'))
#Error
#in case the input in the wrong format

#>>> print(EvalApt(GenAPT('')))
#Error
#input cannot be empty
"""
from stack107 import *
from BinTreeLinked import *
from SymbolTable import *

#input must be a string consisting of mathematical operators and substrings associated with ST table
#separted by spaces
#the string expression should follow the rule of postfix expression
def GenAPT(exp):
    assert type(exp) == type("a string")#precondtion
    st = stack107()  #creating the stack where I will put part of tree
    i = 0#index for the string charachers
    while i < len(exp):
        while i < len(exp) and exp[i] == " ": #if it is space index is shidted
            i += 1
        if i == len(exp): #if the end of the string is reached
            return st.top
        if exp[i] not in '+-*/' and exp[i] != " ":  # if it is not an operator
            j = i
            while exp[j] not in '+-*/' and exp[j] != " ":  # finding the end of substring
                j += 1
            st.push(BT(exp[i:j]))  #adding element in stack
            i = j # shifting the index
        else:
            val2 = st.top()
            st.pop()
            val1 = st.top()
            st.pop()
            st.push(BT(exp[i], val1, val2)) #taking top two elements and creating a tree
        i += 1 #shifting indes
    return st.top()
    #postcondtions
    #the function GenApt returns Arithmetic Parse Tree From Postfix Expression
    #it uses class binary tree to buils the tree

def EvalApt(tr, thetable):
    if tr.leaf(): #if we reached the leaf we don't need to do anythin
        return int(thetable.get(tr.root()))
    else:
        # recursively using math operators which are in the root of each subtree
        if tr.root() == '+':
            return EvalApt(tr.left(), thetable) + EvalApt(tr.right(), thetable)
        if tr.root() == '-':
            return EvalApt(tr.left(), thetable) - EvalApt(tr.right(), thetable)
        if tr.root() == '*':
            return EvalApt(tr.left(), thetable) * EvalApt(tr.right(), thetable)
        if tr.root() == '/':
            assert EvalApt(tr.right(), thetable) != 0 #preconditions
            return EvalApt(tr.left(), thetable) / EvalApt(tr.right(), thetable)
#postconditions
#EvalApt evaluates the parse tree using each element as a key for ST
#it cannot divide by zero


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
