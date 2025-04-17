#include <unity.h>
#include "heap.c"

void setUp()
{
    printf("Set up Heap test");

}

void tearDown()
{

}

void test_heap_pop()
{
    int input[]     = {50,30,20,15,10,8,16};
    int array_size  = sizeof(input) / sizeof(int);

    int result = heap_pop(input, &array_size);

    TEST_ASSERT (result == 50);
    TEST_ASSERT (array_size == 6);

    result = heap_pop(input, &array_size);

    TEST_ASSERT (result == 30);
    TEST_ASSERT (array_size == 5);

}

void test_heap_push()
{
    int input[8]            = {50,30,20,15,10,8,16};
    int array_size_max      = sizeof(input) / sizeof(int);
    int item_to_push        = 60;

    int current_array_size  = array_size_max - 1;


    heap_push(input, &current_array_size, item_to_push);

    TEST_ASSERT (input[7] == 15);
    TEST_ASSERT (input[6] == 16);
    TEST_ASSERT (input[5] == 8);
    TEST_ASSERT (input[4] == 10);
    TEST_ASSERT (input[3] == 30);
    TEST_ASSERT (input[2] == 20);
    TEST_ASSERT (input[1] == 50);
    TEST_ASSERT (input[0] == 60);
    
}