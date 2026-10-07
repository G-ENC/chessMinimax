import pygame
import numpy as np 
from bitUtil import *
from pieces import *
from cosntants import * 
from pieces import *
from tables import *
from move import *

class ChessBoard:

  pieceNames = ["pawn","knight","bishop","rook","queen","king"]

  def __init__(self, screen_w, screen_h, screen, attack_surface):

    self.screen = screen
    self.attack_surface = attack_surface
    self.width = screen_w
    self.height = screen_h
    self.n = 8
    self.cell_w = self.width/self.n
    self.cell_h = self.height/self.n

    self.whitePawn = Piece(Color.WHITE, np.uint64(0x00FF000000000000), "pieceImages/whitePawn.png", "p")
    self.whiteKnight = Piece(Color.WHITE, np.uint64(0x4200000000000000), "pieceImages/whiteKnight.png", "n")
    self.whiteBishop = Piece(Color.WHITE, np.uint64(0x2400000000000000), "pieceImages/whiteBishop.png", "b")
    self.whiteRook = Piece(Color.WHITE, np.uint64(0x8100000000000000), "pieceImages/whiteRook.png", "r")
    self.whiteQueen = Piece(Color.WHITE, np.uint64(0x0800000000000000), "pieceImages/whiteQueen.png", "q")
    self.whiteKing = Piece(Color.WHITE, np.uint64(0x1000000000000000), "pieceImages/whiteKing.png", "k")
    
    self.blackPawn = Piece(Color.BLACK, np.uint64(0x000000000000FF00), "pieceImages/blackPawn.png", "p")
    self.blackKnight = Piece(Color.BLACK, np.uint64(0x00000000000042), "pieceImages/blackKnight.png", "n")
    self.blackBishop = Piece(Color.BLACK, np.uint64(0x0000000000000024), "pieceImages/blackBishop.png", "b")
    self.blackRook = Piece(Color.BLACK, np.uint64(0x0000000000000081), "pieceImages/blackRook.png", "r")
    self.blackQueen = Piece(Color.BLACK,np.uint64( 0x000000000000008), "pieceImages/blackQueen.png", "q")
    self.blackKing = Piece(Color.BLACK, np.uint64(0x0000000000000010), "pieceImages/blackKing.png", "k")

    self.allPieces = [[self.whitePawn,self.whiteKnight,self.whiteBishop,self.whiteRook,self.whiteQueen,self.whiteKing],
                      [self.blackPawn, self.blackKnight,self.blackBishop,self.blackRook,self.blackQueen,self.blackKing]]
    
    self.whitePieceBitboard = self.getWhiteBitboard()
    self.blackPieceBitboard = self.getBlackBitboard()
    self.bothPieceBitboard = self.getBothBitboard()

    self.side = -1
    self.enpassant = Coordinate.no_sq
    self.castle = 0

  def copy(self):
    nb = ChessBoard.__new__(ChessBoard)
    nb.screen, nb.attack_surface = self.screen, self.attack_surface
    nb.width, nb.height, nb.n = self.width, self.height, self.n
    nb.cell_w, nb.cell_h = self.cell_w, self.cell_h

    nb.allPieces = [[Piece(p.color, p.bitmap, p.filePath, p.type) for p in side] for side in self.allPieces]

    (nb.whitePawn, nb.whiteKnight, nb.whiteBishop, nb.whiteRook, nb.whiteQueen, nb.whiteKing) = nb.allPieces[0]
    
    (nb.blackPawn, nb.blackKnight, nb.blackBishop, nb.blackRook, nb.blackQueen, nb.blackKing) = nb.allPieces[1]

    nb.side, nb.enpassant, nb.castle = self.side, self.enpassant, self.castle
    nb.refreshBoard()

    return nb

  def refreshBoard(self):
    self.whitePieceBitboard = self.getWhiteBitboard()
    self.blackPieceBitboard = self.getBlackBitboard()
    self.bothPieceBitboard = self.getBothBitboard()

#loop funcitons

