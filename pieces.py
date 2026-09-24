from square import Square
import numpy as np

class Pawn:
  def __init__(self):
    self.color=None
    self.coordinates = []
    self.bitmap=None
    self.bitmap = np.uint64(0x00FF000000000000)
    self.filePath = "pieceImages/pawn.png"

   


  
