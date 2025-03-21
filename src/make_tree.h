#include <stdio.h>
#include <stdlib.h>

struct Node* create_node( int value);
struct Node* insert_level_order(int i, int n, int array[]);
struct Node* get_tree_root(int array[], int array_size);
