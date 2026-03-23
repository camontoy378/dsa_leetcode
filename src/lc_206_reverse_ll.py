class Node():

    def __init__(self, data):
        self.data   = data
        self.next   = None

class CreateLinkedList():

    def __init__(self, num_array):
        self.num_array  = num_array

    def create_ll(self):

        head        = None
        ptr_last    = None

        for num in self.num_array:

            if head == None:
                head        = Node(num)
                ptr_last    = head
            else:
                ptr_last.next = Node(num)
                ptr_last = ptr_last.next

        return head

class ReverseLinkedList():

    def __init__(self, num_array, solution_type):
        self.num_array      = num_array
        self.solution_type  = solution_type

    def reverse_ll_iter(self):

        #Create linked list
        cll     = CreateLinkedList(self.num_array)
        head    = cll.create_ll()

        #Setup
        tmp_p   = None
        tmp_n   = head

        #If no nodes
        if not head:
            return None

        while (head.next != None) :
            tmp_n       = head.next
            head.next   = tmp_p
            tmp_p       = head
            head        = tmp_n

        head.next = tmp_p

        return head
    
    def reverse_ll_rec(self, ptr_curr, ptr_prev, head):
        
        #Stop condition
        if ptr_curr.next == None:
            head            = ptr_curr
            ptr_curr.next   = ptr_prev
            return head
        
        #Work
        ptr_prev_new    = ptr_curr
        ptr_curr_new    = ptr_curr.next
        ptr_curr.next   = ptr_prev

        return self.reverse_ll_rec(ptr_curr_new, ptr_prev_new, head)


    def solve(self):

        #Create linked list
        cll         = CreateLinkedList(self.num_array)
        head        = cll.create_ll()


        #Factory

        #Solve iterively
        if self.solution_type == "iter":
            head = self.reverse_ll_iter()

        #Solve recursively
        elif self.solution_type == "rec":
            #If no nodes
            if not head:
                return []

            ptr_prev    = None
            ptr_curr    = head

            head = self.reverse_ll_rec(ptr_curr, ptr_prev, head)
        else:
            print("No solution type given")
            print("Exiting")
        

        output = []
        ptr_cur_node = head

        while ptr_cur_node != None:

            output.append(ptr_cur_node.data)

            ptr_cur_node = ptr_cur_node.next

        return output
