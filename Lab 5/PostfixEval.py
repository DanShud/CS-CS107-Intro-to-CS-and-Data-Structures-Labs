"""
Lab 5: Infix to Postfix
cs107 Introduction to Computer Science & Data Structures
Haverford College

Danylo Shudrenko

test cases from
https://www.free-online-calculator-use.com/postfix-evaluator.html
>>> assert PostfixEval('4 8 3 * +') == 28
>>> assert PostfixEval('4 8 + 3 *') == 36
>>> assert PostfixEval('7 8 + 3 2 + /') == 3
>>> assert PostfixEval('4') == 4

My test cases:

>>> assert PostfixEval('4                  3 +') == 7 #even if there is too much space between
>>> assert PostfixEval('3 2 /') == 1.5 #not floor division
>>> assert PostfixEval("10 100 + 2 *") == 220 #for two+ digits numbers
>>> assert PostfixEval(" 1 1 /") == 1 #if there is space in front of the expression
>>> assert PostfixEval("1 1 /   ") == 1 #if there is space in the end of the expression



#>>> print(PostfixEval('3 0 /'))
#Error
#it would be an error because we cannot divide numbers by zero

#>>> print(PostfixEval('1 + 1')
#Error
#in case the input in the wrong format

#>>> print(PostfixEval(''))
#Error
#input cannot be empty
"""

from stack107 import *

#precondtions the function takes 3 strings
#the first string "operator" must consist only
#of one character, which would be "+","-","*", or "/"
#the sring "op1" and "op2" should consist only of numbers
#"op2" cannot equals "0"
def calculate(operator:str, op1:str, op2:str) :
    #precondtions
    assert operator in '+-*/'
    for i in op1:
        i.isnumeric()
    for i in op2:
        i.isnumeric()


    op1 = float(op1) #converting to the number
    op2 = float(op2) #converting to the number
    if operator == "+":
        return op1 + op2
    if operator == "-":
        return op1 - op2
    if operator == "*":
        return op1 * op2
    if operator == "/":
        assert op2 != 0 #precondtions
        return op1 / op2
#fucntion calcualte calculate the expression
#knowing the operator from the "operator" input
#and two operands - "op1", "op2"


#preconditon
#input must be a string consisting of mathematical operators and numbers
#separted by spaces
#the string expression should follow the rule of postfix expression
def PostfixEval(exp: str):
    assert type(exp) == type("a string") # preconditons
    elements = stack107() #stack where I put the elemets we are working with
    i = 0 #index of the string
    while(i < len(exp)):
        while i < len(exp) and (exp[i] == ' '): #if the element is a space we are just ignoring it
            i += 1
        if i == len(exp): #if the whole string is already checked
            return float(elements.top())
        if exp[i].isnumeric(): #if it is a number
            j = i #additional index to get all digits of the number
            while j < len(exp) and exp[j].isnumeric(): #while the next character is another digit of the number
                j += 1
            elements.push(exp[i:j]) # adding the nubmber to elements I am working with
            i = j # moving the index
        else: #if it is operation
            val2 = elements.top()
            elements.pop()
            val1 = elements.top()
            elements.pop() #we are getting first two operandands
            elements.push(str(calculate(exp[i], val1, val2))) #adding the result of operation on top two operandans
            i += 1 #shifting index

    return float(elements.top()) #in the stack there will be only one element left after all the operations and it
    #would be the result of expression
    #postcondtions
    #Function PostfixEval calculate the value of postfix espression

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
