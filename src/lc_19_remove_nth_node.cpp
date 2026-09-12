#include <iostream>

struct ListNode{
    int val;
    ListNode* next;
};


class Solution{
    
public:

    ListNode* remove_nth_node(ListNode* head, int nth_node){

        ListNode* prev  = nullptr;
        ListNode* cur   = head;
        int i = 1;

        //Position pointers
        for(i; (cur != nullptr) && (i < nth_node); i++){
            prev    = cur;
            cur     = cur->next;
        }

        //Remove
        if(prev == nullptr){
            prev = cur->next;
            head = prev;
        }
        else{
            prev->next = cur->next;
        }

        //Free memory
        if(cur == nullptr){
            return head;
        }
        else{
            delete cur;
            cur = nullptr;
        }

        return head;

    }

    ListNode* removeNthFromEnd(ListNode* head, int n){
        int nth_node;
        int num_nodes = 0;

        //Count total nodes
        ListNode* tmp = head;
        while(tmp != nullptr){
            num_nodes++;
            tmp = tmp->next;
        }

        //Get nth_node to remove
        nth_node = num_nodes - n + 1;
        
        head = remove_nth_node(head, nth_node);
        
        return head;
    }
};

int main(void){

    std::cout << "This is main()" << std::endl;

    return 0;
}