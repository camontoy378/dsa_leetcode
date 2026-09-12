class FizzBuzz():

    def __init__(self, n):
        self.n  = n

    def solve(self):

        n = self.n

        output = []

        mystring = ""

        for i in range(1, n+1):

            
            if not (i % 3):
                mystring = mystring + "Fizz"

            if not (i % 5):
                mystring = mystring + "Buzz"

            if mystring == "":
                mystring = str(i)

            output.append(mystring)

            mystring = ""

        return output