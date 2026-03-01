class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MinDepthBT():

    def __init__(self, bt):
        self.bt = bt

    def get_adj_dict(self, adj_dict, root_node):
        
        #Stop condition
        if root_node == None:
            return
        
        #Work: Fill Adjency dictionary
        if (root_node.left == None) and (root_node.right == None):
            adj_dict[root_node.val] = []
        elif  (root_node.left == None):
            adj_dict[root_node.val] = [root_node.right.val]
        elif  (root_node.right == None):
            adj_dict[root_node.val] = [root_node.left.val]
        else:
            adj_dict[root_node.val] = [root_node.left.val, root_node.right.val]

        #Recursion
        self.get_adj_dict(adj_dict, root_node.left)
        self.get_adj_dict(adj_dict, root_node.right)

        return

    def get_min_depth_bfs(self, to_visit_dict, node_val):
        
        #Setup
        visiting_q  = []

        #Map Node value : level
        output      = {}


        #Default
        visiting_q.append(node_val)
        output[node_val] = 1


        while visiting_q:
            
            visiting_val = visiting_q.pop(0)
            
            #If leaf node (Node with no children).
            if to_visit_dict[visiting_val] == []:
                return output[visiting_val]

            for child in to_visit_dict[visiting_val]:

                visiting_q.append(child)
                output[child] = output[visiting_val] + 1

        return 0

    def get_min_depth_dfs(self, node):
        
        if node == None:
            return None
        
        left    = self.get_min_depth_dfs(node.left)
        right   = self.get_min_depth_dfs(node.right)

        if (left == None) and (right == None):
            return 1
        elif left == None:
            return 1 + right
        elif right == None:
            return 1 + left
        else:
            return 1 + min(left, right)

    def solve_dfs(self):

        root = self.bt

        if root == None:
            return 0

        return self.get_min_depth_dfs(root)
    
    def solve_bfs(self):

        adj_dict = {}

        root = self.bt

        if root == None:
            return 0
        
        self.get_adj_dict(adj_dict, root)

        return self.get_min_depth_bfs(adj_dict, root.val)
   