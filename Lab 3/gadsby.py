"""
Lab 3: “I’ve heard about silent ‘e’, but ...
cs107 Introduction to Computer Science & Data Structures
Haverford College

Gadsby:a text w/out 'e'

Goal is to confirm/refute that the text does not contain the letter 'e' as claimed.

Text source file, see: https://en.wikisource.org/wiki/Gadsby

Python3 file I/O: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

"""

lineCount = 0

# loop over file object
#precondtions
#function receives a txt file
with open('GadsbyTrimmed.txt') as f:    # EXTEND CODE TO HUNT FOR 'e's
    checker = True
    for line in f:
        if "e" in line or "E" in line: #if we found "e" in the any line of the text document
            checker = False
            print('The letter "E(e)" was found in line', lineCount + 1, 'with', line.count('e'), 'occurrence(s)')
        lineCount += 1
if checker:
    ('The letter "e" was not found in the text')
#postconditions
#funtion is looking for letter "e"
#if the function find the letter it says the amount of occurrences of this
#letter in the line it was found
#and print 'The letter "e" was not found in the text' if there are no letter "e" in the text