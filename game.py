from bitBoard import BitBoard
import pygame



class Game:

  def __init__(self,screen_w, screen_h):

    self.width = screen_w
    self.height = screen_h

    self.running = True

    pygame.init()

    self.screen = pygame.display.set_mode((self.width, self.height))

    self.clock = pygame.time.Clock()



  def drawBoard(self):
    for row in range(8):
      for column in range(8):
        pygame.draw.rect(self.screen, (255,0,0), )
        pygame.

  def initGame(self):

    run = True

    while run:

      

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False

      pygame.display.update()
    pygame.quit()