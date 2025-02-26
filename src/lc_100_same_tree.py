

class TreeNode():

    def __init__(self, val=0, left=None, right=None):
        self.val    = val
        self.left   = left
        self.right  = right


class SameTree():

    def __init__(self, array1, array2):
        self.array1  = array1
        self.array2  = array2
    
    def create_tree_from_array(self, array):

        root : TreeNode = None
        #insert_left = True

        if len(array) == 0:
            return
        
        for item in array:
            root = self.insert(root, item)

        return root
        #head = TreeNode(val=array[0])

        #if len(array) == 1:
        #    return
        
        #for item in array:
        #    pass
        
    #Only works for 3 values max.
    def insert(self, ptr, value):

        if ptr == None:
            if value == None:
                return
            else:
                ptr = TreeNode(value)
        elif ptr.left == None:
            ptr.left = TreeNode(value)
        else:
            ptr.right = TreeNode(value)
        
        return ptr

    def solve(self):

        p = self.create_tree_from_array(self.array1)
        q = self.create_tree_from_array(self.array2)


        #Compare root
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        #Compare left
        if p.left and q.left == None:
            return False
        if p.left.val != q.left.val:
            return False
        #Compare right
        if p.right.val != q.right.val:
            return False

        return True
