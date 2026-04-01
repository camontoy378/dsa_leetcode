#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void initialize_array(int* array, int array_size, int value)
{
    for (int i = 0; i < array_size; i++)
    {
        array[i] = value;
    }
}

int num_ways_climb_stairs(int steps, int* p_track_steps)
{
    //Stop conditions

    if (p_track_steps[steps] != -1)
    {
        return p_track_steps[steps];
    }

    if (steps <= 2)
    {
        p_track_steps[steps] = steps;
        return p_track_steps[steps];
    }

    //Work and recursion

    return num_ways_climb_stairs(steps - 1, p_track_steps) + num_ways_climb_stairs(steps - 2, p_track_steps);
}


int solve(int steps)
{
    int array_size = steps + 1;

    int track_steps[array_size];

    initialize_array(track_steps, array_size, -1);

    return num_ways_climb_stairs(steps, track_steps);

}

int main(void)
{
    int n = 5;

    printf("At main\n");

    int num_way = solve(n);

    printf("Num ways to climb stairs = %d\n", num_way);

    return 0;
}