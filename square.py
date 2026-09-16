import numpy as np



class Square:
    def __init__(self, index):
        self.index = index
    
    def __str__(self):
        f = self.index%8
        r = self.index//8 + 1
        return "%s%d" % f,r
        

    def toBitBoard(self):
        return np.uint64(1) << self.index