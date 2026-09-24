import numpy as np
from square import Square

debruijn64 = np.uint64(0x03f79d71b4cb0a89);

#print board
def printBitBoard(bitboard):
  print()
  for rank in range(8):
    for file in range(8):
        #loop over every index and convert to square index
        square = Square(rank*8 + file)
        #print rank
        if file == 0:
            print("  %d   " % (8-rank), end="")
        #either 1 or 0
        RED = "\033[32m"
        GRAY = "\033[90m"
        bit = RED if getBit(bitboard, square) else GRAY
        print(f"{bit}█▉\033[00m", end="")
    print()
  #print files
  print("\n      a b c d e f g h \n")
  #bitobard as decimal number
  print(f"      Bitboard: {bitboard}\n")

#one time use
def printBitBoardForEnumList():
  for rank in range(8):
    for file in range(8):
      print(f"{chr(ord("a")+file)}{8-rank} = {rank*8 +file}")

# set/get/pop methods
def getBit(bitboard: np.uint64, square: Square) -> np.uint64:
  return bitboard & (square.toBitBoard())

def setBit(bitboard: np.uint64, square: Square) -> np.uint64:
  bitboard |= square.toBitBoard()
  return bitboard

def clearBit(bitboard: np.uint64, square: Square) -> np.uint64:
  return bitboard & (~square.toBitBoard())

ls1bTable = np.array(
  [ 0,  1, 48,  2, 57, 49, 28,  3,
   61, 58, 50, 42, 38, 29, 17,  4,
   62, 55, 59, 36, 53, 51, 43, 22,
   45, 39, 33, 30, 24, 18, 12,  5,
   63, 47, 56, 27, 60, 41, 37, 16,
   54, 35, 52, 21, 44, 32, 23, 11,
   46, 26, 40, 15, 34, 20, 31, 10,
   25, 14, 19,  9, 13,  8,  7,  6], 
   dtype=np.uint8)

ms1bTable = np.array(
  [ 0, 47,  1, 56, 48, 27,  2, 60,
   57, 49, 41, 37, 28, 16,  3, 61,
   54, 58, 35, 52, 50, 42, 21, 44,
   38, 32, 29, 23, 17, 11,  4, 62,
   46, 55, 26, 59, 40, 36, 15, 53,
   34, 51, 20, 43, 31, 22, 10, 45,
   25, 39, 14, 33, 19, 30,  9, 24,
   13, 18,  8, 12,  7,  6,  5, 63], 
   dtype=np.uint8)

def getLsbIndex(bb: np.uint64) -> np.uint8:
    return ls1bTable[((bb&-bb) *debruijn64)>>np.uint8(58)]

def getMsbIndex(bb: np.uint64):
    
    bb |= bb >> np.uint8(1)
    bb |= bb >> np.uint8(2)
    bb |= bb >> np.uint8(4)
    bb |= bb >> np.uint8(8)
    bb |= bb >> np.uint8(16)
    bb |= bb >> np.uint8(32)
    return ms1bTable[(bb * debruijn64) >> np.uint8(58)]

def countBits(bitboard: np.uint64) -> np.uint8:
  count = np.uint8(0)
  while(bitboard):
    bitboard &= bitboard -1
    count += 1
  return count

def setOccupancy(index: np.uint8, bits_in_mask: np.uint8, attack_mask: np.uint64):

  occupacy = np.uint64(0)
#idk what is going on
  for count in range(bits_in_mask):
    square = Square(getLsbIndex(attack_mask))
    attack_mask = clearBit(attack_mask, square)
    if(index & (np.uint64(1)<<count)):
        occupacy |= (square.toBitBoard())
  return occupacy



   