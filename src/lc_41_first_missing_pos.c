#include <stdio.h>

#define TRUE 0
#define FALSE 1

void swap(int* arr, int i, int j){
    int tmp = arr[i];
    arr[i]  = arr[j];
    arr[j]  = tmp;
}

void print_array(int* arr, int arr_size){

    int i = 0;
    for(i; i < arr_size; i++){
        printf("%d, ", arr[i]);
    }
    printf("\n");
}

int qs_arr(int* arr, int i, int j){
    
    int pivot = i;

    while (j >= i){

        if ( (arr[i] > arr[pivot]) && (arr[j] <= arr[pivot]) ){
            swap(arr, i, j);
        }

        if ( arr[i] <= arr[pivot]){
            i++;
        }

        if (arr[j] > arr[pivot]){
            j--;
        }
    }

    swap(arr, j, pivot);

    return j;
}

void quicksort(int* arr, int i, int j ){
    
    int pivot;

    if (i >= j){
        return;
    }

    pivot = qs_arr(arr, i, j);

    quicksort(arr, i, pivot - 1);
    quicksort(arr, pivot + 1, j);
}

int firstMissingPositive(int* nums, int numsSize){

    //Init
    int found;
    int num_needed = 1;
    int tmp;
    int i;
    int j;

    i = 0;
    j = numsSize - 1;

    print_array(nums, numsSize);
    quicksort(nums, i, j);
    print_array(nums, numsSize);

    //Find 1
    while (i < numsSize){
        if ( nums[i] == num_needed){
            break;
        }
        i++;
    }

    if (i >= numsSize){
        return num_needed;
    }

    //Find missing positive
    while (nums[i] == num_needed)
    {
        i++;
        num_needed++;
    }

    return num_needed;
}

int main(){
    printf("At Main\n");

    //Test 1
    int nums[]      = {1,2,0};
    int output      = 3;
    int nums_size   = sizeof(nums) / sizeof(nums[0]); 

    //Test 2
    //int nums[]      = {3,4,-1,1};
    //int output      = 2;
    //int nums_size   = sizeof(nums) / sizeof(nums[0]); 

    //Test 3
    //int nums[]      = {7,8,9,11,12};
    //int nums[]      = {11,12,7,8,9};
    //int output      = 1;
    //int nums_size   = sizeof(nums) / sizeof(nums[0]); 

    output = firstMissingPositive(nums, nums_size);

    printf("Output = %d\n", output);

    return 0;
}