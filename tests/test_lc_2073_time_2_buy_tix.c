#include <unity.h>
#include "lc_2073_time_2_buy_tix.c"

void setUp()
{
    //
}

void tearDown()
{
    //
}

void test_time_required_to_buy()
{
    //Test 1
    int tickets[] = {2,3,2};
    int k = 2;
    int output = 6;

    int ticket_size     = sizeof(tickets)/sizeof(tickets[0]);

    TEST_ASSERT(time_required_to_buy(tickets, ticket_size, k) == output);


}