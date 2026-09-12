import setup_paths

from lc_412_fizz_buzz import FizzBuzz

def test_solve():

    #Test 1
    n       = 3
    output  = ["1","2","Fizz"]

    solution = FizzBuzz(n)

    assert solution.solve() == output

    #Test 2
    n       = 5
    output  = ["1","2","Fizz","4","Buzz"]

    solution = FizzBuzz(n)

    assert solution.solve() == output

    #Test 3
    n       = 15
    output  = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

    solution = FizzBuzz(n)

    assert solution.solve() == output