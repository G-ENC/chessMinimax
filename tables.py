from cosntants import *
import numpy as np
from square import Square
from bitUtil import *

FILE_A = np.uint64(72340172838076673)
FILE_B = np.uint64(144680345676153346)
FILE_H = np.uint64(9259542123273814144)
FILE_G = np.uint64(4629771061636907072)

RANK_1 = np.uint64(18374686479671623680)
RANK_2 = np.uint64(71776119061217280)
RANK_7 = np.uint64(65280)
RANK_8 = np.uint64(255)

SQUARE_ITTER_NO_COLOR = []
for i in range(64):
  SQUARE_ITTER_NO_COLOR.append(Square(i))

SQUARE_ITTER_COLOR = []
for color in Color:
  for i in range(64):
    SQUARE_ITTER_COLOR.append((color, Square(i)))

                  # ATTACKS #
def maskPawnAttacks(color:Color, square: Square) -> np.uint64:
  attacks = np.uint64(0)
  #white piece
  if not color:
    #white pawn at left most square can go to right diagonal
    attacks |= (square.toBitBoard() & ~FILE_A) >> np.uint8(9) 
    #white pawn at right most square can go to left diagonal
    attacks |= (square.toBitBoard() & ~FILE_H) >> np.uint8(7) 
  #black piece
  else:
    #black pawn at left most square can go to right diagonal
    attacks |= (square.toBitBoard() & ~FILE_A) << np.uint8(7) 
    #black pawn at right most square can go to left diagonal
    attacks |= (square.toBitBoard() & ~FILE_H) << np.uint8(9)
  return attacks

PAWN_ATTACKS = np.fromiter((maskPawnAttacks(color, square) for (color, square) in SQUARE_ITTER_COLOR), dtype=np.uint64, count=2*64)
PAWN_ATTACKS.shape = (2,64)

def maskKinghtAttacks(square: Square) -> np.uint64:
  attack = np.uint64(0)

  left_mask = FILE_A|FILE_B
  right_mask = FILE_G|FILE_H

  upper_right_top = ((square.toBitBoard()) >> np.uint8(15))
  upper_right_under = (~FILE_G & square.toBitBoard()) >> np.uint8(6)

  upper_right_top = (square.toBitBoard() >> np.uint8(15))&~FILE_A
  upper_right_under = (square.toBitBoard() >> np.uint8(6))&~left_mask

  upper_left_top = (square.toBitBoard() >> np.uint8(17))&~FILE_H
  upper_left_under = (square.toBitBoard() >> np.uint8(10))&~right_mask
  
  lower_left_under = (square.toBitBoard() << np.uint8(15))&~FILE_H
  lower_left_top = (square.toBitBoard() << np.uint8(6))&~right_mask

  lower_right_under = (square.toBitBoard() << np.uint8(17))&~FILE_A
  lower_right_top = (square.toBitBoard() << np.uint8(10))&~left_mask
 
  attack = upper_right_top|upper_right_under|upper_left_top|upper_left_under|lower_left_under|lower_left_top|lower_right_under|lower_right_top

  return attack

KNIGHT_ATTACKS = np.fromiter((maskKinghtAttacks(square) for square in SQUARE_ITTER_NO_COLOR), dtype=np.uint64, count=64)

def maskKingAttacks(square: Square) -> np.uint64:
  attack = np.uint64(0)

  lower_right = square.toBitBoard()<<np.uint8(9)&~FILE_A
  lower_center = square.toBitBoard()<<np.uint8(8)
  lower_left = square.toBitBoard()<<np.uint8(7)&~FILE_H

  center_right = square.toBitBoard()<<np.uint8(1)&~FILE_A
  center_left = square.toBitBoard()>>np.uint8(1)&~FILE_H

  upper_right = (square.toBitBoard()>>np.uint8(9))&~FILE_H
  uppper_center = square.toBitBoard()>>np.uint8(8)
  upper_left = square.toBitBoard()>>np.uint8(7)&~FILE_A

  attack |= lower_right | lower_center | lower_left | center_right | center_left | upper_right | uppper_center | upper_left

  return attack 

KING_ATTACKS = np.fromiter((maskKingAttacks(square) for square in SQUARE_ITTER_NO_COLOR), dtype=np.uint64, count=64)

