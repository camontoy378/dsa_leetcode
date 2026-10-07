#include <unity.h>

#include "lc_1_two_sum.c"


void startUp(void){
    //
}

void tearDown(void){
    //
}

void test_twoSum(void){
    
    //Test 1
    int nums[]      = {2,7,11,15};
    int target      = 9;
    int output[]    = {0,1};

    int nums_size   = sizeof(nums) / sizeof(nums[0]);
    int return_size = 2;

    int *my_output  = twoSum(nums, nums_size, target, &return_size);
    TEST_ASSERT(  my_output[0] == output[0]);
    TEST_ASSERT(  my_output[1] == output[1]);
    
    free(my_output);

    //Test 2
    int nums_2[]    = {3,2,4};
    target          = 6;
    int output_2[]  = {1,2};

    nums_size       = sizeof(nums_2) / sizeof(nums_2[0]);
    return_size     = 2;

    int *my_output_2 = twoSum(nums_2, nums_size, target, &return_size);
    TEST_ASSERT(  my_output_2[0] == output_2[0]);
    TEST_ASSERT(  my_output_2[1] == output_2[1]);
    
    free(my_output_2);
}