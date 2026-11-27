#include <stdio.h>
#include <stdlib.h>

/**
 * Definition for singly-linked list.
**/
 struct ListNode {
     int val;
     struct ListNode *next;
 };
 


struct ListNode* add_node(struct ListNode* head, int value){
    
    struct ListNode* tmp = (struct ListNode*) malloc(sizeof(struct ListNode));
    tmp->val    = value;
    tmp->next   = NULL;

    if(head == NULL){
        head = tmp;
        return head;
    }
    else{
        struct ListNode* tail = head;

        while(tail->next != NULL){
            tail = tail->next;
        }

        tail->next = tmp;
    }

    return head;
}

//Create Linked List
struct ListNode* create_ll(int *arr, int size_arr){
    
    struct ListNode* head = NULL; 

    int i = 0;

    for(i; i < size_arr; i++){
        head = add_node(head, arr[i]);
    }

    return head;
};

//Print Linked List
void print_ll(struct ListNode* head){
    struct ListNode* tail = head;
    
    while(tail != NULL){
        printf("%d, ", tail->val );
        tail = tail->next;
    }
    printf("\n\n");
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {

    struct ListNode* l1_tail = l1;
    struct ListNode* l2_tail = l2;

    struct ListNode* head_output = NULL; 

    int sum     = 0;
    int carry   = 0;

    while ( (l1_tail != NULL) || (l2_tail != NULL) ) {
        if (l1_tail != NULL)
        {
            sum += l1_tail->val + carry;
            carry = 0;
        }

        if (l2_tail != NULL)
        {
            sum += l2_tail->val + carry;
            carry = 0;
        }

        carry   = sum / 10;
        sum     = sum % 10;

        //Output
        head_output = add_node(head_output, sum); 

        //Reset sum
        sum = 0;

        //Next digits
        if (l1_tail != NULL){
            l1_tail = l1_tail->next;
        }

        if (l2_tail != NULL){
            l2_tail = l2_tail->next;
        }

        
    }

    if(carry){
        head_output = add_node(head_output, carry);
    }

    return head_output;
    
    
}