#include <iostream>
#include <vector>

using namespace std;

/**
 * Definition for singly-linked list.
 */
 struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

class ll{
public:
    ListNode *head = nullptr;

    void add_node(int value){
        
        ListNode *temp = new ListNode(value);
          
        if(head == nullptr){
            head = temp;
        }
        else{
            
            ListNode *tail = head;

            while(tail->next != nullptr){
                tail = tail->next;
            }

            tail->next = temp;

        }        
    }

 };

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        ll my_output = ll();
        
        int sum = 0;
        int carry = 0;
        ListNode *ptr1 = l1;
        ListNode *ptr2 = l2;

        while( (ptr1 != nullptr) || (ptr2 != nullptr)){
            
            sum += carry;

            if(ptr1 != nullptr){
                sum += ptr1->val;
                
                ptr1 = ptr1->next;
            }
            if(ptr2 != nullptr){
                sum += ptr2->val;
                
                ptr2 = ptr2->next;
            }


            if(sum > 9){
                carry = 1;
                sum = sum % 10;
                my_output.add_node(sum);
            }
            else{
                carry = 0;
                my_output.add_node(sum);
            }


            sum = 0;
        }

        if(carry == 1){
            my_output.add_node(carry);
        }

        return my_output.head;
    }
};
