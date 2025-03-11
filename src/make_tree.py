
class Node:

    def __init__(self, val):
        self.val    = val
        self.left   = None
        self.right  = None

class MakeTree():

    def __init__(self, array):
        self.array          = array
        self.left_index     = 0
        self.array_length   = len(array)

    def get_tree_root(self):

        return self.insert_level_order(self.left_index, self.array_length) 

    def insert_level_order(self, i, n):

        root    = None
        
        #Base case
        if i < n and self.array[i] != None:

            root = Node(self.array[i])

            
            root.left   = self.insert_level_order(2 * i + 1, n)

            root.right  = self.insert_level_order(2 * i + 2, n)

        return root
    
    def print_in_order(self, root):

        if root != None:
            self.print_in_order(root.left)
            print(root.data, end=" ")
            self.print_in_order(root.right)
