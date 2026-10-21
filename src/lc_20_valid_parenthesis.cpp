#include <iostream>
#include <unordered_map>
#include <stack>

using std::string;
using std::cout;
using std::unordered_map;
using std::stack;


class Solution{
public:

    unordered_map <char, char> par_map;
    stack<char> my_stack;

    Solution(){
        par_map[')'] = '(';
        par_map['}'] = '{';
        par_map[']'] = '[';
    }

    void empty_stack(void){
        my_stack = {};
    }
    

    bool isValid(string s){

        int i = 0;

        for(i; i < s.size(); i++){
            
            if( my_stack.empty() != true){
                
                //Matching parenthesis?
                if( my_stack.top() == par_map[s[i]] ){
                    
                    my_stack.pop();
                }
                else{
                    my_stack.push(s[i]);
                }
            }
            else{
                my_stack.push(s[i]);
            }
        }

        if(my_stack.empty()){
            return true;
        }
        else{
            return false;
        }
    }

};