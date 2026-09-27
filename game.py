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
      coords = self.getIndexToScreenCoordinates(index)
      image_rect = image.get_rect(topleft=coords)
      self.screen.blit(image, image_rect)
      bitmap = clearBit(bitmap, Square(index))
      pygame.draw.rect(self.screen,"green", image_rect, 3)

  def drawAllPieces(self):
    self.drawPiecesFromBitmap(self.whitePawn)
    self.drawPiecesFromBitmap(self.whiteKnight)
    self.drawPiecesFromBitmap(self.whiteBishop)
    self.drawPiecesFromBitmap(self.whiteRook)
    self.drawPiecesFromBitmap(self.whiteQueen)
    self.drawPiecesFromBitmap(self.whiteKing)

  def holdSelectedPiece(self, index):
    sq = Square(index)

    sqTest = Square(55)

    isFilled = 0

    
    if getBit(self.whitePawn.bitmap, sq):
      print("p")
     
    if getBit(self.whiteBishop.bitmap, sq):
      print("b")
    if getBit(self.whiteKnight.bitmap, sq):
      print("k")
    if getBit(self.whiteRook.bitmap, sq):
      print("R")
    if getBit(self.whiteQueen.bitmap, sq):
      print("Q")
    if getBit(self.whiteKing.bitmap, sq):
      print("K")

  
class Game:
  def __init__(self,screen_w=800, screen_h=800):
    self.run = True
    pygame.init()
    self.screen = pygame.display.set_mode((screen_w, screen_h))
    self.clock = pygame.time.Clock()   
    self.cb = ChessBoard(screen_w,screen_h,self.screen)
    self.update = True
    self.fps = 120

  def initGame(self):



    while self.run:

      self.clock.tick(self.fps)
      

      # self.update = True
      # if self.update:
        
      self.cb.drawCheckerBoardPattern()
      self.cb.drawAllPieces()
      coords = pygame.mouse.get_pos()
      pygame.draw.circle(self.screen,"red", coords, 10)
        # self.update = False

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
          mouse_location = pygame.mouse.get_pos()
          selected_index = int(self.cb.getScreenCoordinatesToIndex(mouse_location))
          self.cb.holdSelectedPiece(selected_index)
          self.update = True
      
          

      pygame.display.update()
    pygame.quit()