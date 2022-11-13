"""
Lab 3: Palindromes
cs107 Introduction to Computer Science & Data Structures
Haverford College

In this problem I consider as palindrom is
the symbols order, which may be read the same way in either forward or reverse direction,
not taking into account all other non-alphabetic characters
Also, I will consider smal and bigg letters as the same letter
For example "a" == "A"
This definition is based on thes cases from http://www.palindromelist.net/

Initial test cases:
>>> assert palindrome("mom")
>>> assert not palindrome("mother")

Mine test cases:

>>> assert palindrome("!mo!m") # test with non-alphabetic characters inside of the palindrome

>>> assert palindrome("!mo  m") # test with spaces inside of the palindrome

>>> assert palindrome("!m!o  m") # test with spaces and non alpabetic characters inside of the palindrome

>>> assert palindrome("!a  2134") #just one alphabetic character

>>> assert palindrome("")

#is palindrome since there are not any alphabetic characters, so the empty line may be read
#the same way in either forward or reverse direction

>>> assert palindrome("!@ *(&)   )^72  05182   357198 57")

#is palindrome since there are not any alphabetic characters, so the empty line may be read
#the same way in either forward or reverse direction

>>> assert not palindrome("A car, a man,ddmaraca.") #regular case when it is not a palindrome

>>> assert not palindrome("ba") #regular case when it is not a palindrome

#Test with regular sentences(some non-alphabetic symbols may persist) test cases from http://www.palindromelist.net/

>>> assert palindrome("Are Mac ‘n’ Oliver ever evil on camera?")

>>> assert palindrome("A car, a man, a maraca.")

>>> assert palindrome("Are we not pure? “No sir!” Panama’s moody Noriega brags. “It is garbage!” Irony dooms a man; a prisoner up to new era.")
"""

def palindrome(s: str)-> bool:
    #precondtions
    #I assume that the function consider small and big letters as the same letter
    #for example "a" == "A"
    #Also, I will get rid of all non-alphabetic based on the test cases of palindroms from:
    #http://www.palindromelist.net/

    s = s.lower() #making all letters small letters
    l = 0 #pointer on the left side of string
    r = len(s) - 1 #pointer on the right side of string
    while l < r:
        while l < r and s[l].isalpha() == False : #finding the first alphabetic symbol on the left side
            l +=1
        if (l == r): #it means there are no more the first alphabetic symbol on diapasone between l and r
            break
        while l < r and s[r].isalpha() == False: #finding the the first alphabetic symbol on the right side
            r -= 1
        if (s[l] != s[r]):
            return False #if we find mismatch it means that the string is not a palindrome
        l += 1 #moving pointer
        r -= 1 #moving pointer

    return True # if we didn't find any mismatch it means that the string is a palindrome
    #postconditions
    #function return True if the input string is a palindrome(palindrome, in this problem, is
    #the symbols order, which may be read the same way in either forward or reverse direction,
    #not taking into account all other non-alphabetic characters)
    #and return False if the input is not a palindrome

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests passed")
