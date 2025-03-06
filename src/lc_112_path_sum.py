from make_tree import *

class PathSum():

    def __init__(self, tree_array, expected_value):
        self.tree_array     = tree_array
        self.expected_value = expected_value

    def solve(self):

        i           = 0
        n           = len(self.tree_array)
        sum         = 0
        output_init = False

        mytree  = MakeTree(self.tree_array)
        root    = mytree.insert_level_order(i, n)

        return self.tree_trasverse(root, self.expected_value, sum, output_init)
    
    def tree_trasverse(self, root, expected_value, sum, output):

        if root == None:
            return output
        
        if output:
            return output
        
        print(f"data = {root.data}")
        sum += root.data

        if root.left == None and root.right == None:
            return sum == expected_value
        

        if output == False:
            output = self.tree_trasverse(root.left, expected_value, sum, output)
            

        if output == False:
            output = self.tree_trasverse(root.right, expected_value, sum, output)
        
        return  output