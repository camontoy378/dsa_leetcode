#include <unity.h>
#include "lc_209_min_size_subarray.c"

void setUp(void){
    //
}

void tearDown(void){
    //
}

void test_minSubArrayLen(void){
    
    //Test 1
    int target      = 7;
    int nums[]      = {2,3,1,2,4,3};
    int output      = 2;
    int nums_size   = sizeof(nums)/sizeof(nums[0]); 

    TEST_ASSERT(minSubArrayLen(target, nums, nums_size) == output);

    //Test 2
    target          = 4;
    int nums_2[]    = {1,4,4};
    output          = 1;
    nums_size       = sizeof(nums_2)/sizeof(nums_2[0]); 

    TEST_ASSERT(minSubArrayLen(target, nums_2, nums_size) == output);

    //Test 3
    target          = 11;
    int nums_3[]    = {1,1,1,1,1,1,1,1};
    output          = 0;
    nums_size       = sizeof(nums_3)/sizeof(nums_3[0]); 

    TEST_ASSERT(minSubArrayLen(target, nums_3, nums_size) == output);
}