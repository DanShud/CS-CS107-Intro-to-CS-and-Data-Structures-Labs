"""
Lab 5: Symbol Table (using Binary Search Tree)
cs107 Introduction to Computer Science & Data Structures
Haverford College

Danylo Shudrenko

>>> t = ST()       # empty symbol table
>>> t.set('x', 5)
>>> t.set('y', 3)
>>> t.set('z', t.get('x'))
>>> assert t.get('z') == t.get('x')
>>> assert not t.get('z') == t.get('y')
>>> print(t)
None['x', 5]None['y', 3]['z', 5]

>>> a = ST()
>>> a.set('xxx','20') #setting non one digit strings
>>> a.set(1, 5) # setting number as a key
>>> a.set("", 2) #setting empty string as a key
>>> print(a.get("1")) #checing the function get
5
>>> a.get("abc") #if we don't have the element in ST
It is a silly key. The Symbol Table doesn't contain it
>>> assert a.get(1) + a.get("") == 7 # checking the function get
>>> print(a)  #checking the representation
['', 2]['1', 5]None['xxx', '20']None

>>> a.set('xxx', 5) #reseting the value in symbol table
>>> print(a.get('xxx')) #checking the new representation
5
>>> print(a)  #checking the new representation
['', 2]['1', 5]None['xxx', 5]None
"""

from BinTreeLinkedforST import *


class ST:  # symbol table
    def __init__(self):  # construct an empty ST
        self.rep = BT()

    # precondtion
    # function set gets where and whet for Symbol Table to add it to the tree
    def set(self, where, what):
        nod = [str(where), what]  # creates a node of where and what
        temp = ST()
        temp.rep = self.rep  # creating a temporary ST not to mutate self by mistake

        # preconditon
        # function gets the tree and the node it needs to add
        def helper(tree, node):
            if tree == None or tree.root() == None:  # if the tree is empty we are creating the root
                return BT(node)
            if tree.leaf():  # if it is the leaf
                if (node[0] > tree.root()[0]):  # if the node[0](where) is bigger than root it would be added
                    # to the right side of the tree
                    return BT(tree.root(), None, BT(node))
                else:  # if smaller - to the left
                    return BT(tree.root(), BT(node), None)
            elif tree.left() == None and node[0] < tree.root()[0]:  # if tree doesn't have left subtree
                # and node[0](where) is smaller than root it would be added to the left
                return BT(tree.root(), BT(node), tree.right())
            elif tree.right() == None and node[0] > tree.root()[0]:  # if the tree doesn't have the
                # right subtree and node[0](where) is bigger than root it would be added to the right
                return BT(tree.root(), tree.left(), BT(node))
            elif tree.root()[0] == node[0]:  # if we found the same element we substitute it with new node
                return BT(node, tree.left(), tree.right())
            else:
                if tree.root()[0] < node[0]:  # in all other cases the function just recursivly go either in left or in right side
                    # in the right if node[0](where) is bigger than root
                    return BT(tree.root(), tree.left(), helper(tree.right(), node))
                else:
                    # in the left if node[0](where) is smaller than root
                    return BT(tree.root(), helper(tree.left(), node), tree.right())
            # postcondtions
            # function helper add a node into the tree
            # it organizes it as UNBALANCED binary search tree, by comparing the node[0]

        self.rep = helper(temp.rep, nod)  # mutating the self

    # postcondtions
    # method set add a node into the tree where node[0] is "where", and node[1] is "what"
    # it organizes it as UNBALANCED binary search tree, by comparing the node[0](where)

    # precondition
    # function get ST represented as unbalanced binary search tree
    # and the element which is searched
    def get(self, where):  # getter (accessor)
        temp = ST()
        temp.rep = self.rep  # creating a copy not to mutate the self
        where = str(where)

        # precondition
        # method get unbalanced binary search tree
        # and the element which is searched
        def helper(tree, where):
            if tree == None or (tree.leaf() and tree.root()[0] != where):  # if the value is not in ST
                print("It is a silly key. The Symbol Table doesn't contain it")
                return
            if tree.root()[0] == where:  # if we found the value
                return tree.root()[1]
            if tree.root()[0] < where: #if the value is bigger
                #go in the right part of the tree
                return helper(tree.right(), where)
            else:
                #if smaller in the left
                return helper(tree.left(), where)
        #function helper recusively is searching for the element "where" in tree
        # and then return the value this key is reffering to
        return helper(temp.rep, where)
        #method get the value associated with key "where" from ST

    def __str__(self):  # abstract to text
        return str(self.rep)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
