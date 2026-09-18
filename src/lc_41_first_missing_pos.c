#include <stdio.h>
#include <stdlib.h>

void print_array(int* arr, int arr_size){

    int i = 0;
    for(i; i < arr_size; i++){
        printf("%d, ", arr[i]);
    }
    printf("\n");
}

int firstMissingPositive(int* nums, int numsSize){

    int i;
    int adj_i;
    int output = 1;

    //Set nums < 1 to 0.
    for( i = 0; i < numsSize; i++){
        if(nums[i] < 1){
            nums[i] = 0;
        }
    }

    //Mark sequential numbers found starting from 1.
    //Mark by making positive number a negative.
    for(i = 0; i < numsSize; i++){

        adj_i = abs(nums[i]) - 1;
        
        if( nums[i] == 0){
            continue;
        }
        else if( (adj_i < numsSize) && (nums[adj_i] == 0)){
            nums[adj_i] = abs(nums[i]) * -1;
        }
        else if (adj_i < numsSize) {
            //
            nums[adj_i] = abs(nums[adj_i]) * -1;
        }
    }

    //Find missing positive
    for(i = 0; i < numsSize; i++){
        
        if(nums[i] >= 0){
            return output;
        }
        output++;
    }

    return output;

}
