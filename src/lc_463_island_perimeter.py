class IslandPerimeter():

    def __init__(self, grid):
        self.grid   = grid

    def is_index_out_of_bounds(self, index_row, index_column, row_length, column_length):
        return index_row < 0 or index_row >= row_length or index_column < 0 or index_column >= column_length

    def get_inital_valid_indexes(self, row_length, column_length):
        for r in range(row_length):
            for c in range(column_length):
                if self.grid[r][c] == 1:
                    return r, c 
        

    def get_perimeter_of_cell(self, num_valid_neighbors):
        
        if num_valid_neighbors == 0:
            return 4
        elif num_valid_neighbors == 1:
            return 3
        elif num_valid_neighbors == 2:
            return 2
        elif num_valid_neighbors == 3:
            return 1
        else:
            return 0
            

    def get_valid_neighbors(self, index_row, index_column, row_length, column_length):

        valid_neighbors = []

        neighbors   = [ [index_row - 1, index_column], [index_row + 1, index_column], \
                       [index_row, index_column - 1], [index_row, index_column + 1]]
        
        for loop_index_row, loop_index_column in neighbors:

            if not self.is_index_out_of_bounds(loop_index_row, loop_index_column, row_length, column_length) and \
                self.grid[loop_index_row][loop_index_column] == 1:

                valid_neighbors.append([loop_index_row, loop_index_column])

        return valid_neighbors


    def solve(self):

        output_perimeter = 0

        q       = []
        visited = []

        row_length      = len(self.grid)
        column_length   = len(self.grid[0])

        init_index_row, init_index_column = self.get_inital_valid_indexes(row_length, column_length)

        q.append([init_index_row,init_index_column])
        visited.append([init_index_row,init_index_column])

        while q:

            q_index_row, q_index_column = q.pop(0)

            valid_neighbors = self.get_valid_neighbors(q_index_row, q_index_column, row_length, column_length)

            num_valid_neighbors = len(valid_neighbors)
            output_perimeter += self.get_perimeter_of_cell(num_valid_neighbors)

            for n_index_row, n_index_column in valid_neighbors:
                
                if [n_index_row, n_index_column] in visited:
                    continue
                
                q.append([n_index_row, n_index_column])

                visited.append([n_index_row, n_index_column])                

        return output_perimeter