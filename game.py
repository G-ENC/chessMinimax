import pygame
import numpy as np 
from bitUtil import *
from pieces import *
from cosntants import * 
from pieces import *
from tables import *
from chessBoard import ChessBoard


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
          #not holding any object
          if self.holdPiece == None:
            # if the selected piece exists in that square and the it is that players turn accept the selection
            if self.cb.getObjectByIndex(selected_index)!=None and self.cb.getObjectByIndex(selected_index).color == self.cb.side:
              self.holdPieceIndex = selected_index
              self.holdPiece = self.cb.popAndGetSelectedPiece(selected_index)
          #holding piece
          else:
            #placement in the same square doesnt passesd the turn
            if self.holdPieceIndex == selected_index:
              self.cb.putPieceToSquare(self.holdPiece,selected_index)
              self.holdPiece = None
              self.holdPieceIndex = None
            #if the placedf piece is in a diffent location the turn is finished
            elif self.holdPieceIndex != selected_index:
              self.cb.putPieceToSquare(self.holdPiece,selected_index)
              self.holdPiece = None
              self.holdPieceIndex = None
              self.cb.nextPlayerTurn()

      #update screen
      if self.update:
        
        # printBitBoard(self.cb.whitePawn.bitmap)
        self.cb.drawCheckerBoardPattern()
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