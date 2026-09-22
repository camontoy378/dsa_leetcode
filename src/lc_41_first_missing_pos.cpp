#include <iostream>
#include <vector>


class Solution{
public:
    int firstMissingPositive(std::vector<int>& nums){
        
        int hash_array_size = nums.size() + 1;

        //Array init to 0 by default
        std::vector<int> hash_array(hash_array_size);
        
        //Fill hash array
        int i;
        for(i = 0; i < nums.size(); i++){
            if( (nums[i] > 0) && ( nums[i] < hash_array_size)){
                hash_array[nums[i]] = 1;
            }
        }
        
        //Search for first missing positive
        i = 1;
        while (i < hash_array_size){
            if(hash_array[i] == 0){
                return i;
            }
            i++;
        }

        return i;
    }

};

void my_assert(int input1, int input2){
    if( input1 == input2){
        std::cout << "First missing positive = " << input1 << std::endl;
    }
    else{
        std::cout << "First missing positive NOT found!" << std::endl;
    }
}

int main(void){

    //Test 1
    std::vector<int> nums   = {1,2,0};
    int output              = 3;

    Solution fmp = Solution();
    
    int result = fmp.firstMissingPositive(nums);
    
    my_assert( result, output);

    //Test 2
    std::vector<int> nums2  = {3,4,-1,1};
    output                  = 2;
    
    result = fmp.firstMissingPositive(nums2);
    
    my_assert( result, output);

    //Test 3
    std::vector<int> nums3  = {7,8,9,11,12};
    output                  = 1;
    
    result = fmp.firstMissingPositive(nums3);
    
    my_assert( result, output);

    //Test 4
    std::vector<int> nums4  = {0,2,2,1,1};
    output                  = 3;
    
    result = fmp.firstMissingPositive(nums4);
    
    my_assert( result, output);



   
    return 1;
}