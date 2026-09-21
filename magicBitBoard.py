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


def findMagicNumber(square: Square, relevant_bits: np.uint64, bishop_flag: bool):
    occupancies = np.zeros(4095,dtype=np.uint64)
    attacks = np.zeros(4095,dtype=np.uint64)
    used_attacks = np.zeros(4095,dtype=np.uint64)

    attack_mask = maskBishopAttacks(square) if bishop_flag else maskRookAttacks(square)
    
    occupancy_indecies = 1 << relevant_bits

    for i in range(occupancy_indecies):
        occupancies[i] = setOccupancy(i,relevant_bits,attack_mask)
        attacks[i] = maskBishopAttacksWithBlocker(square, occupancies[i]) if bishop_flag else maskRookAttacksWithBlocker(square, occupancies[i])

    for random_count in range(100000000000):
        magic_number = generateMagicNumber()

        if countBits((attack_mask*magic_number) & 0xFF00000000000000) < 6:
            continue
        