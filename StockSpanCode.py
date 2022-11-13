"""
Lab 4: ListADT
cs107 Introduction to Computer Science & Data Structures
Haverford College
Danylo Shudrenko

Initial test cases:

>>> print(span([10, 4, 5, 90, 120, 80, 121]))
[1, 1, 2, 4, 5, 1, 7]

>>> print(span([88]))
[1]

#>>> print(span(["error"]))    # or empty list, different assertion tripped
Exception raised: ...

My test cases:
>>> print(span([100, 80, 60, 70, 60, 75, 85]))
[1, 1, 1, 2, 1, 4, 6]

>>> print(span([5,4, 2, 1]))
[1, 1, 1, 1]

>>> print(span([3, 1, 2]))
[1, 1, 2]
"""

from templatestackADT import stackADT

def intListPredicate(lst:list)-> bool:      # linear complexity O(len(lst))
    if lst == []:
        return True
    else:
        head = lst[0]
        rest = lst[1:]
        return (type(head) == type(8)) and intListPredicate(rest)

def spanNaive(prices: list) -> list:             # quadratic complexity O(len(prices)^2)
    assert len(prices) > 0
    assert intListPredicate(prices)
    
    spans = [None] * len(prices)   # generate a list to hold spans
    assert len(spans) == len(prices)
    spans[0] = 1                   # by definition, initial span is always 1

    for d in range(1, len(prices)):     # each of the remaining spans
        spans[d] = 1
        i = d - 1               # start at the previous day's price
        while (i >= 0) and (prices[d] >= prices[i]):
            spans[d] += 1           # increment the span
            i -= 1                  # move to the previous day's price

    return spans

def spanWstacks(prices: list) -> list: # better complexity O(N) (Please see the explanation in postcondition
    #precondtion
    assert len(prices) > 0
    assert intListPredicate(prices)

    spans = [None] * len(prices)   # generate a list to hold spans
    st = stackADT() #create the stack where we would add the "local" maximum
    for i in range(len(prices)):
        while not st.empty():#if stack is empty it means that all elements before were smaller than our element
            if prices[i] < prices[st.top()]: #if previous "local" maximum on range of the span of the element
                # in stack is bigger than element we are looking now
                break
            st.pop()
        if st.empty(): #it means that the current element is bigger than all previous "local maximum"
            spans[i] = i + 1
        else:
            spans[i] = i - st.top() #we find a previous "local maximum" and popped all smaller elements
            #which means that all elements on from there to the elemnt will be smaller
        st.push(i) #adding the index of the element as it becomes new "local maximum"
    return spans
    #postcondtion
    # stock span: determine the list of integer values for a list of stock prices p
    # to depict the span (s) at a given day (d), where
    # s[d] := number of consecutive prior to d where p[i] <= p[d] for i < d
    #it works for 2n because in worse case the function add each element once and can pop each element only once
    #therfore complexity linear -> O(n)

span = spanWstacks           # set to spanWstacks to test your code


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
