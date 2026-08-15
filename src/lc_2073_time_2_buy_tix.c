#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100
#define FALSE 0
#define TRUE 1

typedef struct{
    int q_arr[MAX_SIZE];
    int front;
    int back;
    int num_elements;
}Queue;

int is_q_empty(Queue* q){

    if ( q->num_elements <= 0 ){
        return TRUE;
    }
    else{
        return FALSE;
    }
}

int is_q_full(Queue* q){
    if ( q->num_elements >= MAX_SIZE){
        return TRUE;
    }
    else{
        return FALSE;
    }
}

void initialize_q(Queue* q){
    q->front        = 0;
    q->back         = 0;
    q->num_elements = 0;
}

void push_q(Queue* q, int value){
    if (is_q_full(q)){
        printf("Queue is full...\n");
        return;
    }
    else{
        q->q_arr[q->back] = value;
        q->back = (q->back + 1) % MAX_SIZE;
        q->num_elements++;
    }
}

int pop_q(Queue* q){
    if (is_q_empty(q)){
        printf("Queue is empty...\n");
        return -1;
    }
    else{
        //Pop
        int val = q->q_arr[q->front];
        q->front = ( q->front + 1) % MAX_SIZE;
        q->num_elements--;

        return val;
    }
}


int time_required_to_buy(int* tickets, int ticket_size, int k){

    Queue q;

    initialize_q(&q);

    //Initialize q array
    int i = 0;
    for (i; i < ticket_size; i++){
        push_q(&q, i);
    }

    int ticket_index    = 0;
    int count           = 0;

    while (! is_q_empty(&q)){

        ticket_index = pop_q(&q);

        //Process ticket
        tickets[ticket_index] -= 1;
        count++;

        //Test for k
        if (tickets[ticket_index] == 0){
            if (ticket_index == k){
                return count;
            }
        }
        else{
            push_q(&q, ticket_index);
        }
    }

    return count;

}


int main(void){

    //Test 1
    int tickets[]   = {2,3,2};
    int k           = 2;
    int output      = 6;

    //Test 2
    //int tickets[]       = {5,1,1,1};
    //int k               = 0;
    //int output          = 8;

    int ticket_size     = sizeof(tickets)/sizeof(tickets[0]);

    int time_2_buy = time_required_to_buy(tickets, ticket_size, k);

    printf("Time to buy = %d\n", time_2_buy);

    return 0;
}