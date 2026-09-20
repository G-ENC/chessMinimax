import numpy as np

state = np.uint32(1804289383)
def getPsudoRandomU32Number():
  global state
  number = state
    
  #XOR shift algorigthm 
  number ^= number << 13
  number ^= number >> 17
  number ^= number << 5

  state = number
  return number

def getRandomU64Number() -> np.uint64:

  number1 = np.uint64(getPsudoRandomU32Number()) & 0xFFFF
  number2 = np.uint64(getPsudoRandomU32Number()) & 0xFFFF
  number3 = np.uint64(getPsudoRandomU32Number()) & 0xFFFF
  number4 = np.uint64(getPsudoRandomU32Number()) & 0xFFFF

  return number1 | number2<<16 | number3 << 32 | number4 <<48

def generateMagicNumber() -> np.uint64:
  return getRandomU64Number() &getRandomU64Number() & getRandomU64Number()  