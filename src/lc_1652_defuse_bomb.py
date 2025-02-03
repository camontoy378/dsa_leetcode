
class DefuseBomb:

    def __init__(self, input_list, k):
        self.input_list = input_list
        self.k          = k

    def solve(self):

        output  = []

        #Add initial window
        len_list    = len(self.input_list)
        mod_num     = len_list


        #Setup vars
        sum = 0
        k = self.k

        if self.k > 0:
            start   = 1
            end     = 1 + self.k
        elif self.k == 0:
            start   = 1
            end     = len_list
        else:
            #Make indexes positive.
            start   = self.k    + len_list
            end     = 0         + len_list

        #Initial sum
        for i in range(start, end):
            sum += self.input_list[i]

        if self.k == 0:
            output.append(0)
        else:
            output.append(sum)

        #Update vars
        if self.k < 0:
            end = 0 + len_list + start -1
        else:
            end = len_list

        #Sliding windows
        for j in range(start, end):
            if self.k == 0:
                output.append(0)
            else:
                prev_index = (j % mod_num)
                next_index = ((j + abs(self.k)) % mod_num)  
                
                sum += -(self.input_list[prev_index]) + self.input_list[next_index]

                output.append(sum) 

        return output