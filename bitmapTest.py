from bitUtil import *
from square import Square
from cosntants import *
from tables import *

empty_bb = np.uint64(0)

sq1 = Square(Coordinate.h5)
sq2 = Square(Coordinate.a5)
sq3 = Square(Coordinate.e8)
sq4 = Square(Coordinate.e1)

# printBitBoard(sq1.toBitBoard())
printBitBoard(maskKingAttacks(sq1))
printBitBoard(maskKingAttacks(sq2))
printBitBoard(maskKingAttacks(sq3))
printBitBoard(maskKingAttacks(sq4))





# for i in range(64):
#   printBitBoard(KING_ATTACKS[i])


# zero_A_File = []
# FILE/RANK ISOLATION
# for file in range(8):
#   for rank in range(8):

#     if(file == 6):
#       square = Square(rank*8+file)
#       empty_bb = setBit(empty_bb, square)

# print("==============g file==============")
# printBitBoard(empty_bb)

