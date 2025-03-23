#include <make_tree.h>

/*************************************************************************/
//
/*************************************************************************/ 
struct Node
{
    int val;
    struct Node *left;
    struct Node *right;
};


/*************************************************************************/
//
/*************************************************************************/
struct Node* create_node( int value)
{
    struct Node* new_node = (struct Node*) malloc (sizeof (struct Node) );
    new_node->val   = value;
    new_node->left  = NULL;
    new_node->right = NULL; 
};

/*************************************************************************/
//
/*************************************************************************/

struct Node* get_tree_root(int array[], int array_size)
{
    int array_index_0   = 0;

    return insert_level_order(array_index_0, array_size, array);
};


/*************************************************************************/
//
/*************************************************************************/
struct Node* insert_level_order(int i, int n, int array[])
{
    struct Node* root = NULL;

    //Base Case
    if (i < n && array[i] != '\0')
    {    
        root        = create_node(array[i]);

        root->left  = insert_level_order(2 * i + 1, n, array);
        root->right = insert_level_order(2 * i + 2, n, array);
    }

    return root;
}