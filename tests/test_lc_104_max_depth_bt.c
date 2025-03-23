#include <unity.h>
#include <lc_104_max_depth_bt.c>

void setUp()
{

}

void tearDown()
{

}

void test_solve()
{
    //Test 1
    int input[] = {1,2,3};
    int array_size = sizeof(input)/sizeof(input[0]);
    
    TEST_ASSERT( solve(input, array_size) == 2 );

    //Test 2
    int input_2[] = {1};
    int array_size_2 = sizeof(input_2)/sizeof(input_2[0]);
    
    TEST_ASSERT( solve(input_2, array_size_2) == 1 );

    //Test 3
    int input_3[] = {3,9,20,'\0','\0',15,7};
    int array_size_3 = sizeof(input_3)/sizeof(input_3[0]);
    
    TEST_ASSERT( solve(input_3, array_size_3) == 3 );

    //Test 4
    int input_4[] = {1,'\0',2};
    int array_size_4 = sizeof(input_4)/sizeof(input_4[0]);
    
    TEST_ASSERT( solve(input_4, array_size_4) == 2 );
}