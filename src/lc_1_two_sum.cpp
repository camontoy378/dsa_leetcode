#include <iostream>
#include <vector>
#include <unordered_map>

using std::vector; 
using std::cout;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        std::unordered_map< int, int> arr_hash;
        vector<int> output;
        int index = 0;
        int current_num;
        int needed_num;
        int value;

        for(index; index < nums.size(); index++ ){

            current_num = nums[index];
            needed_num  = target - current_num;

            cout << current_num << "\n";

            if ( arr_hash.find(needed_num) == arr_hash.end()){
                arr_hash[current_num] = index;
            }
            else{
                auto value = arr_hash.find(needed_num);
                output.push_back( value->second );
                output.push_back(index);
                return output;
            }

            
        }
        cout << std::endl;

        return {0,0};
    }
};