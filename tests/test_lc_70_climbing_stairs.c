#include <unity.h>
#include "lc_70_climbing_stairs.c"

void setup(void){
    //
}

void teardown(void){
    //
}

void test_solve(void){
    
    //Test 1
    int n       = 2;
    int output  = 2;

    TEST_ASSERT( solve(n) == output);


    //Test 2
    n           = 3;
    output      = 3;
    TEST_ASSERT( solve(n) == output);

}