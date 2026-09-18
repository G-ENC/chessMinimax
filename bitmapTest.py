from bitUtil import *
from square import Square
from cosntants import *
from tables import *

empty_bb = np.uint64(0)

sq1 = Square(Coordinate.e5)
sq2 = Square(Coordinate.h8)
sq3 = Square(Coordinate.h1)
sq4 = Square(Coordinate.a1)
sq5 = Square(Coordinate.a8)

# printBitBoard(sq1.toBitBoard())
# printBitBoard(maskRookAttacks(sq1))
# printBitBoard(maskRookAttacks(sq2))
# printBitBoard(maskRookAttacks(sq3))
# printBitBoard(maskRookAttacks(sq4))



for i in range(64):
  printBitBoard(ROOK_ATTACKS[i])


# zero_A_File = []
# FILE/RANK ISOLATION
# for file in range(8):
#   for rank in range(8):

#     if(file == 6):
#       square = Square(rank*8+file)
#       empty_bb = setBit(empty_bb, square)

# print("==============g file==============")
# printBitBoard(empty_bb)

