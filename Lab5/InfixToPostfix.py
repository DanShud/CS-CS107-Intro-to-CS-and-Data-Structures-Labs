"""
Lab 5: Infix to Postfix
cs107 Introduction to Computer Science & Data Structures
Haverford College

Danylo Shudrenko

adapted from https://runestone.academy/runestone/books/published/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html

Intial test cases:
>>> assert infixToPostfix("A * B + C * ( D + E )") == 'A B * C D E + * +'
>>> assert infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )") == 'A B + C * D E - F G + * -'
>>> assert infixToPostfix("7") == '7'

My test cases:
>>> assert infixToPostfix("( 1 + X ) - X - X") == "1 X + X - X -" #numbers and characters
>>> assert infixToPostfix("A * B + C * D") == "A B * C D * +" #to check whether the order of operation is followd
>>> assert infixToPostfix("A / B") == "A B /" #to check that it is dividing in the right order
>>> assert infixToPostfix("") == "" #empty input

"""

from stack107 import *

def infixToPostfix(infixexpr: str)-> str:
    assert type(infixexpr) == type("a string")

    # a dictionary with precedence values
    prec = {}
    prec["*"] = prec["/"] = 3
    prec["+"] = prec["-"] = 2
    prec["("] = 1

    opStack = stack107()        # stack for scratch work (matching operands)
    postfixList = []            # holds the result
    tokenList = infixexpr.split()   # tokenize: now a list of tokens

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)      # put operand into the result
        elif token == '(':
            opStack.push(token)            # push(): wait for closing paren
        elif token == ')':
            topToken = opStack.top()       # top/pop(): match this paren
            opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)    # move token to result
                topToken = opStack.top()
                opStack.pop()
        else:
            while (not opStack.empty()) and (prec[opStack.top()] >= prec[token]):
                  postfixList.append(opStack.top())
                  opStack.pop()
            opStack.push(token)

    while not opStack.empty():
        postfixList.append(opStack.top())
        opStack.pop()
    return " ".join(postfixList)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
