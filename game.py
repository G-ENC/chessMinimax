from bitBoard import BitBoard
import pygame
import numpy as np 
from bitUtil import *
from pieces import *
from cosntants import * 
from pieces import *

class ChessBoard:

  pieceNames = ["pawn","knight","bishop","rook","queen","king"]

  def __init__(self, screen_w, screen_h, screen):
    self.screen = screen
    self.width = screen_w
    self.height = screen_h
    self.n = 8
    self.cell_w = self.width/self.n
    self.cell_h = self.height/self.n

    self.whitePawn = Piece(Color.WHITE, np.uint64(0x00FF000000000000), "pieceImages/whitePawn.png")
    self.whiteKnight = Piece(Color.WHITE, 0x4200000000000000, "pieceImages/whiteKnight.png")
    self.whiteBishop = Piece(Color.WHITE, 0x2400000000000000, "pieceImages/whiteBishop.png")
    self.whiteRook = Piece(Color.WHITE, 0x8100000000000000, "pieceImages/whiteRook.png")
    self.whiteQueen = Piece(Color.WHITE, 0x0800000000000000, "pieceImages/whiteQueen.png")
    self.whiteKing = Piece(Color.WHITE, 0x1000000000000000, "pieceImages/whiteKing.png")
    
    # self.blackPawn = Piece(Color.BLACK, np.uint64(0x00FF000000000000), "pieceImages/blackPawn.png")
    # self.blackKnight = Piece(Color.BLACK, 0x4200000000000000, "pieceImages/blackKnight.png")
    # self.blackBishop = Piece(Color.BLACK, 0x2400000000000000, "pieceImages/blackBishop.png")
    # self.blackRook = Piece(Color.BLACK, 0x8100000000000000, "pieceImages/blackRook.png")
    # self.blackQueen = Piece(Color.BLACK, 0x0800000000000000, "pieceImages/blackQueen.png")
    # self.blackKing = Piece(Color.BLACK, 0x1000000000000000, "pieceImages/blackKing.png")


  def indexToScreenCoordinates(self, index):
    row = index%8 
    column = index//8 
    x_co = row*self.cell_w 
    y_co = column*self.cell_h 
    return(x_co,y_co)
  
  def drawCheckerBoardPattern(self):
    white = True
    for column in range(self.n):
      white = not white
      for row in range(self.n):
        sq_rect = pygame.Rect(self.cell_w*row, self.cell_h*column, self.cell_w, self.cell_h)
        if white:
          pygame.draw.rect(self.screen, (0,0,0), sq_rect)
        else:
          pygame.draw.rect(self.screen, (200,0,200), sq_rect)
        white = not white

  def drawPiecesFromBitmap(self, piece: Piece):
    bitmap = piece.bitmap
    image = pygame.image.load(f"{piece.filePath}").convert_alpha()
    image = pygame.transform.scale(image, (int(self.cell_w), int(self.cell_h)))
    while bitmap:
      index = getLsbIndex(bitmap)      
      coords = self.indexToScreenCoordinates(index)
      image.get_rect().center = coords
      self.screen.blit(image, coords)

      bitmap = clearBit(bitmap, Square(index))
      pygame.draw.rect(self.screen,"green", image.get_rect(), 3)
 
  def drawAllPieces(self):
    self.drawPiecesFromBitmap(self.whitePawn)
    self.drawPiecesFromBitmap(self.whiteKnight)
    self.drawPiecesFromBitmap(self.whiteBishop)
    self.drawPiecesFromBitmap(self.whiteRook)
    self.drawPiecesFromBitmap(self.whiteQueen)
    self.drawPiecesFromBitmap(self.whiteKing)
    
class Game:
  def __init__(self,screen_w=800, screen_h=800):
    self.run = True
    pygame.init()
    self.screen = pygame.display.set_mode((screen_w, screen_h))
    self.clock = pygame.time.Clock()   
    self.cb = ChessBoard(screen_w,screen_h,self.screen)

  def initGame(self):

    self.cb.drawCheckerBoardPattern()
    self.cb.drawAllPieces()

    while self.run:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.run = False

      pygame.display.update()
    pygame.quit()