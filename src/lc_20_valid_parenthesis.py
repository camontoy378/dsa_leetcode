
class ValidParenthesis:
    
    def __init__(self, input):
        self.input = input

    def solve(self):

        hash_map = { "(":")", "[":"]", "{":"}"}

        mystack = []

        for char in self.input:
            if char in hash_map:
                mystack.append(char)
            elif mystack != [] and mystack[-1] in hash_map and char == hash_map[mystack[-1]]:
                mystack.pop()
            else:
                mystack.append(char)

        if mystack == []:
            return True
        else:
            return False
        