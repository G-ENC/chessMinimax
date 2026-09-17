import numpy as np
from cosntants import *


class Square:
    def __init__(self, index):
        self.index = np.uint64(index)
    
    def __str__(self):
        f = self.index%8
        r = self.index//8 + 1
        
        return Coordinate(r*8+f).name
        

    def toBitBoard(self) -> np.uint64:
        return np.uint64(1) << self.index