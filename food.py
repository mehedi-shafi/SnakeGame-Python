from vars import *

class Food:
    def __init__(self, x, y):
        self.posx = x
        self.posy = y
        self.point = 1
        self.size = blockSize

    def render(self, window):
        pygame.draw.rect(window, brown, 
                        pygame.Rect(self.posx, 
                                    self.posy, 
                                    self.size, 
                                    self.size))