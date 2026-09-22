import numpy as np
from square import Square
from tables import *
from randomUtil import *

ROOK_INDEX_BITS = [
    12, 11, 11, 11, 11, 11, 11, 12,
    11, 10, 10, 10, 10, 10, 10, 11,
    11, 10, 10, 10, 10, 10, 10, 11,
    11, 10, 10, 10, 10, 10, 10, 11,
    11, 10, 10, 10, 10, 10, 10, 11,
    11, 10, 10, 10, 10, 10, 10, 11,
    11, 10, 10, 10, 10, 10, 10, 11,
    12, 11, 11, 11, 11, 11, 11, 12
]

BISHOP_INDEX_BITS = [
    6, 5, 5, 5, 5, 5, 5, 6,
    5, 5, 5, 5, 5, 5, 5, 5,
    5, 5, 7, 7, 7, 7, 5, 5,
    5, 5, 7, 9, 9, 7, 5, 5,
    5, 5, 7, 9, 9, 7, 5, 5,
    5, 5, 7, 7, 7, 7, 5, 5,
    5, 5, 5, 5, 5, 5, 5, 5,
    6, 5, 5, 5, 5, 5, 5, 6
]

rook_magic_numbers = []
bishop_magic_numbers = []

def findMagicNumber(square: Square, relevant_bits: np.uint8, bishop_flag: bool):

    
    occupancies = np.zeros(4096, np.uint64)
    attacks = np.zeros(4096, np.uint64)
    used_attacks = np.zeros(4096, dtype=np.uint64)

    attack_mask = maskBishopAttacks(square) if bishop_flag else maskRookAttacks(square)


    occupancy_indecies = np.uint64(1) << np.uint8(relevant_bits)
    shift = np.uint64(64-relevant_bits)

    for i in range(occupancy_indecies):
        occupancies[i] = setOccupancy(i,relevant_bits,attack_mask)
        attacks[i] = maskBishopAttacksWithBlocker(square, occupancies[i]) if bishop_flag else maskRookAttacksWithBlocker(square, occupancies[i])

    while True:
        magic_number = generateMagicNumber()


        if countBits((attack_mask*magic_number) & 0xFF00000000000000) < 6:
            continue

        
        used_attacks = np.zeros(4096, np.uint64)
        
        fail = False
        for i in range(occupancy_indecies):
            magic_index = (np.uint64(occupancies[i]*magic_number))>>(shift)

            if(used_attacks[magic_index] == np.uint64(0)):
                used_attacks[magic_index] = attacks[i]
            elif(used_attacks[magic_index] != attacks[i]):
                fail = True
                break

        if not fail:
            return magic_number
  

def init_magic_numbers():

    for i in range(64):
        rook_magic_numbers.append(findMagicNumber(Square(i), countBits(maskRookAttacks(Square(i))), 0))
    for i in range(64):
        bishop_magic_numbers.append(findMagicNumber(Square(i), countBits(maskBishopAttacks(Square(i))), 1))


    return(rook_magic_numbers,bishop_magic_numbers)