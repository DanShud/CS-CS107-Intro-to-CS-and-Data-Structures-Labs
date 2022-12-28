"""
Lab 6: Student DemoGraphics
cs107
Haverford College

Danylo Shudrenko

!!!!!!!!!!!!!OBSERVATIONS!!!!!!:
This graph is an undirected graph. Also, it is not weighted, and none of nodes has self-loop.
Additionaly, by the way we construct graph, there will not be a situation when two courses,
or two students are connected by edge.



graph ADT
implemented using a dictionary, where each value is a list

John Dougherty
Haverford College

# unit tests for the graph class

>>> students = graph()  # empty graph
>>> print(students)
{}
>>> students.add_node('alice')
>>> students.add_node('bob')
>>> students.add_node('carol')
>>> print(students)
{'alice': [], 'bob': [], 'carol': []}
>>> assert students.list_nodes() == ['alice', 'bob', 'carol']
>>> students.link('alice', 'carol')
>>> assert students.connected('alice', 'carol')
>>> print(students)
{'alice': ['carol'], 'bob': [], 'carol': ['alice']}
>>> students.add_node('dave')
>>> students.add_node('eddie')
>>> students.add_node('fran')
>>> students.add_node('greg')
>>> print(students)
{'alice': ['carol'], 'bob': [], 'carol': ['alice'], 'dave': [], 'eddie': [], 'fran': [], 'greg': []}
>>> assert not students.connected('alice', 'eddie')
>>> students.link('alice','eddie')
>>> assert students.connected('alice', 'eddie')
>>> assert students.neighbor_count('alice') == 2
>>> assert students.neighbor_count('greg') == 0
>>> assert students.list_neighbors('alice') == ['carol', 'eddie']
>>> assert students.list_neighbors('greg') == []
>>> assert students.size() == 7
>>> students.link('eddie', 'carol')
>>> assert students.connected('eddie', 'carol')
>>> assert students.connected('alice', 'carol')
>>> assert students.connected('carol', 'alice')
>>> assert not students.connected('bob', 'carol')
>>> assert not students.connected('bob', 'eddie')
>>> assert students.list_neighbors('eddie') == ['alice', 'carol']


"""

class graph:
    def __init__(self):     # construct an empty graph ...
        self.rep = {}       # .. as an empty adjacency list represented
                            # as an empty dictionary

    def __str__(self):      #!ACCESSOR! for printing the contents of the graph
        return str(self.rep)

    def add_node(self, node):   #!MUTATOR! add a new node to the graph, no links yet
        if not node in self.rep:
            self.rep[node] = [] # add this node, initially no links (i.e., an island)

    def link(self, x, y):       #!MUTATOR! link two nodes already in the graph
        assert x in self.rep    # x found in graph
        assert y in self.rep    # y found in graph
        assert x != y           # no self links
        self.rep[x].append(y)   # link from x to y, and ...
        self.rep[y].append(x)   # ... link from y to x (undirected graph)
 
    def connected(self, x, y):  #!ACCESSOR! returns True iff x and y are linked
        return (y in self.rep[x]) and (x in self.rep[y])

    def neighbor_count(self, node): #!ACCESSOR! returns the number of adjacent nodes
        assert node in self.rep     # node  found in graph
        return len(self.rep[node])

    def list_neighbors(self, node): #!ACCESSOR! returns all neighbors of a node
        assert node in self.rep     # node  found in graph
        return self.rep[node]

    def list_nodes(self):           #!ACCESSOR! returns a list containing graph nodes
        return list(self.rep)

    def size(self):             #!ACCESSOR! returns the number of nodes in the graph
        return len(self.rep)

    #precondition
    #method common_courses takes two values studentA, and studentB
    #both of those value have to be nodes in the graph
    def common_courses(self, studentA, studentB): #!ACCESSOR!
        res = [] #setting up the list of the result
        for courseA in self.rep[studentA]: #for each course of studentA
            for courseB in self.rep[studentB]: #the method compare it with each course of studentB
                if courseA == courseB: #if courses are identical
                    res.append(courseA)  #the course is added to the list of result
        return res
    #precondtion
    #methon common_courses return the list of common courses of two students

    #precondtion
    #method who_is_taking accept the variable "course", which has to be node in the graph
    def who_is_taking(self, course): #!ACCESSOR!
        return self.list_neighbors(course) #since the courses are connected only with students
        #the list of neighbours is all students who are taking the course
    #postcondtion
    #method who_is_taking return the list of student who are taking the course from input




if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("graph tests completed")
