

class MovingAverage():

    def __init__(self, max_window_size):
        self.max_window_size        = max_window_size
        self.current_window_size    = 0
        self.sum                    = 0
        self.array_index            = -1
        self.array                  = [] 

    def next(self, val):

        self.array.append(val)
        self.array_index += 1
        self.current_window_size += 1

        if self.current_window_size > self.max_window_size:
            self.current_window_size -= 1
            
            self.sum = self.sum - self.array[self.array_index - self.current_window_size] + val

            return self.sum / self.current_window_size
        
        else:
            self.sum += val

            return self.sum / self.current_window_size

    def solve(self):
        return True