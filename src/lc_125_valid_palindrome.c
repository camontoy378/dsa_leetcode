#include <stdbool.h>

char lower_case(char c)
{
    if ((c >= 'A') && (c <= 'Z'))
    {
        //
        int conv_factor = 'a' - 'A';

        c = c + conv_factor;
        return c;
    }
    else
    {
        return c;
    }
}

bool is_alphanumeric(char c)
{
    if ( (c >= 'a') && (c <= 'z') || (c >= 'A') && (c <= 'Z') || (c >= '0') && (c <= '9') )
    {
        return true;    
    }

    return false;

}

int len_string(char * s)
{
    int counter = 0;
    int i       = 0;

    for ( i; s[i] != '\0'; i++)
    {
        counter++;
    }

    return counter;
}

bool isPalindrome(char* s)
{
    int left_index  = 0;
    int right_index = len_string(s) - 1;
    
    while (left_index < right_index)
    {
        while ( (left_index < right_index) && ( ! is_alphanumeric(s[left_index])) )
        {
            left_index++;
        }

        while ( (left_index < right_index) && ( ! is_alphanumeric(s[right_index])) )
        {
            right_index--;
        }

        if ( ! ( lower_case(s[left_index]) == lower_case(s[right_index]) ) )
        {
            return false;
        }

        left_index++;
        right_index--;
    }
    
    return true;
}