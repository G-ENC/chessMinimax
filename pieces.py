from square import Square
import numpy as np
from cosntants import *

class Piece:
  def __init__(self, color:Color, bitmap:np.uint64, filePath:str, pieceType):
    self.color= color
    self.bitmap = bitmap
    self.filePath = filePath
    self.type = pieceType

  def __str__(self):
    return f"{self.color.name} {self.type}"
  
  
