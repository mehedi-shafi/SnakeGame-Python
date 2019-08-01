from vars import *

class Snake:
    def __init__(self):
        self.head_pos = [display_size[0]//2, display_size[1]//2]
        self.body = self.createbody()
        self.speed = initalspeed
        self.size = len(self.body)
        self.direction = RIGHT
        self.GAME_OVER = False
        self.score = 0

    def move(self, shiftTo):
        if self.validmove(shiftTo):
            self.direction = shiftTo
        pass

    def validmove(self, shiftTo):
        if self.direction == LEFT and shiftTo == RIGHT:
            return False
        if self.direction == RIGHT and shiftTo == LEFT:
            return False
        if self.direction == UP and shiftTo == DOWN:
            return False
        if self.direction == DOWN and shiftTo == UP:
            return False
        return True

    def eat(self):
        self.score += 1
        self.size = len(self.body)

    def update(self):
        if self.direction == RIGHT: 
            self.head_pos[0] += self.speed
        if self.direction == LEFT:
            self.head_pos[0] -= self.speed
        if self.direction == UP:
            self.head_pos[1] -= self.speed
        if self.direction == DOWN:
            self.head_pos[1] += self.speed
        self.body.insert(0, list(self.head_pos))
        self.checkgameover()

    def checkgameover(self):
        if (self.head_pos[0] >= display_size[0] or self.head_pos[0] <= 0):
            self.GAME_OVER = True
        if (self.head_pos[1] >= display_size[1] or self.head_pos[1] <= 0):
            self.GAME_OVER = True
        for block in self.body[1 : ]:
            if self.head_pos[0] == block[0] and self.head_pos[1] == block[1]:
                self.GAME_OVER = True

    def render(self, window):
        for snakeBit in self.body:
            pygame.draw.rect(window, green, pygame.Rect(*snakeBit, blockSize, blockSize))
        pass
    
    def __del__(self):
        pass

    def createbody(self):
        trail = [[self.head_pos[0], self.head_pos[1]]]
        for i in range(initialSnakeLength-1):
            trail.append([trail[i][0]-blockDistance, trail[i][1]])
        return trail