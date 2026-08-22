#include <stdio.h>

#define TRUE 0
#define FALSE 1


int firstMissingPositive(int* nums, int numsSize){

    //Init
    int found;
    int num_needed = 1;
    int tmp;
    int i;
    int j;


    for(i = 0; i < numsSize; i++){

        printf("DEBUG_01: i = %d\n", i);
        printf("DEBUG_02: nums[i] = %d\n", nums[i]);
        
        found = FALSE;

        for(j = i; j < numsSize; j++){

            if(num_needed == nums[j]){
                //swap
                tmp     = nums[i];
                nums[i] = nums[j];
                nums[j] = tmp;
                found   = TRUE;
                num_needed++;
                break; 
            }
        }
        
        if(found == FALSE){
            return num_needed;
        }

    }

    return num_needed;
}

int main(){
    printf("At Main\n");

    //Test 1
    //int nums[]      = {1,2,0};
    //int output      = 3;
    //int nums_size   = sizeof(nums) / sizeof(nums[0]); 

    //Test 2
    //int nums[]      = {3,4,-1,1};
    //int output      = 1;
    //int nums_size   = sizeof(nums) / sizeof(nums[0]); 

    //Test 3
    int nums[]      = {7,8,9,11,12};
    int output      = 1;
    int nums_size   = sizeof(nums) / sizeof(nums[0]); 

    output = firstMissingPositive(nums, nums_size);

    printf("Output = %d\n", output);

    return 0;
}