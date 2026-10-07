#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {

    int* output = (int*) malloc(sizeof(int) * 2);

    output[0]   = -1;
    output[1]   = -1;

    int i,j;

    //Find 2 Sum
    for(i = 0; i < numsSize; i++){

        j = i + 1;
        for(j; j < numsSize; j++ ){
            
            if( (nums[i] + nums[j]) == target){
                output[0]   = i;
                output[1]   = j;
                *returnSize = 2;
            }
        }
    }

    return output;
    
}