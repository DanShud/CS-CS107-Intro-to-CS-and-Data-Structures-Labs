"""
Binary Tree (non-empty)

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
>>> assert 'A' < 'B'
>>> assert t2.max() == 'C'
>>> assert t3.max() == 'D'

"""

class BT:
    # constructor: a BT is either leaf/root-only, or
    #       a new top node (root) connected to two (sub)BTs
    #   primitive: BT(v)
    #   extending: BT(l, t, r)
    def __init__(self, top, left=None,  right=None):
        if left == None and right == None:          # primitive
            self.rep = [top, None, None]
        else:                                       # extending
            self.rep = [top, left, right]

    # axioms:
    #   leaf(BT(v)) === True
    #   leaf(BT(t, l, r)) === False
    def leaf(self):
        return self.rep[1] == None and self.rep[2] == None

    # axioms:
    #   root(BT(v)) === v
    #   root(BT(l, t, r)) === t
    def root(self):
        return self.rep[0]

    # axioms:
    #   left(BT(v)) === undefined
    #   left(BT(l, t, r)) === l
    def left(self):
        assert (not self.leaf())
        return self.rep[1]
    
    # axioms:
    #   right(BT(v)) === undefined
    #   right(BT(l, t, r)) === r
    def right(self):
        assert (not self.leaf())
        return self.rep[2]
    
    # size function for binary trees;
    # should work on any representation
    # of a binary tree
    def size(self):
        if self.leaf():
            return 1
        else:
            return self.left().size() + self.right().size() + 1

    def max(self):      # returns the largest value in the tree
        
        def max3(x, y, z):      # max of three items
            l = [x, y, z]       # make a temp list ...
            ll = sorted(l)      # ... sort that list ...
            return ll[-1]   # ... last element must be the largest value
        
        if self.leaf():
            return self.root()
        else:
            return max3(self.left().max(), self.right().max(), self.root())
        
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
        print("Congratulations! You have passed all the doctests")



