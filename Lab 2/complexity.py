""" Lab 2: complexity template

    adapted from Rajesh Kumar by John Dougherty
    cs107 Haverford College
    Danylo Shudrenko

    Complete the methods/algorithm from each of the following*:
        - bubble_sort OR selection_sort
        - merge_sort OR counting_sort OR quick_sort
        - linear_search AND is_sorted
        - binary_search_iterative (or another way if you choose ...)
    * you can (and should consider) implementing more [for full credit]

    The recorded data is saved into a dictionary "time_dict".  At the end this data is exported to
    a CSV file to be imported into a spreadsheet for more analysis.
"""
import copy
import random
import time
#import matplotlib.pyplot as plt
import math


class Complexity:
    # you can change this number to a lower number to test/debug/verify your implementations faster.
    # However, you should roll back to 100000 while testing in the end generating the final report.
    MAX = 1000000  # represent the largest number that can be generated
    def __init__(self, num_items):
        # Creating a list of random numbers between 0 to Complexity.MAX
        # Setting the seed to make sure that the same random list is generated every time with the same parameters
        random.seed(123)  # If you comment this line, you will get different list every time
        self.input_list = [int(random.random() * Complexity.MAX) for i in range(num_items)]  # List comprehension
        # Sorting a list using the built-in function of Python for list
        self.sys_sorted_list = sorted(self.input_list)  # Returns a sorted list without modifying the actual input_list
        # You can use the sys_sorted_list to check if your implementation is correct
        # Setting a list of random keys which will be used for testing the search algorithms. The items of the list may or may not be in the input_list
        random.seed(321)  # acomplishing the above by changing the seed value
        self.unsure_keys = [int(random.random() * Complexity.MAX) for i in range(num_items)]

        # Random sampling the list so we know the items of the sure_keys: means they are in the input_list for sure
        self.sure_keys = random.sample(self.input_list, k=num_items)

    # MAKE SURE YOU DO NOT MODIFY THE input_list in any of the functions; otherwise you will get into issues that may not be straight forward to detect/resolve
    # There are several ways to make copy of a list in Python. Google and find out. One of the best and fastest ways is duplicate = original[:]
    # Although its not the most efficient way, you should create a copy of the input list in every function for sanity as you know lists are mutable.
    def bubble_sort(self):
        #preconditon
        #function works for list of comparable and sortable elements
        sorted_list = copy.deepcopy(self.input_list) # make a deepcopy in order not to mutate list
        n = len(sorted_list)
        for i in range(n):
            checker = True #I plan to check if the list is sorted to reduce the time of sorting
            for j in range (n - i - 1): #with the buble sort the top elements are always sorted
                if (sorted_list[j + 1] < sorted_list[j]):
                    sorted_list[j],sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
                    checker = False
            if checker: #in case we didn't change the positions of any elements, the list was sorted initially
            #it meas we don't need to work on it anymore
                break
        return sorted_list
        #postcondition
        #function sort initial using bubble sort
        #return sorted list


    def selection_sort(self):
        # preconditon
        # function works for list of comparable and sortable elements
        sorted_list = copy.deepcopy(self.input_list) # make a deepcopy in order not to mutate list
        n = len(sorted_list)
        #I will not create two subaray, I will just separate my list into sorted part, and unsorted part
        end_of_sorted_part = 0 # this variable will show the end of the sorted part
        while end_of_sorted_part < n:
            mi = end_of_sorted_part #it would be the index of the smallest element in unsorted part
            for i in range(end_of_sorted_part, n):
                if (sorted_list[mi] > sorted_list[i]):
                    mi = i
            sorted_list[end_of_sorted_part], sorted_list[mi] = sorted_list[mi], sorted_list[end_of_sorted_part]
            #we extend our sorted subarray by adding minimum element
            end_of_sorted_part += 1
        return sorted_list
        # postcondition
        # function sort initial using bubble sort
        # return sorted list

    def merge_sort(self):
        # preconditon
        # function works for list of comparable and sortable elements
        sorted_list = copy.deepcopy(self.input_list)  # make a deepcopy in order not to mutate list
        def merging(arr1 : list, arr2: list)->list:
            res = [] #array, which we will get in result of merging
            n = len(arr1)
            j = 0
            for i in arr2:
                while j < n and arr1[j] < i: #if the element from the first array smaller we add it
                    #j < n needed to check if we already put all elements from first list
                    res.append(arr1[j])
                    j+=1
                res.append(i)
            return res
        #postconditions
        #function merges two sorted arrays in one sorted array

        def mergesort(arr:list)->list:
            n = len(arr)
            if n == 1: #if the length of array is equals 1 it means the array already sorted
                return arr
            x = n // 2 #the middle of the array
            arr1 = mergesort(arr[:x])
            arr2 = mergesort(arr[x:])
            return merging(arr1, arr2)
         #the function sort an array using mergesort
        return mergesort(sorted_list)
        #postconditions
        # the function sort an array using mergesort

    #description of the sorting from https://www.geeksforgeeks.org/counting-sort/
    def counting_sort(self):
        #precondtions function  works only for sorting integer numbers >= 0
        # function works for list of comparable and sortable elements
        arr = copy.deepcopy(self.input_list) # make a deepcopy in order not to mutate list
        ma = 0
        for i in range(len(arr)):
            if (arr[i] > arr[ma]):
                ma = i
        #I found the biggest element in array
        #now let's create our array for counting
        count = [0 for i in range(arr[ma] + 1)]
        for i in arr:
            count[i] += 1
        #counting of the amount of each element in array
        sorted_list = []
        for i in range(len(count)):
            for j in range(count[i]):
                sorted_list.append(i) #adding count[i] of element i to the sorted array
        return sorted_list
        #post condition
        #the function sort an array using countsort

    #description of the sorting from https://www.geeksforgeeks.org/quick-sort/
    def quick_sort(self):
        #precondtions
        # function works for list of comparable and sortable elements
        # I realize n algorithm where I choose a the first element as a pivot
        sorted_list = copy.deepcopy(self.input_list)  # make a deepcopy in order not to mutate list
        def quicksort(l:int , r:int):
            #preconditon
            #this void receives two indexes describing the part of the array(l- left, r - right side) and
            # sort this part using quick sort
            if r > l: #if not it means that function already sorted the previous part
                pivot =  l
                #this loop puts all smaller elements befor pivot and leaves bigger elements after pivot
                for i in range(l + 1, r):
                    if sorted_list[pivot] > sorted_list[i]:
                        sorted_list[pivot], sorted_list[pivot+1] = sorted_list[pivot +1], sorted_list[pivot]
                        sorted_list[pivot], sorted_list[i] = sorted_list[i], sorted_list[pivot]
                        pivot += 1
                quicksort(l, pivot - 1)
                quicksort(pivot + 1, r)
        quicksort(0, len(sorted_list))
        return sorted_list
        #function returns sorted array, sorting it recursively using quick sorting

    # Searching algorithms implementations
    def linear_search(self, input, key):
        #preconditons
        #function search for elemnt "key" in array
        arr = input
        for i in arr:
            if i == key:
                return True #if we found element, we can stop the search
        return False #if we didn't find anything before, it means that this elemt is not present in the array
    #postcondtion
    #searching algorithm working O(n) in the worse case if the elemnt is noit present

    def binary_search_iterative(self, input, key):
        #precondtion
        #works only for list of comparable elements and intially sorted list

        #Uncomment if you need to check whether the intial array is sorted
        #Please be mindful that it wil make a complexity of algorithm O(nlogn) instead od just O(logn)
        #if self.is_sorted(input) == False:
            #print("Binary_search_iterative works only for sorted array")
            #raise ValueError
        arr = input
        l = 0  #the left sife of the part of the array I am searching in
        r = len(arr) - 1  # the right part of the array I am searching in
        while (r - l > 1):
            mid = (r + l) // 2# the middle part of the part of the array
            if (arr[mid] == key): #in case we find our element
                return True
            elif arr[mid] > key:
                r = mid #moving the right side
            else:
                l = mid #moving the left side
        if arr[l]== key or arr[r] == key: # checking whether we found an element
            return True
        else:
            return False
    #postcondtions
    #searching algorithm working O(logn)


    # is_sorted
    def is_sorted(self, input):
        #precondition
        #works only for list of comparable elements
        assert isinstance(input, list)
        n = len(input)
        for i in range(n - 1):
            if input[i] > input[i - 1]: #if at least two elements are not in order it means that the array is not sorted
                return False
        return True #if we didn't find any misorder, it means that the array was sorted
        #postcondtion
        #function returns True, if the array is sorted, and False if it is not


    # The Analysis
    def get_time_taken_by_bubble_sort(self):
        # Compute and return the time taken by the function bubble_sort
        # checking the correctness of the implementation of bubble_sort
        sorted_list = self.bubble_sort()
        if sorted_list == self.sys_sorted_list:
            print("Bubble sort worked fine!")
        else:
            print("Opps!, Bubble sort has problems!")
        # Running bubble sort 20 times on the same input
        # Getting the average time that the function takes to execute for the same input because the following code to compute the time is not perfect

        times = []
        for i in range(20):
            start = time.time()
            self.bubble_sort()
            elapsed_time_lc = (time.time() - start)
            times.append(elapsed_time_lc)
        return sum(times) / len(times)  # returning the average time taken by the bubble sort to sort the same list

    def get_time_taken_by_selection_sort(self):
        # Compute and return the time taken by the function selection_sort
        # checking the correctness of the implementation of selection_sort
        sorted_list = self.selection_sort()
        if sorted_list == self.sys_sorted_list:
            print("Selection sort worked fine!")
        else:
            print("Opps!, Selection sort has problems!")
        # Running selection sort 20 times on the same input
        # Getting the average time that the function takes to execute for the same input because the following code to compute the time is not perfect

        times = []
        for i in range(20):
            start = time.time()
            self.selection_sort()
            elapsed_time_lc = (time.time() - start)
            times.append(elapsed_time_lc)
        return sum(times) / len(times)  # returning the average time taken by the selection sort to sort the same list


    def get_time_taken_by_merge_sort(self):
        # Compute and return the time taken by the function selection_sort
        # checking the correctness of the implementation of selection_sort
        sorted_list = self.merge_sort()
        if sorted_list == self.merge_sort():
            print("Merge sort worked fine!")
        else:
            print("Opps!, Merge sort has problems!")
        # Running merge sort 20 times on the same input
        # Getting the average time that the function takes to execute for the same input because the following code to compute the time is not perfect

        times = []
        for i in range(20):
            start = time.time()
            self.merge_sort()
            elapsed_time_lc = (time.time() - start)
            times.append(elapsed_time_lc)
        return sum(times) / len(times)  # returning the average time taken by the merge sort to sort the same list

    def get_time_taken_by_counting_sort(self):
        sorted_list = self.counting_sort()
        if sorted_list == self.counting_sort():
            print("Counting sort worked fine!")
        else:
            print("Opps!, Counting sort has problems!")
        # Running counting sort 20 times on the same input
        # Getting the average time that the function takes to execute for the same input because the following code to compute the time is not perfect

        times = []
        for i in range(20):
            start = time.time()
            self.counting_sort()
            elapsed_time_lc = (time.time() - start)
            times.append(elapsed_time_lc)
        return sum(times) / len(times)  # returning the average time taken by the counting sort to sort the same list

    def get_time_taken_by_quick_sort(self):
        sorted_list = self.quick_sort()
        if sorted_list == self.quick_sort():
            print("Quick sort worked fine!")
        else:
            print("Opps!, Quick sort has problems!")
        # Running quick sort 20 times on the same input
        # Getting the average time that the function takes to execute for the same input because the following code to compute the time is not perfect

        times = []
        for i in range(20):
            start = time.time()
            self.quick_sort()
            elapsed_time_lc = (time.time() - start)
            times.append(elapsed_time_lc)
        return sum(times) / len(times)  # returning the average time taken by the quick sort to sort the same list

    # Time taken by Searching algorithms
    def get_time_taken_by_linear_search(self):
        time1 = time.time()
        for i in self.sure_keys:
            self.linear_search(self.sys_sorted_list, i)
        time1 = time.time() - time1
        # (1) time to search for each element of sure_keys in the sys_sorted_list
        time2 = time.time()
        for i in self.unsure_keys:
            self.linear_search(self.sys_sorted_list, i)
        time2 = time.time() - time2
        # (2) time to search for each element of unsure_keys in the sys_sorted_list
        time3 = time.time()
        for i in self.sure_keys:
            self.linear_search(self.input_list, i)
        time3 = time.time() - time3
        # (3) time to search for each element of sure_keys in the input_list
        time4 = time.time()
        for i in self.unsure_keys:
            self.linear_search(self.input_list, i)
        time4 = time.time() - time4
        # (4) time to search for each element of unsure_keys in the input_list

        return (time1 + time2 + time3 + time4)/4.0
        #postcondition
        # return the average time taken by linear_search() function in conducting all the above searches

    def get_time_taken_by_binary_search(self):
        time1 = time.time()
        for i in self.sure_keys:
            self.binary_search_iterative(self.sys_sorted_list, i)
        time1 = time.time() - time1
        # (1)time to search for each element of sure_keys in the sys_sorted_list by calling the binary_search() function that you have implemented
        time2 = time.time()
        for i in self.unsure_keys:
            self.binary_search_iterative(self.sys_sorted_list, i)
        time2 = time.time() - time2
        # (2) time to search for each element of unsure_keys in the sys_sorted_list by calling the binary_search() function that you have implemented
        # (3) search for each element of sure_keys in the input_list by calling the binary_search() function that you have implemented
        #I feel I can't do it because binary search only works for sorted lists
        # (4) search for each element of unsure_keys in the input_list by calling the binary_search() function that you have implemented
        # I feel I can't do it because binary search only works for sorted lists

        return (time1 + time2)/2.0
        #postconditions
        #Return the average time taken by binary_search() function in conducting all above searches

    def get_time_taken_by_is_sorted(self):
        time1 = time.time()
        self.is_sorted(self.sys_sorted_list)
        time1 = time.time() - time1
        #(1) time to check whether the sys_sorted_list sorted calling is_sorted()
        time2 = time.time()
        self.is_sorted(self.input_list)
        time2=time.time() - time2
        # (2) time to check whether the input_list sorted calling is_sorted()
        return (time1 + time2)/2.0
        #postcondition
        #Return the average time taken by is_sorted()

    # The following dictionary shall be used in the main function
    dict_time_functions = {'Bubble': get_time_taken_by_bubble_sort,
                           'Selection': get_time_taken_by_selection_sort,
                           'Merge': get_time_taken_by_merge_sort,
                           'Quick': get_time_taken_by_quick_sort,
                           'Counting': get_time_taken_by_counting_sort,
                           'Quick': get_time_taken_by_quick_sort,
                           'LinearSearch': get_time_taken_by_linear_search,
                           'BinarySearch': get_time_taken_by_binary_search,
                           'IsSorted': get_time_taken_by_is_sorted}


