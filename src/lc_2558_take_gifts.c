#include "heap.c"
#include <math.h>

int pickGifts(int* gifts_array, int size_gifts_array, int k)
{
    int max_num = 0;
    int square_root;
    int total_gifts = 0;

    heapify_max(gifts_array, &size_gifts_array);
    
    for (int i = 0; i < k; i++)
    {
        max_num = heap_pop(gifts_array, &size_gifts_array);

        square_root = sqrt(max_num);

        heap_push(gifts_array, &size_gifts_array, square_root);

    }

    while (size_gifts_array > 0)
    {
        total_gifts += heap_pop(gifts_array, &size_gifts_array);

    }

    printf("Total gifts = %d\n", total_gifts);    

    return total_gifts;
}
