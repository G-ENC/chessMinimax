from cosntants import *
import numpy as np
from square import Square
from bitUtil import *

#
  #     NOT A FILE
  # 8   0 1 1 1 1 1 1 1 
  # 7   0 1 1 1 1 1 1 1 
  # 6   0 1 1 1 1 1 1 1 
  # 5   0 1 1 1 1 1 1 1 
  # 4   0 1 1 1 1 1 1 1 
  # 3   0 1 1 1 1 1 1 1 
  # 2   0 1 1 1 1 1 1 1 
  # 1   0 1 1 1 1 1 1 1 

  #     a b c d e f g h

                  # ATTACKS #
def maskPawnAttacks(square: Square, color: Color):
  
  attacks = np.uint64(0)
  
  bitboard = np.uint64(0)

  bitboard = setBit(bitboard, square)

  #white piece
  if not color:
    
    attacks |= bitboard >> 7
    attacks |= bitboard >> 9
  #black piece
  else:
    pass

  return attacks