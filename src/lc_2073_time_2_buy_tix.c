#include <stdio.h>
#include <stdlib.h>


typedef struct Node{
    int num_tix;
    int k;
    struct Node* next;
}Node;

//Global
Node* head = NULL;

void add_new_node(int value, int k){

    //Create new node
    Node* ptr_new_node      = (Node*) malloc(sizeof(Node));
    ptr_new_node->num_tix   = value;
    ptr_new_node->k         = k;
    ptr_new_node->next      = NULL;

    //Add node to ll
    if (head == NULL){
        head = ptr_new_node;
    }
    else{
        Node* tmp = head;

        while(tmp->next != NULL){
            tmp = tmp->next;
        }

        tmp->next = ptr_new_node;
    }
}

void create_linked_list(int* ptr_array, int array_size){
    
    int i = 0;
    for (i; i < array_size; i++){
        add_new_node(ptr_array[i], i);
    }
}

void print_linked_list(void){
    Node* tmp;
    tmp = head;

    while(tmp != NULL){
        printf("Num tix = %d\n", tmp->num_tix);
        tmp = tmp->next;
    }
}
//Create function to remove and element
void remove_node(Node* ptr_cur){

    if (ptr_cur == head){
        head = ptr_cur->next;
    }
    else{

        Node* ptr_prev = head;
        while(ptr_prev->next != ptr_cur){
            ptr_prev = ptr_prev->next;
        }

        ptr_prev->next = ptr_cur->next;
    }

    free(ptr_cur);
}

int time_required_to_buy(int* tickets, int ticket_size, int k){
    
    create_linked_list(tickets, ticket_size);
    //print_linked_list();

    int time_2_buy  = 0;
    Node* tmp       = head;
    Node* rm_node;

    while (head != NULL){
        
        tmp->num_tix--;
        time_2_buy++;
        printf("Num_tix = %d", tmp->num_tix);
        printf(" time_2_buy = %d\n", time_2_buy);

        if(tmp->num_tix == 0){
            if(tmp->k == k){
                return time_2_buy;
            }
            else{
                rm_node = tmp;
                tmp = tmp->next;
                remove_node(rm_node);
            }
        }
        else{
            tmp = tmp->next;
        }
        
        if (tmp == NULL){
            tmp = head;
        }
    }

    return 0;
}

//Create main.
int main(void){

    //Test 1
    //int tickets[]   = {2,3,2};
    //int k           = 2;
    //int output      = 6;

    //Test 2
    int tickets[]       = {5,1,1,1};
    int k               = 0;
    int output          = 8;

    int ticket_size     = sizeof(tickets)/sizeof(tickets[0]);

    int time_2_buy = time_required_to_buy(tickets, ticket_size, k);

    printf("Time to buy = %d", time_2_buy);

    return 0;
}