from vars import *

class MainMenu:
    def __init__(self):
        pass

    def update(self):
        pass

    def render(self, window):
        menuFont = pygame.font.SysFont('monaco', 30)
        menuSurf = menuFont.render('Snake Game!!', True, black)
        menuRect = menuSurf.get_rect()
        menuOptText = menuFont.render('1. Play \n2. Quit', True, black)
        menuOptRect = menuOptText.get_rect()
        menuOptRect.midtop = (360, 120)
        menuRect.midtop = (360, 50)
        window.blit(menuSurf, menuRect)
        window.blit (menuOptText, menuOptRect)