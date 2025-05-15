from make_tree import MakeTree

class SymmetricTree():

    def __init__(self, input):
        self.input  = input

    def get_nums_from_array_tree(self, node_index, q, trasverse_left):

        if node_index >= len(self.input):
            return

        if trasverse_left:

            #recursive call to left nodes
            self.get_nums_from_array_tree( 2 * node_index + 1, q, trasverse_left)

            #recursive call to right nodes
            self.get_nums_from_array_tree( 2 * node_index + 2, q, trasverse_left)

        else:
            #recursive call to right nodes
            self.get_nums_from_array_tree( 2 * node_index + 2, q, trasverse_left)

            #recursive call to left nodes
            self.get_nums_from_array_tree( 2 * node_index + 1, q, trasverse_left)

        q.append(self.input[node_index])

        return
    
    def get_nums_from_node_tree(self, node, q, trasverse_left):
        
        if node == None:
            return q.append(None)
        
        if trasverse_left:

            #recursive call to left nodes
            self.get_nums_from_node_tree( node.left, q, trasverse_left)

            #recursive call to right nodes
            self.get_nums_from_node_tree( node.right, q, trasverse_left)

        else:
            #recursive call to right nodes
            self.get_nums_from_node_tree( node.right, q, trasverse_left)

            #recursive call to left nodes
            self.get_nums_from_node_tree( node.left, q, trasverse_left)

        q.append(node.val)

        return



    def solve_array(self):

        init_root_node_index    = 0
        init_left_node_index    = 1
        init_right_node_index   = 2

        trasverse_left  = True
        trasverse_right = False


        q_left  = []
        q_right = []

        self.get_nums_from_array_tree(init_left_node_index, q_left, trasverse_left)
        self.get_nums_from_array_tree(init_right_node_index, q_right, trasverse_right)

        return q_left == q_right
    

    def solve_tree(self):

        trasverse_left  = True
        trasverse_right = False

        make_tree = MakeTree(self.input)

        my_tree = make_tree.get_tree_root()


        q_left  = []
        q_right = []

        self.get_nums_from_node_tree(my_tree.left, q_left, trasverse_left)
        self.get_nums_from_node_tree(my_tree.right, q_right, trasverse_right)

        return q_left == q_right