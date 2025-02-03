from lc_20_valid_parenthesis import ValidParenthesis
from lc_1652_defuse_bomb import DefuseBomb

def main():

    input_list  = [10,5,7,7,3,2,10,3,6,9,1,6]
    k           = -4

    #solution = ValidParenthesis(input)
    solution = DefuseBomb(input_list, k)
    
    solution.solve()

if __name__ == "__main__":
    main()