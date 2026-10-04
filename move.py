class Move:
  def __init__(self, s, d, p=None):
    self.source = s
    self.destination = d
    self.promotion = p
  
  def __str__(self):
    return f"{self.source} --> {self.destination}"

  def __repr__(self):
    return self.__str__()