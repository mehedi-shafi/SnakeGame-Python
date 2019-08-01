# all game variables
import pygame

# direction
LEFT = 'LEFT'
RIGHT = 'RIGHT'
UP = 'UP'
DOWN = 'DOWN'

display_size = (720, 480)

blockDistance = 10
blockSize = 10

snakePos = [100, 50]
initialSnakeLength = 5
snakeBody = [[100, 50], [90, 50], [80, 50]]
initalspeed = 10
score = 0
choice = 2
gameStat = 'Menu'

# Colors
red = pygame.Color(255, 0, 0)
green = pygame.Color (0, 255, 0)
blue = pygame.Color(0, 0, 255)
black = pygame.Color (0, 0, 0)
white = pygame.Color (255, 255, 255)
brown = pygame.Color (165,42,42)
aqua = pygame.Color (0,255,255)


# game states
STATE_PLAY = 'PLAY'
STATE_PAUSE = 'PAUSE'
STATE_GAME_OVER = 'GAME_OVER'
STATE_MAIN_MENU = 'MENU'