"""
Lab 5: Arithmetic Parse Tree From Postfix Expression (general)
cs107 Introduction to Computer Science & Data Structures
Haverford College

Danylo Shudrenko

I didn't create traversal method on my own as it is already the part of binary tree
I used to build APT

Intial test cases:

>>> print(GenAPT('4 8 3 * +'))
'4''+''8''*''3'

>>> print(GenAPT('4 8 3 * +').postorder())
'4''8''3''*''+'

My test cases:

>>> print(EvalApt(GenAPT('4 8 3 * +')))
28

>>> print(GenAPT('4                  3 +')) #even if there is too much space between
'4''+''3'
>>> print(GenAPT('4                  3 +').postorder())
'4''3''+'
>>> assert (EvalApt(GenAPT('4                  3 +'))) == 7
>>> assert GenAPT('4                  3 +').size() == 3



>>> print(GenAPT("10 100 + 2 *")) #for two+ digits numbers
'10''+''100''*''2'
>>> print(GenAPT("10 100 + 2 *").postorder())
'10''100''+''2''*'
>>> assert (EvalApt(GenAPT("10 100 + 2 *"))) == 220
>>> assert GenAPT("10 100 + 2 *").size() == 5

>>> print(GenAPT(" 1 1 /")) #if there is space in front of the expression
'1''/''1'
>>> print(GenAPT(" 1 1 /").postorder())
'1''1''/'
>>> assert (EvalApt(GenAPT(" 1 1 /"))) == 1
>>> assert GenAPT(" 1 1 /").size() == 3

>>> print(GenAPT("1 1 /   ")) #if there is space in the end of the expression
'1''/''1'
>>> print(GenAPT("1 1 /   ").postorder())
'1''1''/'
>>> assert (EvalApt(GenAPT("1 1 /   "))) == 1


>>> assert (EvalApt(GenAPT('3 2 /'))) == 1.5 #not floor division

#>>> print(EvalApt(GenAPT('3 0 /'))))
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

#input must be a string consisting of mathematical operators and numbers
#separted by spaces
#the string expression should follow the rule of postfix expression
def GenAPT(exp):
    assert type(exp) == type("a string") #precondtion
    st = stack107() #creating the stack where I will put part of tree
    i = 0 #index for the string charachers
    while i < len(exp):
        while i < len(exp) and exp[i] == " ": #if it is space index is shidted
            i += 1
        if i == len(exp): #if the end of the string is reached
            return st.top()
        if exp[i].isnumeric(): #if it is a numeric character
            j = i  # additional index to get all digits of the number
            while j < len(exp) and exp[j].isnumeric():  # while the next character is another digit of the number
                j += 1
            st.push(BT(exp[i:j]))  # adding the nubmber to elements I am working with
            i = j  # moving the index
        else:
            val2 = st.top()
            st.pop()
            val1 = st.top()
            st.pop() #taking top two elements and creating a tree
            st.push(BT(exp[i], val1, val2))
        i += 1 # shifting index

    return st.top()
#postcondtion
#the function GenApt returns Arithmetic Parse Tree From Postfix Expression
#it uses class binary tree to buils the tree


#precondtions
#function get a Arithmetic Parse Tree From Postfix Expression
def EvalApt(tr):
    if tr.leaf(): #if we reached the leaf we don't need to do anythin
        return int(tr.root())
    else:
        #recursively using math operators which are in the root of each subtree
        if tr.root() == '+':
            return EvalApt(tr.left()) + EvalApt(tr.right())
        if tr.root() == '-':
            return EvalApt(tr.left()) - EvalApt(tr.right())
        if tr.root() == '*':
            return EvalApt(tr.left()) * EvalApt(tr.right())
        if tr.root() == '/':
            #precondtions
            assert EvalApt(tr.right()) != 0
            return EvalApt(tr.left()) / EvalApt(tr.right())
#postconditions
#EvalApt evaluates the parse tree
#it cannot divide by zero

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
