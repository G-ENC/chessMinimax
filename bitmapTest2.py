from bitUtil import *
from square import Square
from cosntants import *

exampleBb = np.uint64(0xFFFFFFFFFF000000)

empty_bb = np.uint64(0)

empty_bb |= np.uint64(1)<<0

#setting squares
sq1 = Square(Coordinate.a8)
sq2 = Square(Coordinate.b4)
sq3 = Square(Coordinate.g7)
empty_bb = setBit(empty_bb, sq1)
empty_bb = setBit(empty_bb, sq2)
empty_bb = setBit(empty_bb, sq3)

#clearing bit
empty_bb = clearBit(empty_bb, sq1)

#printing board
# print(type(empty_bb), type(Coordinate.e2))
printBitBoard(empty_bb)
# printBoardWithCoordinates()

