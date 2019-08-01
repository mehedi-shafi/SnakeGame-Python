from vars import *

class HUD:
    def __init__(self):
        self.hudfont = pygame.font.SysFont('monaco', 24)
        self.hud_score = self.hudfont.render('Score: {}'.format(0), True, red)
        self.hud_score_rect = self.hud_score.get_rect()
        self.hud_score_rect.midtop = (360, 20)
        
        self.hud_game_state = self.hudfont.render('{}'.format('PLAY'), True, black)
        self.hud_game_state_rect = self.hud_game_state.get_rect()
        self.hud_game_state_rect.midtop = (660, 20)
        self.GAME_OVER = False
        
    def update(self, game):
        self.hud_game_state = self.hudfont.render('{}'.format(game.state), True, black)
        self.hud_game_state_rect = self.hud_game_state.get_rect()
        if game.state == STATE_PAUSE:
            self.hud_game_state_rect.midtop = (360, 240)
        elif game.state == STATE_PLAY:
            self.hud_game_state_rect.midtop = (660, 20)
        elif game.state == STATE_GAME_OVER:
            ggfont = pygame.font.SysFont('monaco', 72)
            self.hud_game_state = ggfont.render('Game Over', True, red)
            self.hud_game_state_rect = self.hud_game_state.get_rect()
            self.hud_game_state_rect.midtop = (360, 200)
            self.GAME_OVER = True

        self.hud_score = self.hudfont.render('Score: {}'.format(game.player.score), True, red)
        self.hud_score_rect = self.hud_score.get_rect()
        self.hud_score_rect.midtop = (360, 20)

    def render(self, window):
        window.blit(self.hud_score, self.hud_score_rect)
        window.blit(self.hud_game_state, self.hud_game_state_rect)
        if self.GAME_OVER:
            gg_text = self.hudfont.render('GG WP. Press any key to continue', True, black)
            gg_rect = gg_text.get_rect()
            gg_rect.midtop = (360, 260)
            window.blit(gg_text, gg_rect)