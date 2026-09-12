class BTLevelOrderTwo():

    def __init__(self, tree):
        self.tree   = tree

    def bfs(self, root):
        
        visit_q     = []

        output_dict = {}

        #Initialize. Starting node and level
        visit_q.append((root, 1))
        max_level = 0

        while (len(visit_q) > 0):
            
            cur_node_tuple = visit_q.pop(0)
            cur_node    = cur_node_tuple[0]
            cur_level   = cur_node_tuple[1]

            #Record in hash table
            if cur_level not in output_dict:
                output_dict[cur_level]  = [cur_node.val]

                max_level = max(max_level, cur_level)

            else:
                output_dict[cur_level].append(cur_node.val)

                max_level = max(max_level, cur_level)

            new_level   = cur_level + 1

            #Insert new node tuple to Q
            if cur_node.left != None:
                new_node    = cur_node.left
                visit_q.append((new_node, new_level))

            if cur_node.right != None:
                new_node    = cur_node.right
                visit_q.append((new_node, new_level))

        return (output_dict, max_level)

    def solve(self):

        from make_tree import MakeTree

        mytree  = MakeTree(self.tree)
        root    = mytree.get_tree_root()

        if root == None:
            return []

        output_dict, max_level = self.bfs(root)
        
        output = []

        for i in range(max_level, 0, -1):
            print(f"output_dict[i] = {output_dict[i]}")
            output.append(output_dict[i])

        return output