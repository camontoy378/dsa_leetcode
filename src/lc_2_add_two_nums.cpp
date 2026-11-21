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

int main(){

    cout << "At main()...\n";

    //Test 1
    vector<int> l1      = {2,4,3};
    vector<int> l2      = {5,6,4};
    vector<int> output  = {7,0,8};

    ll my_l1 = ll();
    my_l1.create_ll(l1);
    my_l1.print_ll();

    ll my_l2 = ll();
    my_l2.create_ll(l2);
    my_l2.print_ll();

    cout << "Test 1\n";
    Solution ret_output = Solution();
    ret_output.addTwoNumbers(my_l1.head, my_l2.head);

    //Test 2
    vector<int> l1_2    = {0};
    vector<int> l2_2    = {0};

    ll my_l1_2 = ll();
    my_l1_2.create_ll(l1_2);
    my_l1_2.print_ll();

    ll my_l2_2 = ll();
    my_l2_2.create_ll(l2_2);
    my_l2_2.print_ll();

    cout << "Test 2\n";
    ret_output.addTwoNumbers(my_l1_2.head, my_l2_2.head);

    //Test 3
    vector<int> l1_3    = {9,9,9,9,9,9,9};
    vector<int> l2_3    = {9,9,9,9};

    ll my_l1_3 = ll();
    my_l1_3.create_ll(l1_3);
    my_l1_3.print_ll();

    ll my_l2_3 = ll();
    my_l2_3.create_ll(l2_3);
    my_l2_3.print_ll();

    cout << "Test 2\n";
    ret_output.addTwoNumbers(my_l1_3.head, my_l2_3.head);

    return 0;
}