# test cases via enumeration
if __name__ == "__main__":
    # You can change the following values for debugging purposes if you need to but revert them back befroe submission
    # Creating a list that stores number of items in the lists that is to be created for testing
    number_of_lists = 20 # you have to test for at least 20 lists, feel free to test for more list if your computer is fast enough
    num_items_list = [2 ** item for item in range(1, number_of_lists + 1)]  # Making use of list comprehension
    time_dict = dict()

    for num_items in num_items_list: # iterating over each list 
        CurrentRun = Complexity(num_items) # creating a temp object of the class Complexity 
        for name, func in CurrentRun.dict_time_functions.items(): # Running the required functions 
            if name not in time_dict: # for the first time
                time_dict[name] = [func(CurrentRun)]
            else: # for the rest 
                time_dict[name].append(func(CurrentRun))

    # You can print the dictionary to see how the dictionary looks like
    print(time_dict)

# save data to a CSV file, based on an example from
# https://www.tutorialspoint.com/How-to-save-a-Python-Dictionary-to-CSV-file
import csv
with open('complexity.csv', 'w') as f:
    for key in time_dict.keys():
        f.write("%s,%s\n"%(key,time_dict[key]))


"""
    # please comment the following lines if you dont want to see the plot during unit testing and debugging
    # plotting the times taken by each algorithms one by one on a graph
    for key in time_dict:
        plt.plot(time_dict[key], '-o')

    plt.title('Empirical Analysis of Computational Complexities')
    plt.legend(list(time_dict.keys()))
    plt.ylabel('Computation time')
    plt.xlabel('Number of elements')
    plt.xticks(range(number_of_lists), num_items_list)
    plt.show()

"""