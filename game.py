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

    self.allPieces = [[self.whitePawn,self.whiteKnight,self.whiteBishop,self.whiteRook,self.whiteQueen,self.whiteKing],
                      [self.blackPawn, self.blackKnight,self.blackBishop,self.blackRook,self.blackQueen,self.blackKing]]
    
    self.whitePieceBitmap = self.whitePawn.bitmap|self.whiteKnight.bitmap|self.whiteBishop.bitmap|self.whiteRook.bitmap|self.whiteQueen.bitmap|self.whiteKing.bitmap
    self.blackPieceBitmap = self.blackPawn.bitmap|self.blackKnight.bitmap|self.blackBishop.bitmap|self.blackRook.bitmap|self.blackQueen.bitmap|self.blackKing.bitmap
    self.bothPieceBitmap = self.whitePieceBitmap|self.blackPieceBitmap

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
      elif(get_bishop_attacks(square,self.bothPieceBitmap) & self.whiteBishop.bitmap):
        return True
      elif(get_rook_attacks(square,self.bothPieceBitmap) & self.whiteRook.bitmap):
        return True
      elif(get_queen_attacks(square,self.bothPieceBitmap)& self.whiteQueen.bitmap):
        return True
      elif(KING_ATTACKS[square.index] & self.whiteKing.bitmap):
        return True
      
    elif self.side == Color.BLACK:
      if(PAWN_ATTACKS[Color.WHITE][square.index] & self.blackPawn.bitmap):
        return True
      elif(KNIGHT_ATTACKS[square.index] & self.blackKnight.bitmap):
        return True
      elif(get_bishop_attacks(square,self.bothPieceBitmap) & self.blackBishop.bitmap):
        return True
      elif(get_rook_attacks(square,self.bothPieceBitmap) & self.blackRook.bitmap):
        return True
      elif(get_queen_attacks(square,self.bothPieceBitmap)& self.blackQueen.bitmap):
        return True
      elif(KING_ATTACKS[square.index] & self.blackKing.bitmap):
        return True
      
    else:
      return False

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

  def drawAttackSquare(self, index):
    self.attack_surface.fill(pygame.Color(0,0,0,0))
    sq = Square(index)
    if self.isSquareAttacked(sq):
      x,y = self.getIndexToScreenCoordinates(sq.index)
      sq_rect = pygame.Rect(x, y, self.cell_w, self.cell_h)
      pygame.draw.rect(self.attack_surface, (133,1, 1), sq_rect)
    self.screen.blit(self.attack_surface, (0,0))

  def drawAllAttackSquares(self):
    self.attack_surface.fill(pygame.Color(0,0,0,0))
    for column in range(self.n):
      for row in range(self.n):
        sq = Square(row*8+column)
        if self.isSquareAttacked(sq):
          x,y = self.getIndexToScreenCoordinates(sq.index)
          sq_rect = pygame.Rect(x, y, self.cell_w, self.cell_h)
          pygame.draw.rect(self.attack_surface, (133,1, 1), sq_rect)
    self.screen.blit(self.attack_surface, (0,0))

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
        
  def drawAllPieces(self):
    for side in range(2):
      for piece  in range(6):
        self.drawPiecesFromBitmap(self.allPieces[side][piece])

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
  
  def getPieceImage(self,piece:Piece):
    image = pygame.image.load(f"{piece.filePath}").convert_alpha()
    image = pygame.transform.scale(image, (int(self.cell_w), int(self.cell_h)))
    return image

  def getObjectByIndex(self, index):
    sq = Square(index)
    for side in range(2):
      for piece in range(6):
        if getBit(self.allPieces[side][piece].bitmap, sq):
          return self.allPieces[side][piece]

  def popAndGetSelectedPiece(self, index):
    pieceObject = self.getObjectByIndex(index)
    if pieceObject:
      pieceObject.bitmap = clearBit(pieceObject.bitmap, Square(index))

    return pieceObject 

  def putPieceToSquare(self, piece:Piece, index):
    piece.bitmap = setBit(piece.bitmap, Square(index))

#game loop
class Game:
  def __init__(self,screen_w=800,screen_h=800):
    pygame.init()
    self.run = True
    
    self.screen = pygame.display.set_mode((screen_w, screen_h))
    self.attack_surface = pygame.Surface((screen_w,screen_h), pygame.SRCALPHA)
    self.cb = ChessBoard(screen_w,screen_h,self.screen, self.attack_surface)

    self.clock = pygame.time.Clock()   
    self.update = True
    self.fps = 60
    self.holdPiece = None
    self.holdPieceIndex = None
    self.timer = 0
    initALL()

  def initGame(self):
    self.cb.nextPlayerTurn()
    
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
          self.holdPieceIndex = selected_index 
          if self.holdPiece == None:  
            self.holdPiece = self.cb.popAndGetSelectedPiece(selected_index)
          else:
            self.cb.putPieceToSquare(self.holdPiece,selected_index)
            self.holdPiece = None
          self.update = True


      #update screen
      if self.update:
        
        # printBitBoard(self.cb.whitePawn.bitmap)
        self.cb.drawCheckerBoardPattern()
        self.cb.drawAllPieces()

        if self.holdPiece != None:
          self.cb.drawAttackSquare(self.holdPieceIndex)
          holdPieceImage = self.cb.getPieceImage(self.holdPiece)
          m_pos = pygame.mouse.get_pos()
          image_rect = holdPieceImage.get_rect(center=m_pos)
          self.screen.blit(holdPieceImage, image_rect)
        
        self.update = False
      
   

      pygame.display.update()
    pygame.quit()