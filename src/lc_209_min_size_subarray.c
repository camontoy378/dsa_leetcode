#include <stdio.h>

#define MAX_SIZE_ARRAY 100000
#define MIN(a,b) ( (a < b) ? a : b )

int minSubArrayLen(int target, int* nums, int numsSize) 
{
    int output  = MAX_SIZE_ARRAY + 1;

    //Initialize
    int i = 0;
    int j = 0;
    int sum = nums[j];

    printf("Nums size array = %d\n", numsSize);

    while (j < numsSize)
    {
        if ( sum >= target)
        {
            output = MIN(output, (j - i + 1));

            if ( i == j)
            {
                i++;
                j++;
                if (j < numsSize)
                {
                    sum = nums[j];
                }
            }
            else
            {
                sum = sum - nums[i];
                i++;
            }
        }
        else
        {
            j++;
            if (j < numsSize)
            {
                sum = sum + nums[j];
            }            
        }
    }

    if (output == MAX_SIZE_ARRAY + 1)
    {
        return 0;
    }
    else
    {
        return output;
    }    
    
}
