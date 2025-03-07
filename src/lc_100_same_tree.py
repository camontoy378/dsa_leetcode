from make_tree import *

class SameTree():

    def __init__(self, array1, array2):
        self.array1  = array1
        self.array2  = array2

    def compare_roots(self, root1, root2, output):

        #Base case
        if root1 == root2 == None:
            return output
        if root1 == None or root2 == None:
            return False
        if root1.val != root2.val:
            return False
        
        if output == True:
            output = self.compare_roots(root1.left, root2.left, output)

        if output == True:
            output = self.compare_roots(root1.right, root2.right, output)

        return output
    
    ###########################################################################
    # LC Solution
    # Comments:
    # * Solution is more compact at the bottom 
    ###########################################################################
    def isSameTree(self, p, q):
        
        # p and q are both None
        if not p and not q:
            return True
        
        # one of p and q is None
        if not q or not p:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

    def solve(self):

        i = 0
        n = len(self.array1)
        m = len(self.array2)


        mytree_p = MakeTree(self.array1)
        mytree_q = MakeTree(self.array2)

        p = mytree_p.insert_level_order(i, n)
        q = mytree_q.insert_level_order(i, m)

        output_default_value = True

        return self.compare_roots(p, q, output_default_value)

        
