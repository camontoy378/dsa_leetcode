#include <stdio.h>
#include <stdlib.h>

struct ListNode{
    int val;
    struct ListNode* next;
};

struct ListNode* insert(struct ListNode* head, int val)
{
    //Create Node
    struct ListNode* tmp = (struct ListNode*) malloc(sizeof(struct ListNode));

    //Init Node
    tmp->val    = val;
    tmp->next   = NULL;

    //Position ptr
    struct ListNode* tail = head;

    if(head == NULL){
        head = tmp;
    }
    else{
        while(tail->next != NULL){
            tail = tail->next;
        }

        tail->next = tmp;
    }

    return head;
};

struct ListNode* create_ll(int* arr, int arr_size, struct ListNode* head){

    int i = 0;

    for(i; i < arr_size; i++){
        
        head = insert(head, arr[i]);
    }

    return head;
}

void print_ll(struct ListNode* head){

    struct ListNode* tmp = head;

    while(tmp != NULL){
        printf("%d, ", tmp->val);
        tmp = tmp->next;
    }

    printf("\n");
}

//Delete nth Node. nth_node = 1 for first node
struct ListNode* delete_nth_node(struct ListNode* head, int nth_node){

    int i = 1;

    struct ListNode *prev, *cur;

    prev    = NULL;
    cur     = head;

    printf("nth_node = %d\n", nth_node);

    for(i; (cur != NULL) && (i < nth_node); i++){
        prev    = cur;
        cur     = cur->next;
    }

    if(cur == NULL){
        printf("Cannot delete node!  Nth node out of bounds...\n");
        return head;
    }

    if(prev == NULL){
        prev = cur->next;
        head = prev;

        if(head == NULL){
            printf("LL is empty...\n");
        }
    }
    else{
        prev->next = cur->next;
    }

    free(cur);

    return head;
}

struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    
    int nth_node;
    struct ListNode* tmp = head;
    
    //Find number of elements in linked list
    int num_elements = 0;

    while(tmp != NULL){
        tmp = tmp->next;
        num_elements++;
    }

    nth_node = num_elements - n + 1;

    head = delete_nth_node(head, nth_node);
    
    return head;
}

int main(void){

    //Test 1
    /*
    int arr[]       = {1,2,3,4,5};
    int n           = 2;
    int out[]       = {1,2,3,5};
    */

    //Test 2
    //int arr[]       = {1};
    //int n           = 1;
    //int out[]       = {};

    //Test 3
    int arr[]       = {1,2};
    int n           = 1;
    int out[]       = {1};

    int arr_size    = sizeof(arr)/sizeof(arr[0]);
    
    struct ListNode* head = NULL;

    head = create_ll(arr, arr_size, head);

    print_ll(head);

    head = removeNthFromEnd(head, n);

    print_ll(head);

    return 0;
}