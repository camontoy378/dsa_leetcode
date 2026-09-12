#include <stdio.h>


int removeElement(int* nums, int numsSize, int val)
{
   
    int counter = 0;
    int i = 0;
    int j = numsSize - 1;

    for( i; i < numsSize; i++ )
    {
        if(i > j)
        {
            break;
        }
        else if (nums[i] == val)
        {
            while( (j > i) && (nums[j] == val) )
            {
                j--;
            }

            if (j > i)
            {
                nums[i] = nums[j];
                nums[j] = val;
                counter++;
            }
        }
        else
        {
            counter++;
        }
    }

    return counter;
}