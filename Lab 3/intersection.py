"""
Lab 3: Intersection
cs107 Introduction to Computer Science & Data Structures
Haverford College

Initial tests:
>>> in_common(['NJ', 'PA', 'CA', 'WA'],['WA', 'PA', 'GA', 'VA'])
['PA', 'WA']

>>> in_common(['NJ', 'PA', 'CA', 'WA'],['WV', 'DE', 'GA', 'VA'])
[]

Mine:
>>> in_common_loops(['NJ', 'PA', 'CA', 'WA'],['WA', 'PA', 'GA', 'VA']) #general case for common loops
['PA', 'WA']

>>> in_common_loops(['NJ', 'PA', 'CA', 'WA'],['WV', 'DE', 'GA', 'VA']) #when there are no common elements
[]

>>> in_common(['NJ', 'PA', 1, 'WA'],['WA', 12, 5, 1, 'PA', 'GA', 'VA']) #when the list of objects of different types
['PA', 1, 'WA']

>>> in_common_loops(['NJ', 'PA', 1, 'WA'],['WA', 12, 5, 1, 'PA', 'GA', 'VA']) #when the list of objects of different types
['PA', 1, 'WA']

>>> in_common(['NJ', 'PA', 'PA', 'CA', 'WA'],['WA', 'PA', 'GA', 'VA']) #when one list have two same elements
['PA', 'WA']

>>> in_common_loops(['NJ', 'PA', 'PA', 'CA', 'WA'],['WA', 'PA', 'GA', 'VA']) #when both lists have two same elements
['PA', 'WA']

>>> in_common(['NJ', 'PA', 'PA', 'CA', 'WA'],['WA', 'PA', 'PA', 'GA', 'VA']) #when both lists have two same elements
['PA', 'WA']

>>> in_common_loops(['NJ', 'PA', 'PA', 'CA', 'WA'],['WA', 'PA', 'PA', 'GA', 'VA']) #when both lists have two same elements
['PA', 'WA']

>>> in_common([],['WA', 'PA', 'PA', 'GA', 'VA']) #when one list is empty
[]

>>> in_common_loops([],['WA', 'PA', 'PA', 'GA', 'VA']) #when one list is empty
[]

>>> in_common([],[]) #when both lists are empty
[]

>>> in_common_loops([],[]) #when both lists are empty
[]
"""

def in_common_loops(a: list, b: list)-> list:
    #preconditions
    #function receives two lists
    assert isinstance(a, list) and isinstance(b, list)

    res = []
    for i in a:
        if i in b:
            if i not in res:
                res.append(i)
    return res
#poctondtions
#function return the list of the elements, which belong to both list.
#if there are several same elements in one of the intial list, there will be only one element
#in the final list. Final list does not have repetitive elements.
#function works using loops


def in_common_LC(a: list, b: list)-> list:
    # preconditions
    # function receives two lists
    assert isinstance(a, list) and isinstance(b, list)

    res = [x for x in a if x in b and x not in res]
    return res
#poctondtions
#function return the list of the elements, which belong to both list.
#if there are several same elements in one list, there will be only one element
#in the final list. Final list does not have repetitive elements.
#function works using list comprehension

in_common = in_common_LC   # set the function name here to execute/test

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests passed")

