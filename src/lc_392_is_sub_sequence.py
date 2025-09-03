class Subsequence():

    def __init__(self, s, t):
        self.s  = s
        self.t  = t

    def solve(self):

        s_length    = len(self.s)
        s_index     = 0

        if s_length == 0:
            return True 

        for t_char in self.t:

            if t_char == self.s[s_index]:
                s_index += 1

                if s_index == s_length:
                    return True 

        return False