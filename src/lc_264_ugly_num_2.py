class UglyNumTwo():

    def __init__(self, n):
        self.n  = n

    def solve(self):

        n = self.n
    
        prime_factors_limit = [2,3,5]

        ugly_num_set = {1}
        
        output = [1]
        count   = 1

        
        while len(output) < n:

            count += 1

            if self.is_ugly_num(prime_factors_limit, count, ugly_num_set):
                output.append(count)

        return output[-1]

    def is_ugly_num(self, prime_factors_limit, count, ugly_num_set):

        temp = count


        for num in prime_factors_limit:

            modulo = 0

            while modulo == 0:
                modulo = temp % num

                if modulo == 0:
                    temp = temp / num

                    #If already an ugly num
                    if temp in ugly_num_set:
                        ugly_num_set.add(count)
                        return True

        if temp == 1:
            ugly_num_set.add(count)
            return True
        else:
            return False
