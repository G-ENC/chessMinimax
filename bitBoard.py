import numpy as np
from cosntants import *
from bitUtil import *
from magicBitBoard import rook_magic_numbers, bishop_magic_numbers
from tables import *



class BitBoard:
  def __init__(self, ):
    self.piece_bit_board = np.array(12,dtype=np.uint64)
    self.occupancy = np.array(3, dtype=np.uint64)
    self.side = -1
    self.enpassant = Coordinate.no_sq
    self.castle = 0