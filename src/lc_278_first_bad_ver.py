class FirstBadVersion():

    def __init__(self, input, bad):
        self.input  = input
        self.bad    = bad

    def isBadVersion(self, n):
        
        if n >= self.bad:
            return True
        else:
            return False
        
    def get_avg(self, min, max):
        return int( (max + min) / 2 )


    def solve(self):

        n = self.input

        min = 1
        max = n

        new_version = self.get_avg(min, max)
        found = False

        #Binary search
        while not found:
            
            if   ( self.isBadVersion(new_version) and new_version == 1):
                return new_version
            elif ( self.isBadVersion(new_version) and not self.isBadVersion(new_version - 1)):
                return new_version
            elif ( self.isBadVersion(new_version) ):
                max         = new_version - 1
                new_version = self.get_avg(min, max)
            elif ( not self.isBadVersion(new_version) ):
                min         = new_version + 1
                new_version = self.get_avg(min, max)

        return new_version
    