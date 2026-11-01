#include <iostream>

#include <algorithm>
#include <cmath>
#include <queue>
#include <vector>

using std::cout;
using std::min;
using std::pow;
using std::queue;
using std::vector;


class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {

        int output_min  = pow(10,5) + 1;
        int cur_sum     = 0;

        queue<int> q;

        //Process
        for(const int& num : nums){

            cur_sum += num;
            q.push(num);

            //Meets target?
            while(cur_sum >= target){
                output_min = min(output_min, static_cast<int>( q.size() ) );

                //Remove earliest value
                cur_sum -= q.front();
                q.pop();
            }
        }
        
        if(output_min  == (pow(10,5) + 1) ){
            return 0;
        }
        else{
            return output_min;
        } 
        
    }
};
