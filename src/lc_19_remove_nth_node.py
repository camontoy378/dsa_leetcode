class Node():

    def __init__(self, val):
        self.val    = val
        self.next   = None

class LinkedList():

    def __init__(self):
        self.head   = None

    def insert(self, val: int):

        #Create Node and initialize
        tmp = Node(val)

        tail = self.head

        #Insert node
        if(self.head == None):
            self.head = tmp

        else:
            #Position pointer            
            while( tail.next != None):
                tail = tail.next

            tail.next = tmp

    def create_ll(self, head_arr):
            
            for num in head_arr:
                self.insert(num)

    def print_ll(self):

        tmp = self.head

        while(tmp != None):
            print(f"{tmp.val}, ", end="")
            tmp = tmp.next

        print("")    

class RemoveNthNodeFromEnd():

    def __init__(self, head, n):
        self.head       = head
        self.n          = n

    def delete_nth_node(self, head, nth_node: int):

        prev    = None
        cur     = head

        for i in range(1, nth_node):
            prev    = cur
            cur     = cur.next

        if (prev == None):
            prev        = cur.next
            head        = cur.next
        else:
            prev.next  = cur.next

        return head

    def output(self):

        output = []

        tmp = self.head

        while(tmp != None):
            output.append(tmp.val)
            tmp = tmp.next

        return output

    def solve(self):

        head    = self.head
        n       = self.n

        #Determine how many nums
        num_items  = 0
    
        tmp = head

        while(tmp != None):
            num_items += 1
            tmp = tmp.next

        nth_node = num_items - n + 1

        self.head = self.delete_nth_node(head, nth_node)

        return self.head