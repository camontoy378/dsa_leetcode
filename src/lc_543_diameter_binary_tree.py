from make_tree import MakeTree

class DiameterBinaryTree():

    def __init__(self, root):
        self.root   = root

    def length_longest_path(self, root):

        if root == None:
            return 0

        if root.left == None and root.right == None:
            return 0

        right_sum = left_sum = 0

        right_sum   = self.length_longest_path(root.right)
        left_sum    = self.length_longest_path(root.left)
        
        return 1 + max(left_sum, right_sum)

    
    def solve(self):

        my_tree = MakeTree(self.root)

        tree_root = my_tree.get_tree_root()

        left_longest_path = right_longest_path = 0

        if tree_root.left != None:
            left_longest_path = 1 + self.length_longest_path(tree_root.left)
        
        if tree_root.right != None:
            right_longest_path = 1 + self.length_longest_path(tree_root.right)

        longest_path = left_longest_path + right_longest_path

        return longest_path