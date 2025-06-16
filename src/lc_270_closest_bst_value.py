from make_tree import MakeTree

class ClosestBSTValue():

    def __init__(self, root, target):
        self.root   = root
        self.target = target

    def bst_value(self, root):

        if root == None:
            return None
        
        closest_target      = root.val
        closest_value_diff  = abs(root.val - self.target)
        
        if self.bst_value(root.left) != None:
            left_value          = self.bst_value(root.left)
            left_value_diff     = abs(left_value - self.target)

            if left_value_diff < closest_value_diff:
                closest_target      = left_value
                closest_value_diff  = left_value_diff

            
        if self.bst_value(root.right) != None:
            right_value         = self.bst_value(root.right)
            right_value_diff    = abs(right_value - self.target)

            if right_value_diff < closest_value_diff:
                closest_target      = right_value
                closest_value_diff  = right_value_diff

        return closest_target
        

    def solve(self):

        my_tree = MakeTree(self.root)

        root    = my_tree.get_tree_root()

        return self.bst_value(root)