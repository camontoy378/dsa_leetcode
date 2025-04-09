#include <stdio.h>
#include <stdlib.h>

void heapify_recurse(int* array, int root_index, int array_size);
void print_array_values(int* array, int array_size);
void swap_values(int* array, int index1, int index2);


void heapify_max(int* array, int array_size)
{
    for (int i = array_size - 1; i >= 0; i--)
    {
        heapify_recurse(array, i, array_size);
    }
}

void heapify_recurse(int* array, int root_index, int array_size)
{
    int index_child_max_value   =     root_index;
    int index_left_child        = 2 * root_index + 1;
    int index_right_child       = 2 * root_index + 2;

    //Base condition
    if (index_left_child > array_size)
    {
        return;
    }

    //Some pre-work
    if ( index_left_child < array_size && array[index_left_child] > array[index_child_max_value] )
    {
        index_child_max_value = index_left_child;
    }

    if ( index_right_child < array_size && array[index_right_child] > array[index_child_max_value] )
    {
        index_child_max_value = index_right_child;
    }

    //Swap and recurse only if changes are made.
    if ( index_child_max_value != root_index )
    {
        swap_values(array, root_index, index_child_max_value);
        
        //recursion
        heapify_recurse(array, index_child_max_value, array_size);
    }
}

void print_array_values(int* array, int array_size)
{
    for (int i = 0; i < array_size; i++)
    {
        printf("array[%d] = %d\n", i, array[i]);
    }
}
void swap_values(int* array, int index1, int index2)
{
    int temp_val;

    temp_val        = array[index1];
    array[index1]   = array[index2];
    array[index2]   = temp_val;

}
//heapop
//heapush
//create heap


int main()
{
    int array[] = {10,20,15, 12, 40, 25, 18};
    int size    = sizeof(array)/sizeof(array[0]);
    
    printf("Size of array = %d\n", size);
    
    heapify_max(array, size);

    print_array_values(array, size);

    return 0;
}