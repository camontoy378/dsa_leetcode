#include <stdio.h>
#include <make_tree.c>

int max(int a, int b)
{
    if (a > b)
    {
        return a;
    }
    else
    {
        return b;
    }
}

int search_max_depth(struct Node* root)
{
    //Base case
    if (root == NULL)
    {
        return 0;
    }

    //Call recursively
    int max_left    = search_max_depth(root->left);
    int max_right   = search_max_depth(root->right);

    return max(max_left, max_right) + 1;
}

int solve(int arr[], int array_size)
{
    struct Node* root = get_tree_root(arr, array_size);
    
    return search_max_depth(root);
}