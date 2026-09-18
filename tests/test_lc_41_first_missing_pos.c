#include <unity.h>
#include "lc_41_first_missing_pos.c"

void setUp(){
    //
}

void tearDown(){
    //
}

void test_firstMissingPositive(){
    
    //Test 1
    int nums[]      = {1,2,0};
    int output      = 3;
    int nums_size   = sizeof(nums) / sizeof(nums[0]); 

    TEST_ASSERT( firstMissingPositive(nums, nums_size) == output );

    //Test 2
    int nums_2[]    = {3,4,-1,1};
    output          = 2;
    nums_size       = sizeof(nums_2) / sizeof(nums_2[0]);

    TEST_ASSERT( firstMissingPositive(nums_2, nums_size) == output );

    //Test 3
    int nums_3[]    = {7,8,9,11,12};
    output          = 1;
    nums_size       = sizeof(nums_3) / sizeof(nums_3[0]); 

    TEST_ASSERT( firstMissingPositive(nums_3, nums_size) == output );

    //Test 4
    int nums_4[]    = {0,2,2,1,1};
    output          = 3;
    nums_size       = sizeof(nums_4) / sizeof(nums_4[0]);

    TEST_ASSERT( firstMissingPositive(nums_4, nums_size) == output );
}