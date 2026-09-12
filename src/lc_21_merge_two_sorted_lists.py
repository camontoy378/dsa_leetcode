
class ListNode:
    def __init__(self, val=0, next=None):
        self.val    = val
        self.next   = next

class Merge2SortedLists:

    def __init__(self, list1: ListNode, list2: ListNode):
        self.list1  = list1
        self.list2  = list2

    def create_ll(self, array):

        head = ptr_tmp = None
        
        for value in array:

            #insert
            if head != None:
                ptr_tmp.next    = ListNode(value)
                ptr_tmp         = ptr_tmp.next
            else:
                head = ptr_tmp = ListNode(value)

        return head


    def solve(self):

        #create linked list 1
        ll1_head = self.create_ll(self.list1)
        
        #create linked list 2
        ll2_head = self.create_ll(self.list2)
        
        #Merget 2 lists
        ptr1 = ll1_head
        ptr2 = ll2_head
        head_out = tmp_ptr = None

        while (ptr1 != None) and (ptr2 != None):

            if ptr1.val < ptr2.val:
                if head_out != None:
                    tmp_ptr.next = ListNode(ptr1.val)

                    ptr1        = ptr1.next
                    tmp_ptr     = tmp_ptr.next 
                else:
                    head_out    = tmp_ptr = ListNode(ptr1.val)

                    ptr1        = ptr1.next
            else:
                if head_out != None:
                    tmp_ptr.next = ListNode(ptr2.val)

                    ptr2        = ptr2.next
                    tmp_ptr     = tmp_ptr.next 
                else:
                    head_out    = tmp_ptr = ListNode(ptr2.val)

                    ptr2        = ptr2.next

        while (ptr1 != None):
            
            if head_out != None:
                tmp_ptr.next = ListNode(ptr1.val)

                ptr1        = ptr1.next
                tmp_ptr     = tmp_ptr.next 
            else:
                head_out    = tmp_ptr = ListNode(ptr1.val)

                ptr1        = ptr1.next

        while (ptr2 != None):
            
            if head_out != None:
                tmp_ptr.next = ListNode(ptr2.val)

                ptr2        = ptr2.next
                tmp_ptr     = tmp_ptr.next 
            else:
                head_out    = tmp_ptr = ListNode(ptr2.val)

                ptr2        = ptr2.next
       

        print("Output:")
   
        output_list = []
        ptr_out = head_out
        while ptr_out != None:
            print(ptr_out.val)
            output_list.append(ptr_out.val)
            ptr_out = ptr_out.next

        return output_list
