
class FloodFill():

    def __init__(self, image, sr, sc, color):

        self.image      = image
        self.sr         = sr
        self.sc         = sc 
        self.new_color  = color

    def get_neighbors(self, row, column):

        return [[row - 1, column], [row + 1, column], [row, column - 1], [row, column + 1]]
    
    def is_pixel_out_of_bounds(self, row, column):

        row_max_len     = len(self.image)
        column_max_len  = len(self.image[0])

        return row < 0 or row >= row_max_len or column < 0 or column >= column_max_len
    
    def is_pixel_value_valid(self, row, column, starting_pixel_value):
        return self.image[row][column] == starting_pixel_value
            
    def is_pixel_valid(self, row, column, starting_pixel_value):

        if self.is_pixel_out_of_bounds(row, column):
            return False
        
        return self.is_pixel_value_valid(row, column, starting_pixel_value)    


    def solve(self):

        q       = []
        visited = []

        starting_pixel_row_index    = self.sr
        starting_pixel_column_index = self.sc

        starting_pixel_value        = self.image[starting_pixel_row_index][starting_pixel_column_index]

        q.append([starting_pixel_row_index, starting_pixel_column_index])

        visited.append([starting_pixel_row_index, starting_pixel_column_index])

        while q:

            sr, sc = q.pop(0)

            self.image[sr][sc] = self.new_color


            neighbors_list = self.get_neighbors(sr, sc)

            for row, column in neighbors_list:

                if not self.is_pixel_valid(row, column, starting_pixel_value):
                    continue

                if [row,column] in visited:
                    continue

                q.append([row,column])

                visited.append([row, column])

        return self.image