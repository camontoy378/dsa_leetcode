
class FindPathInGraph():
    
    def __init__(self, num_nodes, edges, src, dest):
        self.num_nodes  = num_nodes
        self.edges      = edges
        self.src        = src
        self.dest       = dest

    def create_adj_dict(self, edge_list):

        adj_dict = {}

        for edge in edge_list:
            key     = edge[0]
            value   = edge[1]

            if key in adj_dict:
                adj_dict[key].append(value)
            else:
                adj_dict[key] = [value]

            if value in adj_dict:
                adj_dict[value].append(key)
            else:
                adj_dict[value] = [key]
            
        return adj_dict
    
    def dfs(self, adj_dict, src, dest, visited):

        #Exit condition
        if src == dest:
            return True
        
        if visited[src] == 1:
            return False
        
        #Work
        visited[src] = 1

        #Recursion
        for new_num in adj_dict[src]:
            if self.dfs(adj_dict, new_num, dest, visited):
                return True
            
        return False

    def solve(self):

        src     = self.src
        dest    = self.dest
        visited = [0] * self.num_nodes

        adj_dict = self.create_adj_dict(self.edges)

        return self.dfs(adj_dict, src, dest, visited)
