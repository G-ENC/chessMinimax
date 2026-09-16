from bitUtil import *
from square import Square

def decToBoardPrint(dec):
    bits = str(bin(dec)[2:])
    # print(f" op {bits[0]}")
    for start in range(56,-8,-8):
        for i in range(8):
            print(start+i, end=" ")
        print()


exampleBb = np.uint64(0xFFFFFFFFFF000000)

lsb = bitScanLsb(exampleBb)
print("~~~~~~")
print(len(str(bin(exampleBb)[2:])))
Square(lsb).toBitBoard()
decToBoardPrint(exampleBb)