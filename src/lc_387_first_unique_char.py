class FirstUniqueChar():

    def __init__(self, s):
        self.s  = s

    def solve(self):

        s   = self.s

        char_repeat = {}

        #Count # times char repeats
        for i in range(len(s)):

            if s[i] in char_repeat:
                char_repeat[s[i]] += 1
            else:
                char_repeat[s[i]] = 0

        #Search for non repeating char
        for i in range(len(s)):

            if char_repeat[s[i]] == 0:
                return i

        return -1