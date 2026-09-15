import numpy as np
from square import Square

def print64BitString(bits):
    for i in range(64):
        print(bits[i],end=" ")
        if i%8 == 7:
            print()

def dec_to_bin_reversed(dec):
    if(dec == 0):
        return ""
    if dec<0:
        return str(-dec%2) + str(dec_to_bin_reversed(-dec//2))
    return str(dec%2) + str(dec_to_bin_reversed(dec//2))

def dec_to_bin(dec):
    bin_rev = dec_to_bin_reversed(dec)
    return bin_rev[::-1]    

def decToBinGrid(dec):
    stringBin = dec_to_bin(dec)
    zeros = missingZeros(dec)
    stringBin = zeros + stringBin
    print64BitString(stringBin)

def decToBinGridRev(dec):
    stringBinRev = dec_to_bin_reversed(dec)
    zeros = missingZeros(dec)
    stringBinRev = stringBinRev + zeros
    print64BitString(stringBinRev)

def missingZeros(dec):
    missing = 64-len(dec_to_bin(dec))
    zero_list = ["0" for _ in range(missing)]
    zeros = "".join(zero_list)
    return zeros


    
# def getRow(dec, row):

#     stringBin = dec_to_bin(dec)

shifted_dec = 0x000000000000FF00
neg_shifted_dec = -shifted_dec
print(shifted_dec)
print("~~~~~~~~~~~~~~~")
# shifted_dec |= 0b100101010111110000000011101
# shifted_dec &= 0b111111111111
decToBinGrid(shifted_dec)
print("~~~~~~~~~~~~~~~")
decToBinGrid(neg_shifted_dec)
print("~~~~~~~~~~~~~~~")
# decToBinGridRev(shifted_dec)

def indexToCoordinate(index):

    r = index // 8
    f = index % 8

    return "%s%d" % (chr(ord("A")+f), r+1)

for index in range(64):
    if (index)%8 == 0:
        print()
    print(indexToCoordinate(index), end=" ")
print()


debruijn64 = np.uint64(0x03f79d71b4cb0a89);

print(dec_to_bin(debruijn64))

index64 = np.array(
  [ 0,  1, 48,  2, 57, 49, 28,  3,
   61, 58, 50, 42, 38, 29, 17,  4,
   62, 55, 59, 36, 53, 51, 43, 22,
   45, 39, 33, 30, 24, 18, 12,  5,
   63, 47, 56, 27, 60, 41, 37, 16,
   54, 35, 52, 21, 44, 32, 23, 11,
   46, 26, 40, 15, 34, 20, 31, 10,
   25, 14, 19,  9, 13,  8,  7,  6], 
   dtype=np.uint8)

msb1 = np.array(
  [ 0, 47,  1, 56, 48, 27,  2, 60,
   57, 49, 41, 37, 28, 16,  3, 61,
   54, 58, 35, 52, 50, 42, 21, 44,
   38, 32, 29, 23, 17, 11,  4, 62,
   46, 55, 26, 59, 40, 36, 15, 53,
   34, 51, 20, 43, 31, 22, 10, 45,
   25, 39, 14, 33, 19, 30,  9, 24,
   13, 18,  8, 12,  7,  6,  5, 63], 
   dtype=np.uint8)



def bitScanReverse(bb):
    bb |= bb >> np.uint8(1)
    bb |= bb >> np.uint8(2)
    bb |= bb >> np.uint8(4)
    bb |= bb >> np.uint8(8)
    bb |= bb >> np.uint8(16)
    bb |= bb >> np.uint8(32)
    return msb1[(bb * debruijn64) >> np.uint8(58)]

    
def lsb_bitscan(bb):
    return index64[((np.uint64(bb&-bb)) * debruijn64)>>np.uint64(58)]

for i in range(63):
    binaryNoZero = dec_to_bin(index64[i])
    zeros = "".join(["0" for i in range(6-len(binaryNoZero))])
    print(binaryNoZero+zeros)

shift =lsb_bitscan(0b100011110001001010011011111010010101100000100000)
print(shift)
print(dec_to_bin(np.array(1)<<shift))
shift_m = bitScanReverse(np.uint64(0b000000111100010101001111111000111111100011001000))
print(dec_to_bin(np.array(1)<<shift_m))
shift ^= shift_m
print(dec_to_bin(shift))
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
sq1 = Square(63)
print(dec_to_bin(sq1.toBitBoard()))
decToBinGrid(sq1.toBitBoard())
