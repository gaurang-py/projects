import random #to build randomnes
import sys #  to exit the program
import pygame
from pygame.locals import * 

# Global Variables 
FPS = 30
width = 1000
height = 570
SCREEN = pygame.display.set_mode((width, height))
y = height
game_image = {}
game_sounds = {}
PLAYER = 'images/bee.png'
BACKGROUND = 'images/forest.png'
log = 'images/log.png'





def welcomeScreen():

    #Shows welcome images on the screen


    playerx = int(width/5)
    playery = int((height - game_image['player'].get_height())/2)
    messagex = int((width - game_image['message'].get_width())/2)
    messagey = int(height*0.13)
    basex = 0
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game for them
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(game_image['background'], (0, 0))    
                SCREEN.blit(game_image['player'], (playerx, playery))    
                SCREEN.blit(game_image['message'], (0,0))    
                SCREEN.blit(game_image['base'], (basex,450))    
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def mainGame():
    score = 0
    playerx = int(170)
    playery = int(425)
    basex = 0

    # Create 2 logs for blitting on the screen
    newlog1 = getRandomlog()
    newlog2 = getRandomlog()

    # my List of upper -logs
    
    upperlogs = [
        {'x':  1050, 'y':newlog1[0]['y']},
        {'x':  1050+( 425), 'y':newlog2[0]['y']},
    ]
    # my List of lower logs
    lowerlogs = [

        {'x':  1050, 'y':newlog1[1]['y']},
        {'x':  1050+( 425), 'y':newlog2[1]['y']},
    ]

    logVelX = -4 

    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1

    playerFlapAccv = -8 #velocity while flapping
    playerFlapped = False # It is true only when the bird is flapping


    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    game_sounds['wing'].play()


        crashTest = isCollide(playerx, playery, upperlogs, lowerlogs) # This function will return true if the player is crashed
        if crashTest:
            return     

        #check for score
        playerMidPos = playerx + game_image['player'].get_width()/2
        for log in upperlogs:
            logMidPos = log['x'] + game_image['log'][0].get_width()/2
            if logMidPos<= playerMidPos < logMidPos +4:
                score +=1
                highscore=0
                if score > highscore :
                    highscore=score
                    
                    
                    
                print("Your score is ",score)
                
                game_sounds['point'].play()
                print("Your highscore", highscore)

        if playerVelY <playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False            
        playerHeight = game_image['player'].get_height()
        playery = playery + min(playerVelY, y - playery - playerHeight)

        # move logs to the left
        for upperlog , lowerlog in zip(upperlogs, lowerlogs):
            upperlog['x'] += logVelX
            lowerlog['x'] += logVelX

        # Add a new log when the first is about to cross the leftmost part of the screen
        if 0<upperlogs[0]['x']<5:
            newlog = getRandomlog()
            upperlogs.append(newlog[0])
            lowerlogs.append(newlog[1])

        # if the log is out of the screen, remove it
        if upperlogs[0]['x'] < -game_image['log'][0].get_width():
            upperlogs.pop(0)
            lowerlogs.pop(0)
        
        # Lets blit our sprites now
        SCREEN.blit(game_image['background'], (0, 0))
        for upperlog, lowerlog in zip(upperlogs, lowerlogs):
            SCREEN.blit(game_image['log'][0], (upperlog['x'], upperlog['y']))
            SCREEN.blit(game_image['log'][1], (lowerlog['x'], lowerlog['y']))

        SCREEN.blit(game_image['base'], (basex, y))
        SCREEN.blit(game_image['player'], (playerx, playery))
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += game_image['numbers'][digit].get_width()
        Xoffset = (width - width)/2

        for digit in myDigits:
            SCREEN.blit(game_image['numbers'][digit], (Xoffset, height*0.12))
            Xoffset += game_image['numbers'][digit].get_width()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def isCollide(playerx, playery, upperlogs, lowerlogs):
    if playery> y - 25  or playery<0:
        game_sounds['hit'].play()
        return True
    
    for log in upperlogs:
        logHeight = game_image['log'][0].get_height()
        if(playery < logHeight + log['y'] and abs(playerx - log['x']) < game_image['log'][0].get_width()):
            game_sounds['hit'].play()
            return True

    for log in lowerlogs:
        if (playery + game_image['player'].get_height() > log['y']) and abs(playerx - log['x']) < game_image['log'][0].get_width():
            game_sounds['hit'].play()
            return True

    return False

def getRandomlog():
    """
    Generate positions of two logs(one bottom straight and one top rotated ) for blitting on the screen
    """
    logHeight = game_image['log'][0].get_height()
    offset = height/3
    y2 = offset + random.randrange(0, int(height - game_image['base'].get_height()  - 1.3 *offset))
    logX = width + 10
    y1 = logHeight - y2 + offset
    log = [
        {'x': logX, 'y': -y1}, #upper log
        {'x': logX, 'y': y2} #lower log
    ]
    
    return log
if __name__ == "__main__":
    pygame.init() # Initialize all pygame's modules
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy BEE BY FUN EITH PYTON')
    game_image['numbers'] = ( 
        pygame.image.load('images/0.png').convert_alpha(),
        pygame.image.load('images/1.png').convert_alpha(),
        pygame.image.load('images/2.png').convert_alpha(),
        pygame.image.load('images/3.png').convert_alpha(),
        pygame.image.load('images/4.png').convert_alpha(),
        pygame.image.load('images/5.png').convert_alpha(),
        pygame.image.load('images/6.png').convert_alpha(),
        pygame.image.load('images/7.png').convert_alpha(),
        pygame.image.load('images/8.png').convert_alpha(),
        pygame.image.load('images/9.png').convert_alpha(),
    )

    game_image['message'] =pygame.image.load('images/message.png').convert_alpha()
    game_image['base'] =pygame.image.load('images/base.png').convert_alpha()
    game_image['log'] =(pygame.transform.rotate(pygame.image.load(log).convert_alpha(), 180), 
    pygame.image.load(log).convert_alpha()
    )

    # Game sounds
    game_sounds['die'] = pygame.mixer.Sound('sounds/die.wav')
    game_sounds['hit'] = pygame.mixer.Sound('sounds/hit.wav')
    game_sounds['point'] = pygame.mixer.Sound('sounds/point.wav')
    game_sounds['swoosh'] = pygame.mixer.Sound('sounds/swoosh.wav')
    game_sounds['wing'] = pygame.mixer.Sound('sounds/wing.wav')

    game_image['background'] = pygame.image.load(BACKGROUND).convert()
    game_image['player'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen() # Shows welcome screen to the user until he presses a button
        mainGame() # This is the main game function 







