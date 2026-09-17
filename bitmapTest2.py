from bitUtil import *
from square import Square
from cosntants import *
from tables import *

empty_bb = np.uint64(0)

sq1 = Square(Coordinate.d5)

printBitBoard(maskPawnAttacks(sq1, Color.WHITE))

# zero_A_File = []

empty_bb = ~empty_bb

for file in range(8):
  for rank in range(8):

    if(file == 0):
      square = Square(rank*8+file)
      empty_bb = clearBit(empty_bb, square)

printBitBoard(empty_bb)
printBitBoard(~empty_bb)