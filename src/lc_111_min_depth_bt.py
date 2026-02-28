class MinDepthBT():

    def __init__(self, bt):
        self.bt = bt


    def get_min_depth(self, node):
        
        if node == None:
            return None
        
        left    = self.get_min_depth(node.left)
        right   = self.get_min_depth(node.right)

        if (left == None) and (right == None):
            return 1
        elif left == None:
            return 1 + right
        elif right == None:
            return 1 + left
        else:
            return 1 + min(left, right)

    def solve(self):

        root = self.bt

        if len(root) == 0:
            return 0

        return self.get_min_depth(root)
