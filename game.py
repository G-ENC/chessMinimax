from bitBoard import BitBoard
import pygame



class Game:

  def __init__(self,screen_w=800, screen_h=800):


    self.width = screen_w
    self.height = screen_h

    self.run = True

    pygame.init()

    self.screen = pygame.display.set_mode((self.width, self.height))

    self.clock = pygame.time.Clock()



  def drawCheckerBoardPattern(self, n=8):
    cell_w = self.width/n
    cell_h = self.height/n

    white = True
    for column in range(n):
      white = not white
      for row in range(n):
        sq_rect = pygame.Rect(cell_w*row, cell_h*column, cell_w, cell_h)
        if white:
          pygame.draw.rect(self.screen, (0,0,0), sq_rect)
        else:
          pygame.draw.rect(self.screen, (200,0,200), sq_rect)
        white = not white

  def initGame(self):

    self.drawCheckerBoardPattern()

    while self.run:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.run = False

      pygame.display.update()
    pygame.quit()