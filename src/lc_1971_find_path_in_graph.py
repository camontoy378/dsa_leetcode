
class FindPathInGraph():
    
    def __init__(self, num_nodes, edges, src, dest):
        self.num_nodes  = num_nodes
        self.edges      = edges
        self.src        = src
        self.dest       = dest

    def bfs(self):

        path    = []
        q       = []
        visited = [False] * self.num_nodes

        q.append(self.src)
        visited[self.src] = True

        while q:

            curr_node = q.pop(0)

            #Find adj nodes
            for item in self.edges:

                if item[0] == curr_node:

                    if not visited[item[1]]:

                        q.append(item[1])
                        visited[item[1]] = True
                    
                if item[1] == curr_node:
                    
                    if not visited[item[0]]:

                        q.append(item[0])
                        visited[item[0]] = True

            path.append(curr_node)

            if self.dest in path:
                return True
            
        return False
    

    def solve(self):

        return self.bfs()