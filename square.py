import numpy as np

class Square:
    def __init__(self, index):
        self.index = index
    
    def toBitBoard(self):
        return np.uint64(1) << self.index