#include <unity.h>
#include "lc_509_fibonacci.c"

void startUp(){
    //
}

void tearDown(){
    //
}

void test_fib(){
    //Test 1
    int n       = 2;
    int output  = 1;

    TEST_ASSERT( fib(n) == output );

    //Test 2
    n           = 3;
    output      = 2;

    TEST_ASSERT( fib(n) == output );

    //Test 1
    n           = 4;
    output      = 3;

    TEST_ASSERT( fib(n) == output );
}