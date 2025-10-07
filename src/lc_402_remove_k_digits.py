class RemoveKDigits():

    def __init__(self, number, k):
        self.number     = number
        self.k          = k

    def solve(self):

        stack       = []
        num_high    = ""
        num_low     = ""
       
        len_num_str = len(self.number)
        
        limit   =  len_num_str - self.k

        if len_num_str <= self.k:
            return "0"


        #create number
        current_num = num_low = self.number[self.k:]
        stack.append(int(current_num))

        
        for i in range(0, limit + 1):
            num_high += self.number[i]
            num_low = num_low[1:]
            current_num = int(num_high + num_low)

            if current_num < stack[-1]:
                stack.append(current_num)


        return str(stack[-1])