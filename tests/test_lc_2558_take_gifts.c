#include <unity.h>
#include "lc_2558_take_gifts.c"


void setUp()
{

}

void tearDown()
{

}

void test_pickGifts()
{
    //Test 1
    int input_1[] = {25,64,9,4,100};
    int k       = 4;
    int output  = 29;

    int size_input = sizeof(input_1)/sizeof(int);

    TEST_ASSERT ( output == pickGifts(input_1, size_input, k) );


    //Test 2
    int input_2[] = {1,1,1,1};
    k       = 4;
    output  = 4;

    size_input = sizeof(input_2)/sizeof(int);
    
    TEST_ASSERT ( output == pickGifts(input_2, size_input, k) );
}
