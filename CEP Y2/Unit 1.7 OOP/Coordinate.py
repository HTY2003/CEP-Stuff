class Coordinate (object):
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
         return "(" + str(self.x) +\
                ","+str(self.y) +\
                ")"
    def __repr__(self):
        return self.__str__()
    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return round((x_diff_sq+y_diff_sq)**0.5)
    def __add__(self,other):
        return Coordinate(self.x+other.x,\
                          self.y+other.y)


if __name__ == "__main__":
    origin=Coordinate(0,0)
    
    
