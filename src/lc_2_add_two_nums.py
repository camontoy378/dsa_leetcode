class ListNode:
    def __init__(self, val=0, next=None):
        self.val    = val
        self.next   = next


class AddTwoNums():

    def __init__(self, ll1,ll2):
        self.ll1    = ll1
        self.ll2    = ll2

    def ll_append(self, ptr_head, ptr_tmp, val):

        if ptr_head == None:
            ptr_head = ptr_tmp = ListNode(val)
        else:
            ptr_tmp.next    = ListNode(val)
            ptr_tmp         = ptr_tmp.next

        return ptr_head, ptr_tmp



    def make_ll(self,ll_array):
        
        head = tmp = None

        for value in ll_array:

            head, tmp = self.ll_append(head, tmp, value)
            
        return head

    def solve(self):

        #Create LL
        l1 = tmp1 = self.make_ll(self.ll1)
        l2 = tmp2 = self.make_ll(self.ll2)

        if l1 == None:
            return None
        if l2 == None:
            return None

        
        add_carry   = 0
        output_head = output_tmp = None

        #Add numbers
        while ( tmp1 != None) or (tmp2 != None) or (add_carry == 1):
            
            #Sum
            if (tmp1 == tmp2 == None) and (add_carry == 1):
                output_head, output_tmp = self.ll_append(output_head, output_tmp, add_carry)

                return output_head
            elif tmp1 == None:
                sum = tmp2.val + add_carry
            elif tmp2 == None:
                sum = tmp1.val + add_carry
            else:
                sum = tmp1.val + tmp2.val + add_carry

            #Get output digit
            if sum >= 10:
                sum         = sum - 10
                add_carry   = 1

            else:
                add_carry   = 0

            output_head, output_tmp = self.ll_append(output_head, output_tmp, sum)


            #Advance to next num
            if tmp1 != None:
                tmp1 = tmp1.next
            if tmp2 != None:
                tmp2 = tmp2.next

        print(f"output = {output_head.val}")
        return output_head
    

