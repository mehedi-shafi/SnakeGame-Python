#Snake Game!! Yay
#Made seeing a tutorial


#game imports
import pygame, sys, random, time

#initializing pygame
check_erro_pygame = pygame.init()

if check_erro_pygame[1] > 0 :
    print ("(!) Had {0} initializing errors, exiting", format (check_erro_pygame[1]))
    sys.exit(-1)
else :
    print ("(+) PyGame successfully initialized.")

#Display Initialization
playSurface = pygame.display.set_mode((720, 480))
pygame.display.set_caption('Hissssshhh')


#Colors
red = pygame.Color(255, 0, 0)
green = pygame.Color (0, 255, 0)
blue = pygame.Color(0, 0, 255)
black = pygame.Color (0, 0, 0)
white = pygame.Color (255, 255, 255)
brown = pygame.Color (165,42,42)
aqua = pygame.Color (0,255,255)

#game variables
snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]
snakeSpeed = 10
score = 0
choice = 2
gameStat = 'Menu'

foodPos = [random.randrange(1, 72)*10, random.randrange(1, 46)*10]
foodSpawn = True

direction = 'RIGHT'
changeTo = direction

#FPS controller
fpsController = pygame.time.Clock()

#Game over funtion
def gameOver() :
    myFont = pygame.font.SysFont('monaca', 72)
    GOsurf = myFont.render('Game Over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 20)
    playSurface.blit(GOsurf, GOrect)
    showScore(5)
    global choice
    choice = 2
    pygame.display.flip()
    time.sleep(5)
    global gameStat
    gameStat = 'Menu'


def showScore(choice) :
    scoreFont = pygame.font.SysFont('monaco', 24)
    Ssurf = scoreFont.render('Score : {0}'.format(score), True, red)
    Srect = Ssurf.get_rect()
    if choice == 1 and gameStat == 'Play':
        Srect.midtop = (80, 10)
    elif choice != 2:
        Srect.midtop = (360, 140)
    playSurface.blit(Ssurf, Srect)

def mainMenu() :
    global snakePos
    snakePos = [100, 50]
    global snakeBody
    while len(snakeBody) > 0 : snakeBody.pop()
    snakeBody = [[100, 50], [90, 50], [80, 50]]
    global score
    score = 0
    global choice
    choice = 2
    global direction
    direction = 'RIGHT'
    global changeTo
    changeTo = direction
    playSurface.fill(white)
    menuFont = pygame.font.SysFont('monaco', 30)
    menuSurf = menuFont.render('Snake Game. !! Play till you die', True, black)
    menuRect = menuSurf.get_rect()
    menuOptText = menuFont.render('1. Play \n2. Quit', True, black)
    menuOptRect = menuOptText.get_rect()
    menuOptRect.midtop = (360, 120)
    menuRect.midtop = (360, 50)
    playSurface.blit(menuSurf, menuRect)
    playSurface.blit (menuOptText, menuOptRect)
    choice = 2

#game function
while 1:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d') :
                changeTo = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a') :
                changeTo = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w') :
                changeTo = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s') :
                changeTo = 'DOWN'
            if event.key == pygame.K_ESCAPE :
                if gameStat == 'Play':
                    gameStat = 'Pause'
                elif gameStat == 'Pause' :
                    gameStat = 'Play'
                elif gameStat == 'GameOver' :
                    gameStat = 'Menu'
            if event.key == ord('1') :
                if gameStat == 'Menu' :
                    gameStat = 'Play'
                    choice = 1
            if event.key == ord ('2') :
                if gameStat == 'Menu' :
                    pygame.quit();
                    sys.exit()

    if gameStat == 'Play':
        #validation of direction
        if changeTo == 'RIGHT' and not direction == 'LEFT':
            direction = 'RIGHT'
        if changeTo == 'LEFT' and not direction == 'RIGHT':
            direction = 'LEFT'
        if changeTo == 'UP' and not direction == 'DOWN':
            direction = 'UP'
        if changeTo == 'DOWN' and not direction == 'UP':
            direction = 'DOWN'

        #snake position updating
        if direction == 'RIGHT':
            snakePos[0] += snakeSpeed
        if direction == 'LEFT':
            snakePos[0] -= snakeSpeed
        if direction == 'UP':
            snakePos[1] -= snakeSpeed
        if direction == 'DOWN':
            snakePos[1] += snakeSpeed

        print ('Direction: ' + direction + ' changeTo: ' + changeTo)
        print (snakeBody)

        #Snake body mechanism
        snakeBody.insert(0, list(snakePos))
        if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
            score += 1
            foodSpawn = False
        else :
            snakeBody.pop()

        if foodSpawn == False :
            foodPos = [random.randrange(1, 72)*10, random.randrange(1, 46)*10]
            foodSpawn = True

        playSurface.fill(white)
        for pos in snakeBody:
            pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect (playSurface, brown, pygame.Rect (foodPos[0], foodPos[1], 10, 10))
        if snakePos[0] > 715 or snakePos[0] < 0:
            gameOver()
        if snakePos[1] > 475 or snakePos[1] < 0:
            gameOver()

        for block in snakeBody[1 : ]:
            if snakePos[0] == block[0] and snakePos[1] == block[1] :
                gameOver()
        showScore(1)

    elif gameStat == 'Menu' :
        mainMenu()

    pygame.display.flip()
    fpsController.tick(18)
