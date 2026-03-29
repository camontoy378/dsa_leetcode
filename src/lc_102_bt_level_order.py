class BTLevelOrder():

    def __init__(self, input, dsa_type):
        self.input      = input
        self.dsa_type   = dsa_type


    def bfs(self, parent_node, visiting_q):

        #Initialize
        ptr_index   = 0
        level_index = 1
        output = []

        level = 1
        visiting_q.append([parent_node, level])
        
        while len(visiting_q) > 0:

            #Get current parent node
            visiting_node = visiting_q.pop(0)

            #Set output
            if len(output) < visiting_node[level]:
                output.append([ visiting_node[ptr_index].val ])
            else:
                output[ visiting_node[level_index] - 1].append( visiting_node[ptr_index].val )

            #Get children nodes and put in Q
            if visiting_node[ptr_index].left != None:
                left_child_ptr      = visiting_node[ptr_index].left
                left_child_level    = visiting_node[level_index] + 1

                visiting_q.append([left_child_ptr, left_child_level])

            if visiting_node[ptr_index].right != None:    
                right_child_ptr     = visiting_node[ptr_index].right
                right_child_level   = visiting_node[level_index] + 1

                visiting_q.append([right_child_ptr, right_child_level])

        return output
            

    def dfs(self, parent_node, level_dict, level):

        #Stop condition
        if parent_node == None:
            return 0
        
        if level not in level_dict:
            
            level_dict[level] = [parent_node.val]

        else:
            level_dict[level].append(parent_node.val)
        
        return max(level, self.dfs(parent_node.left, level_dict, level + 1), self.dfs(parent_node.right, level_dict, level + 1))


    def solve(self):

        from make_tree import MakeTree

        mytree  = MakeTree(self.input)

        root    = mytree.get_tree_root()

        #Start coding.

        #Setup
        output      = []

        
        if root == None:
            return []
        
        if self.dsa_type == "dfs":

            #Setup
            level_dict  = {}

            max_level = self.dfs(root, level_dict, 1)

            for i in range(1, max_level + 1):
                output.append(level_dict[i])

        elif self.dsa_type == "bfs":
            
            #Setup
            visiting_q  = []

            output = self.bfs(root, visiting_q)
            
        return output
    