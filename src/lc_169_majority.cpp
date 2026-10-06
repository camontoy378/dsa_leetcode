#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;

class Solution {
public:
    int majorityElement(vector<int>& nums) {

        //Get threshold number
        int freq_threshold = nums.size() / 2 ;

        //Sort array
        std::sort(nums.begin(), nums.end());

        int i               = 0;
        int num_elements    = 0;
        int current_element = nums[0];

        for (i; i < nums.size(); i++ ){
            if(nums[i] == current_element){
                num_elements++;
            }
            else{
                current_element = nums[i];
                num_elements    = 1;
            } 
            
            if(num_elements > freq_threshold){
                return current_element;
            }
        }

        return num_elements;
        
    }
};

void my_assert(int input1, int input2){
    if( input1 == input2){
        std::cout << "Majority element = " << input1 << std::endl;
    }
    else{
        std::cout << "Majority element NOT found!" << std::endl;
    }
}

int main(void){

    std::cout << "At main() ..." << std::endl;

    int result;

    //Test 1
    std::vector<int> nums   = {3,2,3};
    int output              = 3;

    Solution solution;

    result = solution.majorityElement(nums);
    my_assert(result,output);

    //Test 1
    std::vector<int> nums_2 = {2,2,1,1,1,2,2};
    output                  = 2;

    result = solution.majorityElement(nums_2);
    my_assert(result,output);


    return 0;
}