#
  # =======A FILE=========    
  # 8   1 0 0 0 0 0 0 0 
  # 7   1 0 0 0 0 0 0 0 
  # 6   1 0 0 0 0 0 0 0 
  # 5   1 0 0 0 0 0 0 0 
  # 4   1 0 0 0 0 0 0 0 
  # 3   1 0 0 0 0 0 0 0 
  # 2   1 0 0 0 0 0 0 0 
  # 1   1 0 0 0 0 0 0 0 

  #     a b c d e f g h 

  #     Bitboard: 72340172838076673

  # =========NOT A FILE==========
  # 8   0 1 1 1 1 1 1 1 
  # 7   0 1 1 1 1 1 1 1 
  # 6   0 1 1 1 1 1 1 1 
  # 5   0 1 1 1 1 1 1 1 
  # 4   0 1 1 1 1 1 1 1 
  # 3   0 1 1 1 1 1 1 1 
  # 2   0 1 1 1 1 1 1 1 
  # 1   0 1 1 1 1 1 1 1 

  #     a b c d e f g h 

  #     Bitboard: 18374403900871474942

  # =======H FILE========= 
  # 8   0 0 0 0 0 0 0 1 
  # 7   0 0 0 0 0 0 0 1 
  # 6   0 0 0 0 0 0 0 1 
  # 5   0 0 0 0 0 0 0 1 
  # 4   0 0 0 0 0 0 0 1 
  # 3   0 0 0 0 0 0 0 1 
  # 2   0 0 0 0 0 0 0 1 
  # 1   0 0 0 0 0 0 0 1 

  #     a b c d e f g h 

  #     Bitboard: 9259542123273814144

  # =======NOT H FILE========= 
  # 8   1 1 1 1 1 1 1 0 
  # 7   1 1 1 1 1 1 1 0 
  # 6   1 1 1 1 1 1 1 0 
  # 5   1 1 1 1 1 1 1 0 
  # 4   1 1 1 1 1 1 1 0 
  # 3   1 1 1 1 1 1 1 0 
  # 2   1 1 1 1 1 1 1 0 
  # 1   1 1 1 1 1 1 1 0 

  #     a b c d e f g h 

  #     Bitboard: 9187201950435737471

#   ==============8th Rank==============

#   8   1 1 1 1 1 1 1 1 
#   7   0 0 0 0 0 0 0 0 
#   6   0 0 0 0 0 0 0 0 
#   5   0 0 0 0 0 0 0 0 
#   4   0 0 0 0 0 0 0 0 
#   3   0 0 0 0 0 0 0 0 
#   2   0 0 0 0 0 0 0 0 
#   1   0 0 0 0 0 0 0 0 

#       a b c d e f g h 

#       Bitboard: 255


# ==============Not 8th Rank==============

#   8   0 0 0 0 0 0 0 0 
#   7   1 1 1 1 1 1 1 1 
#   6   1 1 1 1 1 1 1 1 
#   5   1 1 1 1 1 1 1 1 
#   4   1 1 1 1 1 1 1 1 
#   3   1 1 1 1 1 1 1 1 
#   2   1 1 1 1 1 1 1 1 
#   1   1 1 1 1 1 1 1 1 

#       a b c d e f g h 

#       Bitboard: 18446744073709551360

# ==============1st Rank==============

#   8   0 0 0 0 0 0 0 0 
#   7   0 0 0 0 0 0 0 0 
#   6   0 0 0 0 0 0 0 0 
#   5   0 0 0 0 0 0 0 0 
#   4   0 0 0 0 0 0 0 0 
#   3   0 0 0 0 0 0 0 0 
#   2   0 0 0 0 0 0 0 0 
#   1   1 1 1 1 1 1 1 1 

#       a b c d e f g h 

#       Bitboard: 18374686479671623680


# ==============Not 1st Rank==============
#   8   1 1 1 1 1 1 1 1 
#   7   1 1 1 1 1 1 1 1 
#   6   1 1 1 1 1 1 1 1 
#   5   1 1 1 1 1 1 1 1 
#   4   1 1 1 1 1 1 1 1 
#   3   1 1 1 1 1 1 1 1 
#   2   1 1 1 1 1 1 1 1 
#   1   0 0 0 0 0 0 0 0 

#       a b c d e f g h 

#       Bitboard: 72057594037927935

# ==============2nd Rank==============
#   8   0 0 0 0 0 0 0 0 
#   7   0 0 0 0 0 0 0 0 
#   6   0 0 0 0 0 0 0 0 
#   5   0 0 0 0 0 0 0 0 
#   4   0 0 0 0 0 0 0 0 
#   3   0 0 0 0 0 0 0 0 
#   2   1 1 1 1 1 1 1 1 
#   1   0 0 0 0 0 0 0 0 

#       a b c d e f g h 

#       Bitboard: 71776119061217280

# ==============7th~ Rank==============
#   8   0 0 0 0 0 0 0 0 
#   7   1 1 1 1 1 1 1 1 
#   6   0 0 0 0 0 0 0 0 
#   5   0 0 0 0 0 0 0 0 
#   4   0 0 0 0 0 0 0 0 
#   3   0 0 0 0 0 0 0 0 
#   2   0 0 0 0 0 0 0 0 
#   1   0 0 0 0 0 0 0 0 

#       a b c d e f g h 

#       Bitboard: 65280

# ==============b file==============

#   8   0 1 0 0 0 0 0 0 
#   7   0 1 0 0 0 0 0 0 
#   6   0 1 0 0 0 0 0 0 
#   5   0 1 0 0 0 0 0 0 
#   4   0 1 0 0 0 0 0 0 
#   3   0 1 0 0 0 0 0 0 
#   2   0 1 0 0 0 0 0 0 
#   1   0 1 0 0 0 0 0 0 

#       a b c d e f g h 

#       Bitboard: 144680345676153346

# ==============g file==============

#   8   0 0 0 0 0 0 1 0 
#   7   0 0 0 0 0 0 1 0 
#   6   0 0 0 0 0 0 1 0 
#   5   0 0 0 0 0 0 1 0 
#   4   0 0 0 0 0 0 1 0 
#   3   0 0 0 0 0 0 1 0 
#   2   0 0 0 0 0 0 1 0 
#   1   0 0 0 0 0 0 1 0 

#       a b c d e f g h 

#       Bitboard: 4629771061636907072