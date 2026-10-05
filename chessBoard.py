import pygame
import numpy as np 
from bitUtil import *
from pieces import *
from cosntants import * 
from pieces import *
from tables import *

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

#draw funcitons
  def drawCheckerBoardPattern(self):
    white = True
    for column in range(self.n):
      white = not white
      for row in range(self.n):
        sq_rect = pygame.Rect(self.cell_w*row, self.cell_h*column, self.cell_w, self.cell_h)
        if white:
          pygame.draw.rect(self.screen, (50,50,50), sq_rect)
        else:
          pygame.draw.rect(self.screen, (200,0,200), sq_rect)
        white = not white
  
  def drawAllAttackSquares(self):
    self.attack_surface.fill(pygame.Color(0,0,0,0))
    for column in range(self.n):
      for row in range(self.n):
        sq = Square(row*8+column)
        if self.isSquareAttacked(sq):
          x,y = self.getIndexToScreenCoordinates(sq.index)
          sq_rect = pygame.Rect(x, y, self.cell_w, self.cell_h)
          pygame.draw.rect(self.attack_surface, (133,1, 1, 129), sq_rect)
    self.screen.blit(self.attack_surface, (0,0))
  
  def drawPiecesFromBitboard(self, piece: Piece):
    bitmap = piece.bitmap
    image = pygame.image.load(f"{piece.filePath}").convert_alpha()
    image = pygame.transform.scale(image, (int(self.cell_w), int(self.cell_h)))
    while bitmap:
      index = getLsbIndex(bitmap)     
      coords = self.getIndexToScreenCoordinates(index)
      image_rect = image.get_rect(topleft=coords)
      self.screen.blit(image, image_rect)
      bitmap = clearBit(bitmap, Square(index))
        
  def drawAllPieces(self):
    for side in range(2):
      for piece  in range(6):
        self.drawPiecesFromBitboard(self.allPieces[side][piece])
        
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
  
  def getPieceImage(self,piece:Piece):
    image = pygame.image.load(f"{piece.filePath}").convert_alpha()
    image = pygame.transform.scale(image, (int(self.cell_w), int(self.cell_h)))
    return image

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