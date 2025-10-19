class RemoveKDigits():

    def __init__(self, number, k):
        self.num     = number
        self.k          = k

    def is_stack_empty(self, stack):
        return len(stack) <= 0
    
    def result(self, stack):

        output = ""
        leading_zeros = True

        for char in stack:
            if not leading_zeros:
                output += char
            elif char != "0" and leading_zeros:
                leading_zeros = False
                output += char

        return output

        # Alternatively, can use line of code below to create the result from
        #   stack and remove leading zeros.            
        #output = "".join(stack).lstrip("0")


    def solve(self):

        k = self.k

        if len(self.num) <= k:
            return "0"

        stack = []

        for mynum in self.num:

            while ( (k > 0) and (not self.is_stack_empty(stack) ) and (stack[-1] > mynum )):
                
                stack.pop()
                k -= 1
                
            stack.append(mynum) 
            
        while(k > 0):
            stack.pop()
            k -= 1
            
        output = self.result(stack)

        if output == "":
            return "0"
        else:
            return output
            