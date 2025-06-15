from make_tree import MakeTree

class RangeSumBST():

    def __init__(self, root, low, high):
        self.root   = root
        self.low    = low
        self.high   = high

    def range_sum(self, root):

        if root == None:
            return 0
        
        left_value = right_value = 0
        
        left_value  = self.range_sum(root.left)
        right_value = self.range_sum(root.right)

        if root.val >= self.low and root.val <= self.high:
            current_value   = root.val
        else:
            current_value   = 0

        return left_value + right_value + current_value


    def solve(self):

        my_tree     = MakeTree(self.root)
        tree_root = my_tree.get_tree_root()

        return self.range_sum(tree_root)