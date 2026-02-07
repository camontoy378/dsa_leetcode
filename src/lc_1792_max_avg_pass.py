import heapq

class MaxAvgPass:

    def __init__(self, classes, extra_students):
        self.classes        = classes
        self.extra_students = extra_students

    def get_pass_ratio(self, classes, index, num_new_students):
        
        num_students_passing    = classes[index][0] + num_new_students
        total_studenst_in_class = classes[index][1] + num_new_students
        pass_ratio_class        = num_students_passing / total_studenst_in_class

        return pass_ratio_class

    def solve(self):

        classes         = self.classes
        extra_students  = self.extra_students

        output      = []
        heap_max    = []
        sum         = 0

        #Initialize pass ratio, pass ratio + 1 student for all classes and difference.
        for class_index in range(len(classes)):
            
            new_students            = 0
            pass_ratio_class        = self.get_pass_ratio(classes, class_index, new_students)

            output.append(pass_ratio_class) 

            new_students            = 1
            pass_ratio_class_new    = self.get_pass_ratio(classes, class_index, new_students)

            increase                = pass_ratio_class_new - pass_ratio_class

            #Sort biggest increases
            heapq.heappush_max(heap_max, [increase, class_index])

        for i in range(extra_students):

            #Get biggest increase from adding student
            max_num             = heapq.heappop_max(heap_max)
            increase            = max_num[0]
            class_index         = max_num[1]

            #Update classes. Add student to passing and total students
            classes[class_index][0]   += 1
            classes[class_index][1]   += 1

            #Update passing ratio for class. 
            output[class_index] += increase 

            #Recalculate
            new_students            = 0
            pass_ratio_class        = self.get_pass_ratio(classes, class_index, new_students)

            new_students            = 1
            pass_ratio_class_new    = self.get_pass_ratio(classes, class_index, new_students)

            increase                = pass_ratio_class_new - pass_ratio_class

            heapq.heappush_max(heap_max, [increase, class_index])

        
        for num in output:
            sum += num

        return float("{:.5f}".format(sum / len(output)))

    