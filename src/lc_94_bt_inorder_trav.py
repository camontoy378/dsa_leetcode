class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val    = val
        self.left   = left
        self.right  = right

class BinTreeInorderTrav():

    def __init__(self, bt_array):
        self.bt_array   = bt_array       

    def inorderTraversal_rec(self, root):

        if root == None:
            return []

        output = []
    
        output.extend(self.inorderTraversal_rec(root.left))

        output.append(root.val)

        output.extend(self.inorderTraversal_rec(root.right))
        
        return output

        

    def solve(self):

        head = None

        self.create_bt(head, 0)

        return True
    
