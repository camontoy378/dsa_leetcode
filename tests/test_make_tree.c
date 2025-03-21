#include "unity.h"
#include <make_tree.c>


void setUp()
{
    printf("Set up");

}

void tearDown()
{
    printf("\nTear down");
}

void test_make_tree()
{


    int input[]         = {9, 8, 7, 6, 5, 6, 6, 6, 6};
    int array_size      = sizeof(input)/sizeof(input[0]);

    struct Node* root   = get_tree_root(input, array_size);

    TEST_ASSERT( root->val == 9 );
    TEST_ASSERT( root->left->val == 8 );
    TEST_ASSERT( root->right->val == 7);


    int input_2[3]      = {1, 2, 3};
    int array_size_2    = sizeof(input_2)/sizeof(input_2[0]);

    struct Node* root_2   = get_tree_root(input_2, array_size_2);

    TEST_ASSERT( root_2->val == 1 );
    TEST_ASSERT( root_2->left->val == 2 );
    TEST_ASSERT( root_2->right->val == 3);
}