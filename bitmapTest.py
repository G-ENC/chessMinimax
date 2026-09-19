from bitUtil import *
from square import Square
from cosntants import *
from tables import *

empty_bb = np.uint64(0)

sq1 = Square(Coordinate.e5)
sq2 = Square(Coordinate.e6)
sq3 = Square(Coordinate.a5)
sq4 = Square(Coordinate.g5)
sq5 = Square(Coordinate.e2)

blocks = sq2.toBitBoard()|sq3.toBitBoard()|sq4.toBitBoard()|sq5.toBitBoard()
printBitBoard(blocks)
# printBitBoard(sq1.toBitBoard())
printBitBoard(maskRookAttacksWithBlocker(sq1, blocks))
print(getLsbIndex(blocks))
print(getMsbIndex(blocks))
printBitBoard(Square(getLsbIndex(blocks)).toBitBoard())
printBitBoard(Square(getMsbIndex(blocks)).toBitBoard())
print(index_to_coordinates[getLsbIndex(blocks)])
print(index_to_coordinates[getMsbIndex(blocks)])
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

