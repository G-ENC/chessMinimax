from bitUtil import *
from square import Square
from cosntants import *
from tables import *

empty_bb = np.uint64(0)

sq1 = Square(Coordinate.h5)

printBitBoard(maskPawnAttacks(sq1, Color.WHITE))

# zero_A_File = []


