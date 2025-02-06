
class ListNode:
    def __init__(self, val=0, next=None):
        self.val    = val
        self.next   = next

class Merge2SortedLists:

    def __init__(self, list1: ListNode, list2: ListNode):
        self.list1  = list1
        self.list2  = list2

    def solve(self):

        temp = ListNode()
        print(temp.val)

        ptr1 = self.list1
        ptr2 = self.list2
        print(ptr1)
        print(ptr2)

        ll1_head: ListNode = None
        ll2_head: ListNode = None

        #create linked list 1
        for item in self.list1:
            if ll1_head == None:
                ll1_head = ListNode(item)
                ptr1 = ll1_head
            else:
                temp = ListNode(item)
                ptr1.next = temp
                ptr1 = ptr1.next

        #create linked list 2
        for item in self.list2:
            if ll2_head == None:
                ll2_head = ListNode(item)
                ptr2 = ll2_head
            else:
                temp = ListNode(item)
                ptr2.next = temp
                ptr2 = ptr2.next

        #Merget 2 lists
        ptr1 = ll1_head
        ptr2 = ll2_head
        head_out: ListNode = None

        while ptr1 != None or ptr2 != None:
            if ptr1 == None:
                if head_out == None:
                    head_out = ListNode(ptr2.val)
                    ptr_out = head_out
                    ptr2 = ptr2.next
                else:
                    tmp = ListNode(ptr2.val)
                    ptr_out.next = tmp
                    ptr_out = ptr_out.next
                    ptr2 = ptr2.next
            elif ptr2 == None:
                if head_out == None:
                    head_out = ListNode(ptr1.val)
                    ptr_out = head_out
                    ptr1 = ptr1.next
                else:
                    tmp = ListNode(ptr1.val)
                    ptr_out.next = tmp
                    ptr_out = ptr_out.next
                    ptr1 = ptr1.next
            elif ptr2.val <= ptr1.val:
                if head_out == None:
                    head_out = ListNode(ptr2.val)
                    ptr_out = head_out
                    ptr2 = ptr2.next
                else:
                    tmp = ListNode(ptr2.val)
                    ptr_out.next = tmp
                    ptr_out = ptr_out.next
                    ptr2 = ptr2.next
            else:
                if head_out == None:
                    head_out = ListNode(ptr1.val)
                    ptr_out = head_out
                    ptr1 = ptr1.next
                else:
                    tmp = ListNode(ptr1.val)
                    ptr_out.next = tmp
                    ptr_out = ptr_out.next
                    ptr1 = ptr1.next

        print("Output:")
   

        output_list = []
        ptr_out = head_out
        while ptr_out != None:
            print(ptr_out.val)
            output_list.append(ptr_out.val)
            ptr_out = ptr_out.next

        return output_list
