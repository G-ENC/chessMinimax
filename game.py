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

  def getPieceImage(self,piece:Piece):
    image = pygame.image.load(f"{piece.filePath}").convert_alpha()
    image = pygame.transform.scale(image, (int(self.cell_w), int(self.cell_h)))
    return image

  def getObjectByIndex(self, index):
    sq = Square(index)
    for i in range(len(self.allPieces)):
      if getBit(self.allPieces[i].bitmap, sq):
        return self.allPieces[i]

  def popAndGetSelectedPiece(self, index):

    pieceObject = self.getObjectByIndex(index)
    if pieceObject:
      pieceObject.bitmap = clearBit(pieceObject.bitmap, Square(index))

    return pieceObject 


  def putPieceToSquare(self, piece:Piece, index):

    piece.bitmap = setBit(piece.bitmap, Square(index))


class Game:
  def __init__(self,screen_w=800,screen_h=800):
    self.run = True
    pygame.init()
    self.screen = pygame.display.set_mode((screen_w, screen_h))
    self.clock = pygame.time.Clock()   
    self.cb = ChessBoard(screen_w,screen_h,self.screen)
    self.update = True
    self.fps = 60
    self.holdPiece = None
    self.timer = 0

  def initGame(self):

    while self.run:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.run = False

        #update the screen so that the piece follows the cursor
        elif event.type == pygame.MOUSEMOTION:  
          self.update = True

        #hold the piece if not holding already
        elif event.type == pygame.MOUSEBUTTONDOWN:
          mouse_location = pygame.mouse.get_pos()
          selected_index = int(self.cb.getScreenCoordinatesToIndex(mouse_location))
          if self.holdPiece == None:  
            self.holdPiece = self.cb.popAndGetSelectedPiece(selected_index)
            self.update = True
          else:
            self.cb.putPieceToSquare(self.holdPiece,selected_index)
            self.holdPiece = None

      #update screen
      if self.update:
        self.cb.drawCheckerBoardPattern()
        self.cb.drawAllPieces()

        if self.holdPiece != None:
          holdPieceImage = self.cb.getPieceImage(self.holdPiece)
          m_pos = pygame.mouse.get_pos()
          image_rect = holdPieceImage.get_rect(center=m_pos)
          self.screen.blit(holdPieceImage, image_rect)
        
        self.update = False
      
   

      pygame.display.update()
    pygame.quit()