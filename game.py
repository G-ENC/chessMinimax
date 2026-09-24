from bitBoard import BitBoard
import pygame
import numpy as np 
from bitUtil import *
from pieces import *
from cosntants import * 

class ChessBoard:

  pieceNames = ["pawn","knight","bishop","rook","queen","king"]

  def __init__(self, screen_w, screen_h, screen):
    self.screen = screen
    self.width = screen_w
    self.height = screen_h
    self.n = 8
    self.cell_w = self.width/self.n
    self.cell_h = self.height/self.n

    self.whitePawn = Piece(Color.WHITE, 0x00FF000000000000, "pieceImages/whitePawn")
    self.whiteKnight = Piece(Color.WHITE, 0x3300000000000000, "pieceImages/white")
    self.whitePawn = Piece(Color.WHITE, 0x00FF000000000000, "pieceImages/whitePawn")
    self.whitePawn = Piece(Color.WHITE, 0x00FF000000000000, "pieceImages/whitePawn")
    self.whitePawn = Piece(Color.WHITE, 0x00FF000000000000, "pieceImages/whitePawn")
    self.whitePawn = Piece(Color.WHITE, 0x00FF000000000000, "pieceImages/whitePawn")

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
  
  def drawAllPieces(self):
    self.drawPiecesFromBitmap(self.piece)
    self.drawPiecesFromBitmap(self.piece)
    
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