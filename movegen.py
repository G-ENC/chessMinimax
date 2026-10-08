import pygame
import numpy as np 
from bitUtil import *
from pieces import *
from cosntants import * 
from pieces import *
from tables import *
from chessBoard import *
from move import Move

#moveset fucniton for each piece

def getKingMoveBitboard(square:Square, chessBoard:ChessBoard):
  if chessBoard.side == Color.WHITE: #whites turn
    return KING_ATTACKS[square.index] & ~chessBoard.whitePieceBitboard #cant go past own pieces as king
  elif chessBoard.side == Color.BLACK:
    return KING_ATTACKS[square.index] & ~chessBoard.blackPieceBitboard

def getKnightMoveBitboard(square:Square, chessBoard:ChessBoard):
  if chessBoard.side == Color.WHITE:
    return KNIGHT_ATTACKS[square.index] & ~chessBoard.whitePieceBitboard
  elif chessBoard.side == Color.BLACK:
    return KNIGHT_ATTACKS[square.index] & ~chessBoard.blackPieceBitboard

def getPawnMoveBitboard(square:Square, chessBoard:ChessBoard):

  opp_bitboard = chessBoard.blackPieceBitboard if not chessBoard.side else chessBoard.whitePieceBitboard
  attack = PAWN_ATTACKS[chessBoard.side][square.index] & opp_bitboard #can go diagonal only when tehre is pieces

  quite = np.uint64(0)

  if chessBoard.side == Color.WHITE:#white pawn
    forward_sq = Square(square.index - 8)
    if forward_sq.index >= 0:#cant go past top
      if not getBit(chessBoard.bothPieceBitboard, forward_sq):#there is no square infort
        quite = forward_sq.toBitBoard()
    
    two_square_forward_sq = Square(square.index - 16)
    if two_square_forward_sq.index >= 0 and getBit(RANK_2,square):
      if not getBit(chessBoard.bothPieceBitboard, two_square_forward_sq):#there is no square infort
        chessBoard.enpassant = forward_sq
        quite |= two_square_forward_sq.toBitBoard()

  elif chessBoard.side == Color.BLACK:#black pawn
    forward_sq = Square(square.index + 8)
    two_square_forward_sq = Square(square.index - 16)
    
    if forward_sq.index <= 63:#cant go past bottom
      if not getBit(chessBoard.bothPieceBitboard, forward_sq):#there is no square infort
        quite = forward_sq.toBitBoard() 
    
    two_square_forward_sq = Square(square.index + 16)
    if two_square_forward_sq.index <= 63 and getBit(RANK_7,square):
      if not getBit(chessBoard.bothPieceBitboard, two_square_forward_sq):#there is no square infort
        chessBoard.enpassant = forward_sq
        quite |= two_square_forward_sq.toBitBoard()

  return attack | quite

def getBishopMoveBitboard(square:Square, chessBoard:ChessBoard):
  return get_bishop_attacks(square, chessBoard.bothPieceBitboard) 

def getRookMoveBitboard(square:Square, chessBoard:ChessBoard):
  return get_rook_attacks(square, chessBoard.bothPieceBitboard)

def getQueenMoveBitboard(square:Square, chessBoard:ChessBoard):
  return get_rook_attacks(square, chessBoard.bothPieceBitboard)|get_bishop_attacks(square, chessBoard.bothPieceBitboard) 

def generatePieceMoves(source_square:Square, piece:Piece, chessBoard:ChessBoard):
  possible_moves = [] #get all the possible move for the piece

  if piece.type == "p": #pawn
    moveset = getPawnMoveBitboard(source_square, chessBoard) #possible square that specific pawn can move 
    white_promote = source_square.toBitBoard() & np.uint64(65280) #white pawn at 7th row
    black_promote = source_square.toBitBoard() & np.uint64(71776119061217280) #black pawn at 2nd row

    if (white_promote and chessBoard.side == Color.WHITE) or (black_promote and chessBoard.side == Color.BLACK): #the pormotion should occure at the round they are playing?? duh
      while(moveset): #for all the bits that are avaible loop every single one and save it as a possible Move() which has a source and destination 
        bit_index = getLsbIndex(moveset) #get lsb 
        dest = Square(bit_index)
        possible_moves.append([Move(source_square, dest, True)])
        moveset = clearBit(moveset, dest) #delete that bit so the next lsb is  new one
      return possible_moves

  elif piece.type == "n": #knight
    moveset = getKnightMoveBitboard(source_square, chessBoard)

  elif piece.type == "k": #king
    moveset = getKingMoveBitboard(source_square, chessBoard)

  elif piece.type == "b": #bishop
    moveset = getBishopMoveBitboard(source_square, chessBoard)

  elif piece.type == "r": #rook
    moveset = getRookMoveBitboard(source_square, chessBoard)

  elif piece.type == "q": #queen
    moveset = getQueenMoveBitboard(source_square, chessBoard)

  while moveset:
    bit_index = getLsbIndex(moveset) 
    dest = Square(bit_index)
    possible_moves.append(Move(source_square, dest))
    moveset = clearBit(moveset, dest) 
  return possible_moves 

def generateAllMoves(chessBoard: ChessBoard):
  all_moves = []
  for side in range(2):
    for piece in range(6):
      piece = chessBoard.allPieces[side][piece]
      piece_bitboard = piece.bitmap
      while piece_bitboard:
        piece_index = getLsbIndex(piece_bitboard) 
        piece_square = Square(piece_index)
        piece_bitboard = clearBit(piece_bitboard, piece_square) 
        all_moves.append(generatePieceMoves(piece_square, piece, chessBoard))
  return all_moves