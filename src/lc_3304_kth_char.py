class KthChar():

    alphabet_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m", \
                     "n","o","p","q","r","s","t","u","v","w","x","y","z","a"]

    def __init__(self, k):
        self.k  = k

    def find_k_char(self, string):
        
        if len(string) >= self.k:
            return string
        
        new_string = string + self.next_chars(string)

        return self.find_k_char(new_string)


    def next_chars(self, nc_string):
        
        output = ""

        for my_char in nc_string:

            for char_index in range(len(self.alphabet_list)):

                if my_char == self.alphabet_list[char_index]:
                    output = output + self.alphabet_list[char_index + 1]
                    break

        return output
            

    def solve(self):

        new_string = self.find_k_char("a")
        return new_string[self.k - 1]
        