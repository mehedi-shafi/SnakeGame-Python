import sys
import random
import time

from vars import *


from snake import Snake
from food import Food
from menu import MainMenu
from hud import HUD


class Game:
    def __init__(self):
        self.initpygame()
        self.createDisplay()
        self.state = STATE_MAIN_MENU
        self.menu = MainMenu()
        self.gameloop()

    def gameloop(self):
        while True:
            for event in pygame.event.get():
                self.handleEvent(event)
            self.update()
            self.render()

    def update(self):
        if self.state == STATE_PLAY:
            self.player.update()
            self.eatFood()
            self.spawnfood()
            self.hud.update(self)
            if self.player.GAME_OVER:
                self.state = STATE_GAME_OVER
        if self.state == STATE_PAUSE:
            self.hud.update(self)
        if self.state == STATE_GAME_OVER:
            self.hud.update(self)
    
    def gameover(self):
        self.player = None
        self.food = None
        self.hud = None
        self.state = STATE_MAIN_MENU
        

    def eatFood(self):
        if self.food.posx == self.player.head_pos[0] and self.food.posy == self.player.head_pos[1]:
            self.player.eat()
            self.food = None
        else:
            self.player.body.pop()

    def render(self):
        self.window.fill(white)        
        if self.state == STATE_PLAY:
            self.player.render(self.window)
            self.food.render(self.window)
            self.hud.render(self.window)
        if self.state == STATE_PAUSE:
            self.player.render(self.window)
            self.food.render(self.window)
            self.hud.render(self.window)
        if self.state == STATE_MAIN_MENU:
            self.menu.render(self.window)
        if self.state == STATE_GAME_OVER:
            self.hud.render(self.window)
        
        pygame.display.flip()
        self.fpsController.tick(15)
    

    def handleEvent(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            self.handleKeyEvent(event.key)

    def handleKeyEvent(self, keyPressed):
        if self.state == STATE_GAME_OVER:
            self.gameover()

        if self.state == STATE_PLAY:
            if keyPressed == pygame.K_RIGHT or keyPressed == pygame.K_d:
                self.player.move(RIGHT)
            if keyPressed == pygame.K_LEFT or keyPressed == pygame.K_a:
                self.player.move(LEFT)
            if keyPressed == pygame.K_UP or keyPressed == pygame.K_w:
                self.player.move(UP)
            if keyPressed == pygame.K_DOWN or keyPressed == pygame.K_s:
                self.player.move(DOWN)
        if self.state == STATE_MAIN_MENU:
            if keyPressed == pygame.K_1:
                if self.state == STATE_MAIN_MENU:
                    self.newgame()
            if keyPressed == pygame.K_2:
                if self.state == STATE_MAIN_MENU:
                    sys.exit()
        if keyPressed == pygame.K_ESCAPE:
            if self.state == STATE_PLAY:
                self.pause()
            elif self.state == STATE_PAUSE:
                self.resume()                

    def pause(self):
        self.state = STATE_PAUSE        

    def resume(self):
        self.state = STATE_PLAY        

    def newgame(self):
        self.player = Snake()
        self.food = None
        self.hud = HUD()
        self.spawnfood()
        self.state = STATE_PLAY
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