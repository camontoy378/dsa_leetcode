
from make_tree import MakeTree

class MaxDepthBinaryTree():

    def __init__(self, tree_array):
        self.tree_array               = tree_array

    def search_max_depth(self, root, sum):

        #Base case
        if root == None:
            return sum
        
        sum += 1

        return max(self.search_max_depth(root.left, sum), 
                   self.search_max_depth(root.right, sum))


    def solve(self):

        #Initialize
        sum     = 0

        mytree  = MakeTree(self.tree_array)

        root    = mytree.get_tree_root()

        return self.search_max_depth(root, sum)