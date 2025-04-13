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