#include <iostream>

#define MAX_SIZE_Q 100

class Queue{
    public:
        int q[MAX_SIZE_Q];
        int index_front;
        int index_back;
        int elements_in_q;

        bool is_empty(){

            if (elements_in_q <= 0){
                return true;
            }
            else{
                return false;
            }
        }

        bool is_full(){
            if (elements_in_q >= MAX_SIZE_Q){
                return true;
            }
            else{
                return false;
            }            
        }

        void push(int value){
            if (is_full()){
                std::cout << "Queue is full...\n";
            }
            else{
                q[index_back]   = value;
                index_back      = (index_back + 1) % MAX_SIZE_Q;
                elements_in_q++; 
            }
        }

        int pop(){

            if (is_empty()){
                std::cout << "Queue is empty...\n";
                return -1;
            }
            else{
                int val = q[index_front];

                index_front = (index_front + 1) % MAX_SIZE_Q;
                elements_in_q--;

                return val;
            }

        }

        Queue(){
            index_front     = 0;
            index_back      = 0;
            elements_in_q   = 0;
        }
};

class Solution{
public:
    //int timeRequiredToBuy(vector<int>& tickets, int k){
    int timeRequiredToBuy(int* tickets, int ticket_size, int k){
        
        //Make instance of Q
        Queue q = Queue();

        //int ticket_size = tickets.size();

        //Init Q
        int i = 0;
        for (i; i < ticket_size; i++){
            q.push(i);
        }

        int ticket_index    = 0;
        int count           = 0;

        while (! q.is_empty()){
            
            ticket_index = q.pop();

            //Process ticket
            tickets[ticket_index]--;
            count++;

            //Test for k
            if (tickets[ticket_index] == 0){
                if (ticket_index == k){
                    return count;
                }
            }
            else{
                q.push(ticket_index);
            }
        }

        return count;
    }

};

int main(){
    std::cout << "At main()\n";

    //Test 1
    //int tickets[]       = {2,3,2};
    //int k               = 2;
    //int output          = 6;

    //Test 2
    int tickets[]       = {5,1,1,1};
    int k               = 0;
    int output          = 8;




    int ticket_size     = sizeof(tickets)/sizeof(tickets[0]);

    Solution solution = Solution();

    int time_2_buy  = solution.timeRequiredToBuy(tickets, ticket_size, k);

    std::cout << "Time to buy is = " << time_2_buy << std::endl;    

    return 0;
}