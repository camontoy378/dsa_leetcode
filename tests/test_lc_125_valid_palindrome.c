#include <unity.h>
#include "lc_125_valid_palindrome.c"

#define TRUE    1
#define FALSE   0

void setup()
{
    //
}

void teardown()
{
    //
}

void test_isPalindrome()
{
    //Test 1
    char s[]    = "A man, a plan, a canal: Panama";
    int output  = TRUE;

    TEST_ASSERT (isPalindrome(s) == output);

}