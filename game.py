import sys
import random
import time

from vars import *


from snake import Snake
from food import Food
from menu import MainMenu


class Game:
    def __init__(self):
        self.initpygame()
        self.createDisplay()
        self.state = STATE_MAIN_MENU
        self.player = Snake()
        self.food = None
        self.menu = MainMenu()
        self.spawnfood()
        self.gameloop()
        self.renderableobjects = []

    def gameloop(self):
        while True:
            for event in pygame.event.get():
                self.handleEvent(event)
            self.update()
            self.render()

    def update(self):
        self.player.update(self.food)
        self.spawnfood()
        pass

    def render(self):
        self.window.fill(white)        
        self.player.render(self.window)
        self.food.render(self.window)
        self.menu.render(self.window)
        pygame.display.flip()
        self.fpsController.tick(24)
    

    def handleEvent(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            self.handleKeyEvent(event)

    def handleKeyEvent(self, event):
        pass

    def createDisplay(self):
        self.window = pygame.display.set_mode(display_size)
        pygame.display.set_caption('Snek !!')
        self.window.fill(white)
        pygame.display.flip()
        self.fpsController = pygame.time.Clock()

    def initpygame(self):
        pygame_error = pygame.init()
        if pygame_error[1] > 0:
            print('{} error while initializing pygame. exiting!!'.format(pygame_error[1]))
            sys.exit(1)
        else:
            print('PyGame initialized')

    def spawnfood(self):
        if self.food == None:
            randpos = [random.randrange(1, 72) * 10, random.randrange(1, 46)*10]
            self.food = Food(*randpos)

if __name__ == '__main__':
    game = Game()