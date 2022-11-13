"""
CS 107 Haverford College
Dan Shudrenko
Anograms Assesment

Test cases:

>>> assert anograms("angel", "glean")
>>> assert anograms("cat", "act")
>>> assert not anograms("catt", "aact")
"""


def anograms(s1:str, s2:str)-> bool:
    checker = {}
    for a in s1:
        if a in checker:
            checker[a] += 1
        else:
            checker[a] = 1
    for a in s1:
        if a in checker:
            checker[a] -= 1
        else:
            checker[a] = -1
    for i in checker:
        if checker[i] != 0:
            return False
    return True
#postconditions
#function return True if two intial strings are anograms,
#and return False in all other cases


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")


"""
How did I think about this assement? 
First, I tried to think what makes two string anograms. Based on the definition I 
understood that they are two string which have the same set of characters.
Then I started to think on how I can check it. First of all, I've could created
a list of same characters in both string, but its complexity would be O(n^2)
I decided that it could've be more optimal if I use hashing(it is kinda similiar to 
counting sort) Then I checked it using test cases

I feel that the way I code didn't change mutch, but previously I didn't use any preconditions
and postcondtions, and didn't organize my code before, because I didn't need it in competitive programming
Unfortunately, I didn't have enough time to do it completly because of time limit 
"""