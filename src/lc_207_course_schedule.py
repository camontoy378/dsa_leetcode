class CourseSchedule():
    
    def __init__(self, num_courses, prereqs):
        self.num_courses    = num_courses
        self.prereqs    = prereqs

    def build_adjacency_graph(self):

        graph = {}

        for course0, course1 in self.prereqs:

            if course1 not in graph:
                graph[course1] = [course0]
            else:
                graph[course1].append(course0)

            if course0 not in graph:
                graph[course0] = []

        return graph
    
    def has_cycle(self, node, stack, visited, adj_graph):

        #Tests
        #If cycle detected.
        if node in stack:
            return False
        
        #If node points to itself
        if node in adj_graph[node]:
            return False
        
        if visited[node] == 'V':
            return True
        
        if adj_graph[node] == []:
            return True
        
        
        
        for new_node in adj_graph[node]:

            #Setup
            visited[node] = 'V'
            stack.append(node)

            result = self.has_cycle(new_node, stack, visited, adj_graph)

            if not result:
                break

            if stack:
                stack.pop()

        return result

        
    

    def solve(self):

        if self.prereqs == []:
            return True

        #Setup
        stack   = []
        visited = ['N'] * self.num_courses

        adj_graph = self.build_adjacency_graph()

        #Foreach node look for cycles. Return False if found.
        for key in adj_graph:

            result = self.has_cycle(key, stack, visited, adj_graph)

            if not result:
                return result

        return True


            