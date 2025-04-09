#include <unity.h>
#include "lc_346_mov_avg.c"


void setUp()
{

}

void tearDown()
{

}

void test_MovingAverageCreate()
{
    //Test 1
    int input[] = {3,1,10,3,5};

    struct MovingAverage* my_ma = movingAverageCreate(input[0]);

    TEST_ASSERT (movingAverageNext(my_ma, input[1]) == 1.0);
    TEST_ASSERT (movingAverageNext(my_ma, input[2]) == 5.5);
    TEST_ASSERT (movingAverageNext(my_ma, input[3]) == 4.666666666666667);
    TEST_ASSERT (movingAverageNext(my_ma, input[4]) == 6.0);

}
