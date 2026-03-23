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

class ReverseLinkedList_iter():

    def __init__(self, num_array):
        self.num_array  = num_array

    def reverse_ll(self):

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


    def solve(self):

        head = self.reverse_ll()

        output = []
        ptr_cur_node = head

        while ptr_cur_node != None:

            output.append(ptr_cur_node.data)

            ptr_cur_node = ptr_cur_node.next

        return output
