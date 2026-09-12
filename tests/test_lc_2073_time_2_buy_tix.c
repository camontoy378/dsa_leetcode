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
    int tickets[]       = {2,3,2};
    int k               = 2;
    int output          = 6;

    int ticket_size     = sizeof(tickets)/sizeof(tickets[0]);

    TEST_ASSERT(time_required_to_buy(tickets, ticket_size, k) == output);

    //Test 2
    int tickets_2[]     = {5,1,1,1};
    k                   = 0;
    output              = 8;

    ticket_size         = sizeof(tickets_2)/sizeof(tickets_2[0]);

    printf("DEBUG: output = %d", output);

    TEST_ASSERT(time_required_to_buy(tickets_2, ticket_size, k) == output);


}