#logic functions
  def isSquareAttacked(self, square:Square):
    if self.side == Color.WHITE:
      if(PAWN_ATTACKS[Color.BLACK][square.index] & self.whitePawn.bitmap):
        return True
      elif(KNIGHT_ATTACKS[square.index] & self.whiteKnight.bitmap):
        return True
      elif(get_bishop_attacks(square,self.bothPieceBitboard) & self.whiteBishop.bitmap):
        return True
      elif(get_rook_attacks(square,self.bothPieceBitboard) & self.whiteRook.bitmap):
        return True
      elif(get_queen_attacks(square,self.bothPieceBitboard)& self.whiteQueen.bitmap):
        return True
      elif(KING_ATTACKS[square.index] & self.whiteKing.bitmap):
        return True
      
    elif self.side == Color.BLACK:
      if(PAWN_ATTACKS[Color.WHITE][square.index] & self.blackPawn.bitmap):
        return True
      elif(KNIGHT_ATTACKS[square.index] & self.blackKnight.bitmap):
        return True
      elif(get_bishop_attacks(square,self.bothPieceBitboard) & self.blackBishop.bitmap):
        return True
      elif(get_rook_attacks(square,self.bothPieceBitboard) & self.blackRook.bitmap):
        return True
      elif(get_queen_attacks(square,self.bothPieceBitboard)& self.blackQueen.bitmap):
        return True
      elif(KING_ATTACKS[square.index] & self.blackKing.bitmap):
        return True
      
    else:
      return False

  # def validMovesForPiece(self, piece:Piece, source_square:Square):

  #   target_squares = []

  #   #quite move
  #   if piece.type == "p":
  #     quite_move = source_square.toBitBoard() - np.uint64(8)
  #     if quite_move >= 0:
  #       target_squares.append(quite_move)

  def nextPlayerTurn(self):
    if (self.side == -1):
      self.side = 0
    elif self.side == 0:
      self.side = 1
    else:
      self.side = 0
 
#get set and pop funcitons
  def getIndexToScreenCoordinates(self, index):
    row = index%8 
    column = index//8 
    x_co = row*self.cell_w 
    y_co = column*self.cell_h 
    return(x_co,y_co)

  def getScreenCoordinatesToIndex(self, coordinate:tuple):
    rank = coordinate[1]//self.cell_h
    file = coordinate[0]//self.cell_w
    return(rank*8+file) #return index for 64 bit number

  def getWhiteBitboard(self):
    return self.whitePawn.bitmap|self.whiteKnight.bitmap|self.whiteBishop.bitmap|self.whiteRook.bitmap|self.whiteQueen.bitmap|self.whiteKing.bitmap
  
  def getBlackBitboard(self):
    return self.blackPawn.bitmap|self.blackKnight.bitmap|self.blackBishop.bitmap|self.blackRook.bitmap|self.blackQueen.bitmap|self.blackKing.bitmap
  
  def getBothBitboard(self):
    white = self.getWhiteBitboard()
    black = self.getBlackBitboard() 
    return white|black
  
  #loops over the piece array and finds the matching piece that occupies the selected square
  def getObjectByIndex(self, index):
    sq = Square(index)
    for side in range(2):
      for piece in range(6):
        if getBit(self.allPieces[side][piece].bitmap, sq):
          return self.allPieces[side][piece]

  #loops over the piece array, clears that bit from selected index and returns that piece object 
  def popAndGetSelectedPiece(self, index):
    pieceObject = self.getObjectByIndex(index)
    if pieceObject:
      pieceObject.bitmap = clearBit(pieceObject.bitmap, Square(index))

    return pieceObject 

  def putPieceToSquare(self, piece:Piece, index):
    piece.bitmap = setBit(piece.bitmap, Square(index))
    
    self.whitePieceBitboard = self.getWhiteBitboard()
    self.blackPieceBitboard = self.getBlackBitboard()
    self.bothPieceBitboard = self.getBothBitboard()

  def clearPieceFromSquare(self, piece:Piece, index):
    piece.bitmap = clearBit(piece.bitmap, Square(index))
    
    self.whitePieceBitboard = self.getWhiteBitboard()
    self.blackPieceBitboard = self.getBlackBitboard()
    self.bothPieceBitboard = self.getBothBitboard()

  def applyMove(self, move):
    nb = self.copy()
    src = Coordinate[move.source].value
    dst = Coordinate[move.destination].value

    source_piece = nb.getObjectByIndex(src)
    victim = nb.getObjectByIndex(dst)
    if victim is not None and victim.color != source_piece.color:
        victim.bitmap = clearBit(victim.bitmap, Square(dst))   # clear the DESTINATION square

    source_piece.bitmap = clearBit(source_piece.bitmap, Square(src))
    source_piece.bitmap = setBit(source_piece.bitmap, Square(dst))
    nb.refreshBoard()
    return nb

  # def applyMove(self, move:Move):
  #   new_board = ChessBoard(self.width, self.height, self.screen,self.attack_surface)

  #   new_board.n = self.n
  #   new_board.cell_w = self.cell_w
  #   new_board.cell_h = self.cell_h

  #   new_board.allPieces = self.allPieces
  #   new_board.whitePieceBitboard = self.whitePieceBitboard
  #   new_board.blackPieceBitboard = self.blackPieceBitboard
  #   new_board.bothPieceBitboard = self.bothPieceBitboard

  #   new_board.side = self.side

  #   source_piece = new_board.popAndGetSelectedPiece(Coordinate[move.source].value)
  #   dest_piece = new_board.getObjectByIndex(Coordinate[move.destination].value)
  #   if dest_piece != None and dest_piece.color != source_piece.color:
  #     new_board.clearPieceFromSquare(dest_piece, getLsbIndex(dest_piece.bitmap))
  #   new_board.putPieceToSquare(source_piece, Coordinate[move.destination].value)

  #   return new_board