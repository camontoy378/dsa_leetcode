class MinStack():

    def __init__(self):
        self.stack              = []
        self.value_index        = 0
        self.min_value_index    = 1

    def push(self, val: int) -> None:

        if not self.stack:

            print("Stack is empty")
            
            self.stack.append([val, val])

            #print(self.stack)
        else:
            #Determine min
            new_min = min(val, self.stack[-1][self.min_value_index])

            self.stack.append([val, new_min])

            #print(self.stack)


    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][self.value_index]
        

    def getMin(self) -> int:
        return self.stack[-1][self.min_value_index]



    def solve(self):

        return True


def main():

    print("In Main")

    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())

if __name__ == "__main__":
    main()