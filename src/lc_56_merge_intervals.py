class MergeIntervals():

    def __init__(self, intervals):
        self.intervals  = intervals
        
    def merge_arrays(self, array1, array2):

        index1          = 0
        index2          = 0
        output_stack    = []

        while (index1 < len(array1)) and (index2 < len(array2)):

            if array1[index1][0] < array2[index2][0]:
                smaller = array1[index1]
                index1 += 1
    
            else:
                smaller = array2[index2]
                index2 += 1

            self.stack_push(output_stack, smaller)

        #Push remaining
        while index1 < len(array1):
            self.stack_push(output_stack,array1[index1])
            index1 += 1

        #Push remaining
        while index2 < len(array2):
            self.stack_push(output_stack,array2[index2])
            index2 += 1

        return output_stack

    def stack_push(self, output_stack, smaller):
        
        #Is stack empty?
        if len(output_stack) == 0:
            output_stack.append(smaller)
        
        #Replace
        elif output_stack[-1][1] > smaller[1]:
            pass
        
        #Merge
        elif output_stack[-1][1] >= smaller[0]:
            temp = output_stack.pop()
            merge_num = [temp[0], smaller[1]]
            output_stack.append(merge_num)
        
        else:
            output_stack.append(smaller)

    def merge(self, intervals):

        midpoint    = int(len(intervals)/2)

        #Ending condition
        if len(intervals) < 2:
            return [intervals[0]]

        #Recursion. Split arrays.
        left_array  = self.merge(intervals[0:midpoint])
        right_array = self.merge(intervals[midpoint:])
        
        #Work
        result = self.merge_arrays(left_array, right_array)

        return result


    def solve(self):

        #Merge Sort
        output = self.merge(self.intervals)

        return output