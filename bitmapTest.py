from bitUtil import *
from square import Square
from cosntants import *
from tables import *
from randomUtil import *
from magicBitBoard import *




empty_bb = np.uint64(0)

sq1 = Square(Coordinate.e5)
sq2 = Square(Coordinate.e6)
sq3 = Square(Coordinate.a5)
sq4 = Square(Coordinate.g5)
sq5 = Square(Coordinate.e2)



# init_magic_numbers()
for i in range(4096):
  printBitBoard(setOccupancy(i, countBits(maskBishopAttacks(sq1)),maskBishopAttacks(sq1)))
#   printBitBoard(generateMagicNumber())
  input() 

# for i in range(64):
#   printBitBoard(ROOK_ATTACKS[i])

# zero_A_File = []
# FILE/RANK ISOLATION
# for file in range(8):
#   for rank in range(8):

#     if(file == 6):
#       square = Square(rank*8+file)
#       empty_bb = setBit(empty_bb, square)

# print("==============g file==============")
# printBitBoard(empty_bb)
