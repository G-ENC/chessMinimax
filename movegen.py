import pygame
import numpy as np 
from bitUtil import *
from pieces import *
from cosntants import * 
from pieces import *
from tables import *
from chessBoard import *

#moveset fucniton for each piece

def getKingMoveBitboard(square:Square, chessBoard:ChessBoard):
  return KING_ATTACKS[square.index] & ~chessBoard.bothPieceBitboard

def getKingMoveBitboard(square:Square, chessBoard:ChessBoard):
  return KNIGHT_ATTACKS[square.index] & ~chessBoard.bothPieceBitboard

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


def 