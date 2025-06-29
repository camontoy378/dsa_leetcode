class ValidAnagram():

    def __init__(self, s, t):
        self.s  = s
        self.t  = t

    def num_letters(self, s, t, s_dict, t_dict):

        for i in range(len(s)):
            
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1

            if t[i] in t_dict:
                t_dict[t[i]] += 1
            else:
                t_dict[t[i]] = 1

    def solve(self):

        s_dict = {}
        t_dict = {}

        if len(self.s) != len(self.t):
            return False
        
        self.num_letters(self.s, self.t, s_dict,t_dict)
        
        for key, value in s_dict.items():

            try:
                t_dict[key]
            except Exception as e:
                print(e)
                return False
             
            if t_dict[key] != value:
                return False

        return True
        