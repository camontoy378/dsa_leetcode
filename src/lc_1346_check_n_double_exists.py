
class CheckNDoubleExists():

    def __init__(self, int_array):
        self.int_array = int_array

    def solve(self):

        hash_table = {}

        for i in range(len(self.int_array)):
            
            if (self.int_array[i]/2) in hash_table or (self.int_array[i]*2) in hash_table:
                return True
            else:
                hash_table[self.int_array[i]] = i

        return False