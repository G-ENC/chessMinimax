from square import Square
import numpy as np
from cosntants import *

class Piece:
  def __init__(self, color:Color, bitmap:np.uint64, filePath:str):
    self.color= color
    self.bitmap = bitmap
    self.filePath = filePath

  
