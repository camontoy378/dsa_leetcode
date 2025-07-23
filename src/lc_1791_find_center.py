class FindCenter():

    def __init__(self, edges):
        self.edges  = edges

    def solve(self):

        #Get first edge.
        first_edge_0 = self.edges[0][0]
        first_edge_1 = self.edges[0][1]

        #Get second edge.
        second_edge_0 = self.edges[1][0]
        second_edge_1 = self.edges[1][1]

        #Get center

        if first_edge_0 == second_edge_0:
            return first_edge_0
        elif first_edge_0 == second_edge_1:
            return first_edge_0
        elif first_edge_1 == second_edge_0:
            return first_edge_1
        else:
            return first_edge_1
