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
  if chessBoard.side == Color.WHITE:
    return KING_ATTACKS[square.index] & ~chessBoard.whitePieceBitboard
  elif chessBoard.side == Color.BLACK:
    return KING_ATTACKS[square.index] & ~chessBoard.blackPieceBitboard

def getKnightMoveBitboard(square:Square, chessBoard:ChessBoard):
  if chessBoard.side == Color.WHITE:
    return KNIGHT_ATTACKS[square.index] & ~chessBoard.whitePieceBitboard
  elif chessBoard.side == Color.BLACK:
    return KNIGHT_ATTACKS[square.index] & ~chessBoard.blackPieceBitboard

def getPawnMoveBitboard(square:Square, chessBoard:ChessBoard):
  attack = PAWN_ATTACKS[chessBoard.side][square.index]
  quite = np.uint64(0)

  if chessBoard.side == Color.WHITE:#white pawn
    forward_sq = Square(square.index - 8)
    if forward_sq >= 0:#cant go past top
      if not getBit(chessBoard.bothPieceBitboard, forward_sq):#there is no square infort
        quite = forward_sq.toBitBoard()
  
  elif chessBoard.side == Color.BLACK:#black pawn
    forward_sq = Square(square.index + 8)
    if forward_sq <= 63:#cant go past bottom
      if not getBit(chessBoard.bothPieceBitboard, forward_sq):#there is no square infort
        quite = forward_sq.toBitBoard() 
  return attack | quite

def getBishopMoveBitboard(square:Square, chessBoard:ChessBoard):
  return get_bishop_attacks(square, chessBoard.bothPieceBitboard) 

def getRookMoveBitboard(square:Square, chessBoard:ChessBoard):
  return get_rook_attacks(square, chessBoard.bothPieceBitboard)

def getQueenMoveBitboard(square:Square, chessBoard:ChessBoard):
  return get_rook_attacks(square, chessBoard.bothPieceBitboard)|get_bishop_attacks(square, chessBoard.bothPieceBitboard) 


def generatePieceMoves(source_square:Square, piece:Piece, chessBoard:ChessBoard):
  possible_moves = []
  if piece.type == "p":
    moveset = getPawnMoveBitboard(source_square, chessBoard)
    white_promote = source_square.toBitBoard() & np.uint64(65280)
    black_promote = source_square.toBitBoard() & np.uint64(71776119061217280)

    if (white_promote and chessBoard.side == Color.WHITE) or (black_promote and ChessBoard.side == Color.WHITE):
      while(moveset):
        bit = getLsbIndex(moveset)
        dest = Square()
        possible_moves.append([Move(source_square,)])
