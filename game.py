from bitBoard import BitBoard
import pygame


class Piece:

  def __init__(self):
    

class ChessBoard:

  def __init__(self, screen_w, screen_h, screen):
    self.screen = screen
    self.width = screen_w
    self.height = screen_h
    self.n = 8

  def drawCheckerBoardPattern(self):
    cell_w = self.width/self.n
    cell_h = self.height/self.n

    white = True
    for column in range(self.n):
      white = not white
      for row in range(self.n):
        sq_rect = pygame.Rect(cell_w*row, cell_h*column, cell_w, cell_h)
        if white:
          pygame.draw.rect(self.screen, (0,0,0), sq_rect)
        else:
          pygame.draw.rect(self.screen, (200,0,200), sq_rect)
        white = not white

  # def drawPieces(self):
   

class Game:

  def __init__(self,screen_w=800, screen_h=800):
    self.run = True
    pygame.init()
    self.screen = pygame.display.set_mode((screen_w, screen_h))
    self.clock = pygame.time.Clock()   
    self.cb = ChessBoard(screen_w,screen_h,self.screen)

  def initGame(self):

    self.cb.drawCheckerBoardPattern()
    while self.run:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.run = False

      pygame.display.update()
    pygame.quit()