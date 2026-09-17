from cosntants import *
import numpy as np
from square import Square
from bitUtil import *

FILE_A = np.uint64(72340172838076673)
FILE_H = np.uint64(9259542123273814144)
RANK_1 = np.uint64(18374686479671623680)
RANK_8 = np.uint64(255)



                  # ATTACKS #
def maskPawnAttacks(square: Square, color: Color):
  
  attacks = np.uint64(0)
  
  bitboard = np.uint64(0)

  bitboard = setBit(bitboard, square)

  #white piece
  if not color:
    if(getBit(FILE_A, square)):
      attacks |= bitboard >> 7
    elif(getBit(FILE_H, square)):
      attacks |= bitboard >> 9
    else:
      attacks |= bitboard >> 7
      attacks |= bitboard >> 9
    
  #black piece
  else:
    pass

  return attacks

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