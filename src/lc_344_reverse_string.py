class ReverseString():

    def __init__(self, s : list[str]):
        self.s = s

    def solve(self):

        s = self.s

        #Setup
        ptr_First   = 0
        ptr_Last    = len(s) - 1

        while ( ptr_First < ptr_Last ):
            
            #Swap
            temp            = s[ptr_First]
            s[ptr_First]    = s[ptr_Last]
            s[ptr_Last]     = temp

            #Update pointers
            ptr_First       += 1
            ptr_Last        -= 1