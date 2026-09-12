import heapq

class GroupAnagrams():

    def __init__(self, strs):
        self.strs   = strs

    def solve(self):

        strs = self.strs

        if strs == [""]:
            return [[""]]
        
        min_heap    = []
        map_ana     = {}
        output      = []
        
        #map anagrams
        for word in strs:


            #Sort string
            for mychar in word:
                heapq.heappush(min_heap, mychar)

            #Assemble chars
            new_string = ""

            while len(min_heap) > 0:
                new_string = new_string + heapq.heappop(min_heap)

            print(new_string)                
            #map
            if new_string in map_ana:
                map_ana[new_string].append(word)
            else:
                map_ana[new_string] = [word]


        for key in map_ana:
            output.append(map_ana[key])

        print(output)
        return output
    
