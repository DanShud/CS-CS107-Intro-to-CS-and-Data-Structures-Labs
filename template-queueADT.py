"""
Lab 4: stackADT
cs107 Introduction to Computer Science & Data Structures
Haverford College
Danylo Shudrenko

Initial test cases:
>>> que = queueADT()
>>> assert que.empty()
>>> que.enqueue("chi")
>>> assert not que.empty()
>>> assert que.front() == "chi"
>>> que.dequeue()
>>> assert que.empty()

My tests:
>>> quenew = queueADT() #empty queue
>>> assert quenew.empty() #checking empty method
>>> quenew.front() #exception for front method
The queue is empty
>>> quenew.dequeue() #exception for dequeue method
The queue is empty
>>> quenew.enqueue("a")
>>> assert quenew.front() == "a" # checking front method
>>> quenew.dequeue()
>>> assert quenew.empty() #checking dequeu method


"""
import copy

from templatestackADT import stackADT

class queueADT:
    def __init__(self):
        self.rep = stackADT() #the representation of abstraction is stack

    # precondtion
    # method "empty" doesn't take anything
    def empty(self): #O(1)
        return self.rep.empty()
    #postcondition
    #method empty returns True iff the queue is empty
    #false in other cases

    #precondtion
    # method "front" doesn't take anything
    def front(self): #O(n), n - length of queue
        if self.empty(): #precondtion
            print("The queue is empty")
        else:
            fr = 0 #the front element we will get
            temp = queueADT()
            temp.rep = copy.deepcopy(self.rep) #creating temporary copy not to mutate queue
            while not temp.rep.empty(): #deleting al ellements from stack representation to get to the last element -
            #front of the queue abstraction
                fr = temp.rep.top()
                temp.rep.pop()
            return fr
    #postcondtion
    # returns the value at the front of the queue
    # or print "The queue is empty" if it is impossible

    #precondtion
    # method "enqueue" take the object to add to the queue
    def enqueue(self, x): #O(1)
        self.rep.push(x)
    # postcondtion
    # mutates the queue to add x at the back

    # precondtion
    # method "dequeue" doesn't take anything
    def dequeue(self): #O(n), n - length of queue
        if self.empty(): #precondtion
            print("The queue is empty")
        else:
            temp = queueADT()
            temp.rep = stackADT() #creating a temporary queue not to mutate intial queue
            #precondtion
            #function helper receive an initial queue to recursivly delete elements
            def helper (var: queueADT())-> queueADT():
                x = var.rep.top() #the top value
                var.rep.pop() #deleting one element
                if var.rep.empty() == False:#if our stack is not empty that it means
                    #that we didn't delete the first element, so we should put the element
                    #we deleted in final queu
                    temp.rep.push(x)
                    helper(var)
            #postcondtion
            #function helper recurcively adding elemnts to temporary queue
            #except for the first element
            helper(self)
            self.rep = temp.rep
    # postcondtion
    # method "dequeue" mutates the queue to remove x from the front
    # or print "The queue is empty" if it is impossible

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print("doctests completed")
