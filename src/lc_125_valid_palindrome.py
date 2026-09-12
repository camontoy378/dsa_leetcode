class ValidPalindrome():

    def __init__(self, input_string):
        self.input_string   = input_string

    def is_alphanumeric(self, my_char):
        
        if ( (my_char >= 'a') and (my_char <= 'z') \
            or (my_char >= 'A') and (my_char <= 'Z') \
            or (my_char >= '0') and (my_char <= '9') ) :
            return True
        else:
            return False

        
    def solve(self):

        s = self.input_string

        left_index  = 0
        right_index = len(s) - 1

        #New string with all lower case characters
        new_string = s.lower()

        while( left_index < right_index):

            while ( left_index < right_index) and ( not self.is_alphanumeric(new_string[left_index]) ):
                left_index += 1

            while ( left_index < right_index) and ( not self.is_alphanumeric(new_string[right_index]) ):
                right_index -= 1
            
            if ( not (new_string[left_index] == new_string[right_index] ) ):
                return False
            
            left_index += 1
            right_index -= 1
            
        return True