"""
Lab 5: Binary Tree adjusted for ST problem
cs107 Introduction to Computer Science & Data Structures
Haverford College

Danylo Shudrenko

Binary Tree wich can be empty (I adjusted the __init__ condtructor)

Initial test cases:
>>> t1 = BT("A")
>>> assert t1.leaf()
>>> assert t1.root() == "A"

>>> t2 = BT("B", BT("C"), t1)
>>> assert not t2.leaf()
>>> assert t2.root() == "B"
>>> assert t2.right().root() == "A"
>>> assert t2.size() == 3

>>> print(t2)
'C''B''A'
>>> assert t2.postorder() == "'C''A''B'"

>>> t3 = BT("D", t2, t1)
>>> print(t3)
'C''B''A''D''A'
>>> assert t3.postorder() == "'C''A''B''A''D'"

My test case to check whether I can create empty tree:

>>> t = BT()
>>> t = BT(t, BT(1), BT(1))
>>> print(t.root())
None

"""

class node:
    def __init__(self, v, ltree, rtree):
        self.value = v
        self.ltree = ltree
        self.rtree = rtree
        
    def __repr__(self):
        return repr(self.value)

class BT:
    # constructor: a BT is either leaf/root-only, or
    #       a new top node (root) connected to two (sub)BTs
    #   primitive: BT(v)
    #   extending: BT(l, t, r)
    def __init__(self, top = None, left=None,  right=None): # I made top equals None to be able to create empty tree
        if left == None and right == None:          # primitive
            self.rep = node(top, None, None)
        else:                                       # extending
            self.rep = node(top, left, right)

    # axioms:
    #   leaf(BT(v)) === True
    #   leaf(BT(t, l, r)) === False
    def leaf(self):
        return self.rep.ltree == None and self.rep.rtree == None

    # axioms:
    #   root(BT(v)) === v
    #   root(BT(l, t, r)) === t
    def root(self):
        return self.rep.value

    # axioms:
    #   left(BT(v)) === undefined
    #   left(BT(l, t, r)) === l
    def left(self):
        assert (not self.leaf())
        return self.rep.ltree
    
    # axioms:
    #   right(BT(v)) === undefined
    #   right(BT(l, t, r)) === r
    def right(self):
        assert (not self.leaf())
        return self.rep.rtree
    
    # size function for binary trees;
    # should work on any representation
    # of a binary tree
    def size(self):
        if self.leaf():
            return 1
        else:
            return self.left().size() + self.right().size() + 1

    # inorder traversal for abstraction
    def __repr__(self):
        if self.leaf():
            return repr(self.root())
        else:                   # not a leaf, so
            return repr(self.left()) + repr(self.root()) + repr(self.right())

    def postorder(self):
        if self.leaf():
            return repr(self.root())
        else:                   # not a leaf, so
            return (self.left().postorder()) + (self.right().postorder()) + repr(self.root())
            

def _test():
    import doctest
    return doctest.testmod()

if __name__ == "__main__":
    if _test()[0] == 0:
        print("Congratulations! You have passed all the bintreelinks tests")



