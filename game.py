import pygame
import numpy as np 
np.seterr(over='ignore')
from bitUtil import *
from pieces import *
from cosntants import * 
from pieces import *
from tables import *
from chessBoard import ChessBoard
from movegen import *




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


  #draw functions
  def drawCheckerBoardPattern(self):
    white = True
    for column in range(self.cb.n):
      white = not white
      for row in range(self.cb.n):
        sq_rect = pygame.Rect(self.cb.cell_w*row, self.cb.cell_h*column, self.cb.cell_w, self.cb.cell_h)
        if white:
          pygame.draw.rect(self.screen, (50,50,50), sq_rect)
        else:
          pygame.draw.rect(self.screen, (200,0,200), sq_rect)
        white = not white

  def initGame(self):
    self.cb.nextPlayerTurn()
    
    while self.run:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.run = False

        elif event.type == pygame.MOUSEMOTION:#update the screen so that the piece follows the cursor
          self.update = True

        elif event.type == pygame.MOUSEBUTTONDOWN:#hold the piece if not holding already
          mouse_location = pygame.mouse.get_pos()
          selected_index = int(self.cb.getScreenCoordinatesToIndex(mouse_location))
          if self.holdPiece == None:#not holding any piece object
            if self.cb.getObjectByIndex(selected_index)!=None and self.cb.getObjectByIndex(selected_index).color == self.cb.side:# if the selected piece exists in that square and the it is that players turn accept the selection
              self.holdPieceIndex = selected_index
              self.holdPiece = self.cb.popAndGetSelectedPiece(selected_index)
              print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
              for move in generateAllMoves(self.cb):
                print(f"{move}")
          else:#holding piece
            if self.holdPieceIndex == selected_index:#placement in the same square doesnt passesd the turn
              self.cb.putPieceToSquare(self.holdPiece,selected_index)
              self.holdPiece = None
              self.holdPieceIndex = None
            elif self.holdPieceIndex != selected_index:#if the placedf piece is in a diffent location the turn is finished
              self.cb.putPieceToSquare(self.holdPiece,selected_index)
              self.holdPiece = None
              self.holdPieceIndex = None
              self.cb.nextPlayerTurn()
          self.update = True

      #update screen
      if self.update:
        
        # printBitBoard(self.cb.whitePawn.bitmap)
        self.drawCheckerBoardPattern()
        self.cb.drawAllPieces()

        if self.holdPiece != None:
          self.cb.drawAllAttackSquares()
          holdPieceImage = self.cb.getPieceImage(self.holdPiece)
          m_pos = pygame.mouse.get_pos()
          image_rect = holdPieceImage.get_rect(center=m_pos)
          self.screen.blit(holdPieceImage, image_rect)
        
        self.update = False
      
   

      pygame.display.update()
    pygame.quit()