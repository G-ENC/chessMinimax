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

    self.whitePawn = Piece( Color.WHITE, np.uint64(0x00FF000000000000), "pieceImages/whitePawn.png")
    self.whiteKnight = Piece( Color.WHITE, np.uint64(0x4200000000000000), "pieceImages/whiteKnight.png")
    self.whiteBishop = Piece( Color.WHITE, np.uint64(0x2400000000000000), "pieceImages/whiteBishop.png")
    self.whiteRook = Piece( Color.WHITE, np.uint64(0x8100000000000000), "pieceImages/whiteRook.png")
    self.whiteQueen = Piece( Color.WHITE, np.uint64(0x0800000000000000), "pieceImages/whiteQueen.png")
    self.whiteKing = Piece( Color.WHITE, np.uint64(0x1000000000000000), "pieceImages/whiteKing.png")
    
    self.blackPawn = Piece( Color.BLACK, np.uint64(0x000000000000FF00), "pieceImages/blackPawn.png")
    self.blackKnight = Piece( Color.BLACK, np.uint64(0x00000000000042), "pieceImages/blackKnight.png")
    self.blackBishop = Piece( Color.BLACK, np.uint64(0x0000000000000024), "pieceImages/blackBishop.png")
    self.blackRook = Piece( Color.BLACK, np.uint64(0x0000000000000081), "pieceImages/blackRook.png")
    self.blackQueen = Piece( Color.BLACK,np.uint64( 0x000000000000008), "pieceImages/blackQueen.png")
    self.blackKing = Piece( Color.BLACK, np.uint64(0x0000000000000010), "pieceImages/blackKing.png")

    self.allPieces = [self.whitePawn,self.whiteKnight,self.whiteBishop,self.whiteRook,self.whiteQueen,self.whiteKing,self.blackPawn, self.blackKnight,self.blackBishop,self.blackRook,self.blackQueen,self.blackKing]

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
          pygame.draw.rect(self.screen, (50,50,50), sq_rect)
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
      # pygame.draw.rect(self.screen,"green", image_rect, 3)

  def drawAllPieces(self):
    for i  in range(len(self.allPieces)):
      self.drawPiecesFromBitmap(self.allPieces[i])

  def popSelectedPiece(self, index):
    sq = Square(index)
    image = None

    def getPieceImage(piece:Piece):
      piece.bitmap = clearBit(piece.bitmap,sq)
      image = pygame.image.load(f"{piece.filePath}").convert_alpha()
      image = pygame.transform.scale(image, (int(self.cell_w), int(self.cell_h)))
      return image

    # def getImageByIndex(piece:Piece, index):
    #   sq = Square(index)
    #   if getBit(piece.bitmap, sq):
    #     return getPieceImage(piece)
    #   else:
    #     return None

    
    #I am so sorry idk how to abstract 
    
    # getImageByIndex()

    if getBit(self.whitePawn.bitmap, sq):
      return getPieceImage(self.whitePawn)

    #look ma if statements!
    if getBit(self.whiteBishop.bitmap, sq):
      self.whiteBishop.bitmap = clearBit(self.whiteBishop.bitmap,sq)
      image = pygame.image.load(f"{self.whiteBishop.filePath}").convert_alpha()
      image = pygame.transform.scale(image, (int(self.cell_w), int(self.cell_h)))
    if getBit(self.whiteKnight.bitmap, sq):
      self.whiteKnight.bitmap = clearBit(self.whiteKnight.bitmap,sq)
      image = pygame.image.load(f"{self.whiteKnight.filePath}").convert_alpha()
      image = pygame.transform.scale(image, (int(self.cell_w), int(self.cell_h)))
    if getBit(self.whiteRook.bitmap, sq):
      self.whiteRook.bitmap = clearBit(self.whiteRook.bitmap,sq)
      image = pygame.image.load(f"{self.whiteRook.filePath}").convert_alpha()
      image = pygame.transform.scale(image, (int(self.cell_w), int(self.cell_h)))
    if getBit(self.whiteQueen.bitmap, sq):
      self.whiteQueen.bitmap = clearBit(self.whiteQueen.bitmap,sq)
      image = pygame.image.load(f"{self.whiteQueen.filePath}").convert_alpha()
      image = pygame.transform.scale(image, (int(self.cell_w), int(self.cell_h)))
    if getBit(self.whiteKing.bitmap, sq):
      self.whiteKing.bitmap = clearBit(self.whiteKing.bitmap,sq)
      image = pygame.image.load(f"{self.whiteKing.filePath}").convert_alpha()
      image = pygame.transform.scale(image, (int(self.cell_w), int(self.cell_h)))


      
    return image

  
class Game:
  def __init__(self,screen_w=800, screen_h=800):
    self.run = True
    pygame.init()
    self.screen = pygame.display.set_mode((screen_w, screen_h))
    self.clock = pygame.time.Clock()   
    self.cb = ChessBoard(screen_w,screen_h,self.screen)
    self.update = True
    self.fps = 60
    self.holdPieceImage = None
    self.timer = 0
  def initGame(self):

    

    while self.run:

      


      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.run = False

        elif event.type == pygame.MOUSEMOTION:  
          self.update = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
          mouse_location = pygame.mouse.get_pos()
          selected_index = int(self.cb.getScreenCoordinatesToIndex(mouse_location))
          self.holdPieceImage = self.cb.popSelectedPiece(selected_index)
          self.update = True


      if self.update:
        self.cb.drawCheckerBoardPattern()
        self.cb.drawAllPieces()

        if self.holdPieceImage != None:
          m_pos = pygame.mouse.get_pos()
          image_rect = self.holdPieceImage.get_rect(center=m_pos)
          self.screen.blit(self.holdPieceImage, image_rect)
        
        self.update = False
      
   

      pygame.display.update()
    pygame.quit()