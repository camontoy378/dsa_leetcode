#include <stdio.h>
#include <stdlib.h>

#include <time.h>

void heapify_recurse(int* array, int root_index, int* ptr_array_size);
void print_array_values(int* array, int* array_size);
void swap_values(int* array, int index1, int index2);

/*************************************************************************/
//
/*************************************************************************/
int heap_pop(int* array, int* ptr_array_size)
{
    int root_value;

    root_value = array[0];

    *ptr_array_size -= 1;

    int last_element_index = *ptr_array_size;

    array[0] = array[last_element_index];

    heapify_recurse(array, 0, ptr_array_size);

    return root_value;
}

/*************************************************************************/
// Check for array size max?
/*************************************************************************/
void heap_push(int* array, int* ptr_array_size, int value_to_push)
{
    int first_free_loc_in_array_index = *ptr_array_size;
    
    array[first_free_loc_in_array_index] = value_to_push;

    *ptr_array_size += 1;
    
    
    for (first_free_loc_in_array_index; first_free_loc_in_array_index >= 0; first_free_loc_in_array_index = first_free_loc_in_array_index / 2 )
    {
        heapify_recurse(array, first_free_loc_in_array_index, ptr_array_size);

        if (first_free_loc_in_array_index == 0)
        {
            break;
        }

    }

}



/*************************************************************************/
//
/*************************************************************************/
void heapify_max(int* array, int* ptr_array_size)
{
    for (int i = *ptr_array_size - 1; i >= 0; i--)
    {
        heapify_recurse(array, i, ptr_array_size);
    }
}

/*************************************************************************/
//
/*************************************************************************/
void heapify_recurse(int* array, int root_index, int* ptr_array_size)
{
    int index_child_max_value   =     root_index;
    int index_left_child        = 2 * root_index + 1;
    int index_right_child       = 2 * root_index + 2;

    //Base condition
    if (index_left_child > *ptr_array_size)
    {
        return;
    }

    //Some pre-work
    if ( index_left_child < *ptr_array_size && array[index_left_child] > array[index_child_max_value] )
    {
        index_child_max_value = index_left_child;
    }

    if ( index_right_child < *ptr_array_size && array[index_right_child] > array[index_child_max_value] )
    {
        index_child_max_value = index_right_child;
    }

    //Swap and recurse only if changes are made.
    if ( index_child_max_value != root_index )
    {
        swap_values(array, root_index, index_child_max_value);
        
        //recursion
        heapify_recurse(array, index_child_max_value, ptr_array_size);
    }
}

/*************************************************************************/
//
/*************************************************************************/
void print_array_values(int* array, int* array_size)
{
    printf("\n\n**** Print Array Values *****\n");
    for (int i = 0; i < *array_size; i++)
    {
        printf("array[%d] = %d\n", i, array[i]);
    }
}

/*************************************************************************/
//
/*************************************************************************/
void swap_values(int* array, int index1, int index2)
{
    int temp_val;

    temp_val        = array[index1];
    array[index1]   = array[index2];
    array[index2]   = temp_val;

}


//create heap
/*
int main()
{
    int input[8]            = {50,30,20,15,10,8,16};
    int array_size_max      = sizeof(input) / sizeof(int);
    int item_to_push        = 60;

    int current_array_size  = array_size_max - 1;


    heap_push(input, &current_array_size, item_to_push);

    return 0;

}
*/