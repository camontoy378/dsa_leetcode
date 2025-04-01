#include <stdio.h>
#include <stdlib.h>

struct MovingAverage 
{
    int index_counter;
    int max_size;
    int sum;
    int* array_ptr;
};


struct MovingAverage* movingAverageCreate(int size) {

    struct MovingAverage* temp = (struct MovingAverage*) malloc (sizeof(struct MovingAverage));

    
    temp->max_size      = size;
    temp->index_counter  = -1;
    temp->sum           = 0;
    temp->array_ptr     = (int*) malloc(sizeof(int) * temp->max_size);

    return temp;
    
}

double movingAverageNext(struct MovingAverage* obj, int val) {

    double moving_avg = 0.0;

    obj->index_counter += 1;

    //var use as circular pointer to index an array
    int index_counter = obj->index_counter % obj->max_size;

    if (obj->index_counter >= obj->max_size)
    {
        obj->sum = obj->sum - *(obj->array_ptr + index_counter) + val;

        *(obj->array_ptr + index_counter) = val;

        moving_avg = (double) obj->sum / obj->max_size; 
        
        return moving_avg;
    }
    else
    {
        *(obj->array_ptr + index_counter) = val;
        obj->sum += val;

        int num_items = obj->index_counter + 1;

        moving_avg = (double) obj->sum / num_items; 

        return moving_avg;
    }
    
    return moving_avg;
}

void movingAverageFree(struct MovingAverage* obj) {

    free(obj);
    
}

