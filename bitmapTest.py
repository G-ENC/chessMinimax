from bitUtil import *
from square import Square
from cosntants import *
from tables import *

empty_bb = np.uint64(0)

sq1 = Square(Coordinate.a5)

printBitBoard(sq1.toBitBoard())
printBitBoard(maskPawnAttacks(sq1, Color.BLACK))

# zero_A_File = []


