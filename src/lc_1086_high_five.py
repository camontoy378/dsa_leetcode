import heapq

class HighFive():

    def __init__(self, scores_array):

        self.scores_array   = scores_array

    def pop(self, array):

        if array:
            neg_score, id =  heapq.heappop(array)
            return -neg_score, id
        else:
            return None, None

    def push(self, array, id, score):

        heapq.heappush(array, (-score, id))
        

    def solve(self):

        NUM_SCORES_TO_AVG = 5

        heap_array = []

        for item in self.scores_array:

            self.push(heap_array, item[0], item[1])

        #dictionary id, sum
        sum_dict = {}
        #dictionary id, num_scores
        num_scores = {}

        #loop
        while 1:
            score, id = self.pop(heap_array)

            if score == None:
                break

            #If id not exist create default dicts.
            elif id not in sum_dict:
                sum_dict[id]    = score
                num_scores[id]  = 1

            elif num_scores[id] < NUM_SCORES_TO_AVG:
                sum_dict[id] += score
                num_scores[id] += 1 

        output = []

        for id, sum in sum_dict.items():
            output.append( [id, int(sum / NUM_SCORES_TO_AVG) ] )

        return sorted(output)