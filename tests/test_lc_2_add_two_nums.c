#include <unity.h>
#include "lc_2_add_two_nums.c"

void startUp(void){
    //
}

void tearDown(void){
    //
}

void test_addTwoNumbers(void){

    //Test 1

    //Create l1 and l2 linked lists
    struct ListNode *head_l1        = NULL;
    struct ListNode *head_l2        = NULL;
    struct ListNode *head_output    = NULL;

    int l1[]        = {2,4,3};
    int size_l1     = sizeof(l1)/sizeof(l1[0]);
    
    int l2[]        = {5,6,4};
    int size_l2     = sizeof(l2)/sizeof(l2[0]);

    int output[]    = {7,0,8}; 
    
    head_l1 = create_ll(l1, size_l1);
    head_l2 = create_ll(l2, size_l2);
    
    head_output = addTwoNumbers(head_l1, head_l2);

    TEST_ASSERT(head_output->val == output[0]);
    TEST_ASSERT(head_output->next->val == output[1]);
    TEST_ASSERT(head_output->next->next->val == output[2]);

    free(head_l1);
    free(head_l2);
    free(head_output);

    //Test 2
    
    int l1_2[]      = {9,9,9,9,9,9,9};   
    int l2_2[]      = {9,9,9,9};

    size_l1         = sizeof(l1_2)/sizeof(l1_2[0]);
    size_l2         = sizeof(l2_2)/sizeof(l2_2[0]);
    
    int output_2[]  = {8,9,9,9,0,0,0,1}; 
    
    head_l1 = create_ll(l1_2, size_l1);
    head_l2 = create_ll(l2_2, size_l2);
    
    head_output = addTwoNumbers(head_l1, head_l2);

    TEST_ASSERT(head_output->val == output_2[0]);
    TEST_ASSERT(head_output->next->val == output_2[1]);
    TEST_ASSERT(head_output->next->next->val == output_2[2]);
}