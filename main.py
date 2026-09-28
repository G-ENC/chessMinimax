from game import Game

#change screen dimentions based on personal computers
linux = True
dim = (1000,1000)
if not linux:
  dim = (600,600)

if __name__ == "__main__":
  game = Game(dim[0],dim[1])
  game.initGame()