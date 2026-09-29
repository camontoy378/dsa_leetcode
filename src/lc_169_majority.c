#include <stdlib.h>

int compare(const void *a, const void *b  ){

    return (*(int*)a - *(int*)b);
}

int majorityElement(int* nums, int numsSize) {
    
    //Sort
    qsort(nums, numsSize, sizeof(nums[0]), compare);

    //Set frequency threshold
    int freq_th         = numsSize / 2;
    int num_elements    = 0;
    int current_element = nums[0];
    int i;

    //Search 
    for(i = 0; i < numsSize; i++){

        if(nums[i] == current_element){
            num_elements++;
        }
        else{
            current_element = nums[i];
            num_elements    = 1;
        }

        if(num_elements > freq_th){
            return current_element;
        }
    }

    return current_element;
    
}