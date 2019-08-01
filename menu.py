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
        menuRect.midtop = (360, 200)

        menuOptText = menuFont.render('1. Play', True, black)
        menuOptRect = menuOptText.get_rect()
        menuOptRect.midtop = (360, 240)
        
        menuOptText2 = menuFont.render('2. Quit', True, black)
        menuOptRect2 = menuOptText.get_rect()
        menuOptRect2.midtop = (360, 270)       
        

        creditfont = pygame.font.SysFont('monaco', 18)
        credit = creditfont.render('https://github.com/mehedi-shafi', True, black)
        creditRect = credit.get_rect()
        creditRect.midtop = (610, 460)

        window.blit(menuSurf, menuRect)
        window.blit (menuOptText, menuOptRect)
        window.blit(menuOptText2, menuOptRect2)
        window.blit(credit, creditRect)

