class FindCeleb():

    def __init__(self, graph):
        self.graph  = graph
    
    def knows(self, a, b):
        if self.graph[a][b] == 1:
            return True
        else:
            return False

    def solve(self):

        #Initialize data structures
        n           = len(self.graph)
        not_celeb   = [0] * n

        for i in range(n):
            
            if not_celeb[i] == 1:
                continue

            for j in range(n):

                if i == j:
                    continue

                if self.knows(i,j) == False:
                    not_celeb[j]    = 1
                else:
                    not_celeb[i]    = 1

                if self.knows(j,i) == False:
                    not_celeb[i]    = 1
                else:
                    not_celeb[j]    = 1
                    

        celeb       = -1

        for i in range(n):

            if not_celeb[i] == 0:
                celeb = i
                
        return celeb
        
        