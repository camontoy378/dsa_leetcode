class NumOneBits():

    def __init__(self, n):
        self.n  = n

    def solve(self):

        n = self.n

        count           = 0
        binary_string   = bin(n)
        str_len         = len(binary_string)

        #ignore first 2 characters 'ob'

        for i in range(2,str_len):

            if binary_string[i] == "1":
                count += 1

        return count