#include <unity.h>

#include "lc_169_majority.c"

void setUp(){
    //
}

void tearDown(){
    //
}

void test_majorityElement(){
    
    //Test 1
    int nums[]      = {3,2,3};
    int output      = 3;
    int nums_size   = sizeof(nums) / sizeof(nums[0]);

    TEST_ASSERT( majorityElement(nums, nums_size) == output );

    //Test 2
    int nums_2[]    = {2,2,1,1,1,2,2};
    output          = 2;
    nums_size       = sizeof(nums_2) / sizeof(nums_2[0]);

    TEST_ASSERT( majorityElement(nums_2, nums_size) == output );
}