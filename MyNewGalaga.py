
import pygame
import vlc
import random
import time
run = True
print("welcome to my pygame!")
print("use asd to move around and w to shoot")

#MUSIC//////////////////////
intromusic = vlc.MediaPlayer("/Users/johnlawall/Desktop/01 Stage Intro.mp3")
lasersound = vlc.MediaPlayer('/Users/johnlawall/Downloads/laser sound.mp3.mov')
enemydiesound = vlc.MediaPlayer("/Users/johnlawall/Library/Mobile Documents/com~apple~QuickTimePlayerX/Documents/enemydie.mov")

intromusic.play()
#Will load the pygame objects into your RAM
pygame.init()
#Sets a window size for the game
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

#Creates a clock
#Used to slow down frames per second (FPS)
clock = pygame.time.Clock()

#Sets the window title for the game (optional)
pygame.display.set_caption("Galaga")

#VARIABLES
playerX = 300
playerY = 550
player_v = 7

enemy1_v = 4
enemy2_v = 4
enemy3_v = 4
enemy4_v = 3
enemy5_v = 3
enemy6_v = 3

laserX = 0
laserY = 0
laser_v = 1

laser2X = 0
laser2Y = 0

score = 0
attack = 0
countfire = 0

#BOSS///////////////////
boss_img = 0
boss = 0
boss_v = 5
bossHP = 10
bossloadnum = 0
fireballX = 0
fireballY = 0



global player, laser, laser_img, laser2, laser_img2
laser = 0

laser_img = pygame.image.load('/Users/johnlawall/Library/Mobile Documents/com~apple~Preview/Documents/laser.png')

laser = laser_img.get_rect(x= -1000 ,y= -100)

laser2 = 0
laser_img2 = pygame.image.load('/Users/johnlawall/Library/Mobile Documents/com~apple~Preview/Documents/laser.png')
laser2 = laser_img2.get_rect(x= 1000 ,y= -100)

#player ship
player_img = pygame.image.load('/Users/johnlawall/Library/Mobile Documents/com~apple~Preview/Documents/player ship.png')
player = player_img.get_rect(x = playerX, y = playerY)

#enemy ships
# ROW 1 
enemy1_img = pygame.image.load('/Users/johnlawall/Library/Mobile Documents/com~apple~Preview/Documents/enemy ship.png')
enemy1 = enemy1_img.get_rect(x=100, y=50)

enemy2_img = pygame.image.load('/Users/johnlawall/Library/Mobile Documents/com~apple~Preview/Documents/enemy ship.png')
enemy2= enemy2_img.get_rect(x=200, y= 50)

enemy3_img = pygame.image.load('/Users/johnlawall/Library/Mobile Documents/com~apple~Preview/Documents/enemy ship.png')
enemy3 = enemy3_img.get_rect(x=300, y=50)

#ROW 2
enemy4_img = pygame.image.load('/Users/johnlawall/Library/Mobile Documents/com~apple~Preview/Documents/enemy ship.png')
enemy4 = enemy4_img.get_rect(x=100, y=125)

enemy5_img = pygame.image.load('/Users/johnlawall/Library/Mobile Documents/com~apple~Preview/Documents/enemy ship.png')
enemy5= enemy5_img.get_rect(x=200, y= 125)

enemy6_img = pygame.image.load('/Users/johnlawall/Library/Mobile Documents/com~apple~Preview/Documents/enemy ship.png')
enemy6 = enemy6_img.get_rect(x=300, y= 125)

boss_img = pygame.image.load('/Users/johnlawall/Documents/bossboi1 copy.png')
boss = boss_img.get_rect(x= 700 ,y= 50)

fireball_img = pygame.image.load('/Users/johnlawall/Downloads/fireballl.png')


fireball = fireball_img.get_rect(x = 700, y = 100)

bossX = boss.x
bossY = boss.y
fireshot = 0




def updateScore():
    global score
    score_display = "Score: " + str(score)
    font = pygame.font.Font('freesansbold.ttf', 22)
    score_text_img = font.render(score_display, True, (225, 225, 225), (0, 0, 0))
    score_text = score_text_img.get_rect()
    score_text.x = 500
    score_text.y = 575
    screen.blit(score_text_img, score_text)
def bossshoot():
    global fireball, fireball2, fireball3, bossX, bossY, fireshot, fireballX, fireballY
    #fireball_img = pygame.image.load('/Users/johnlawall/Downloads/fireballl.png')



    fireball.x = boss.x +boss.width /2
    fireball.y = boss.y
    #fireball_img = pygame.image.load('/Users/johnlawall/Downloads/fireballl.png')
    #fireball = fireball_img.get_rect(x= fireballX ,y= fireballY)




def Boss():
    global bossHP, bossY
    if score >= 6:

        if 9 >= bossHP >= 1:
            if player.x + player.width/2 > boss.x +boss.width /2:
                boss.x += 3
            if player.x + player.width/2 < boss.x +boss.width /2:
                boss.x -= 3
            bossY += boss_v
        if countfire == 200:
            bossshoot()
        if countfire == 250:
            bossshoot()
        if countfire == 300:
            bossshoot()
        if countfire == 350:
            bossshoot()
        if countfire == 400:
            bossshoot()
        if countfire == 450:
            bossshoot()
        if countfire == 500:
            bossshoot()
        if countfire == 550:
            bossshoot()
        if countfire == 600:
            bossshoot()
        if countfire == 650:
            bossshoot()
        if countfire == 700:
            bossshoot()
        if countfire == 750:
            bossshoot()
        if countfire == 800:
            bossshoot()
        if countfire == 850:
            bossshoot()
        if countfire == 900:
            bossshoot()
        if countfire == 950:
            bossshoot()

    #if fireball.y >= 600 or fireball.y <= 0:
                #lasersound = vlc.MediaPlayer('/Users/johnlawall/Downloads/laser sound.mp3.mov')
                #lasersound.play()
     #   bossshoot()





def bossAI():
    global boss_v

    if boss.x > 300:
        boss_v = -boss_v

    if boss.x < 0:
        boss_v = abs(boss_v)

    boss.x += boss_v


def handle_collisions():
    global score, laser, laser2, player, enemy1, enemy2, enemy3, bossHP, bossloadnum, bossY, bossX, playerY
    if laser != 0:
        if laser.colliderect(enemy1):
            enemydiesound = vlc.MediaPlayer("/Users/johnlawall/Library/Mobile Documents/com~apple~QuickTimePlayerX/Documents/enemydie.mov")
            enemydiesound.play()

            enemy1.y = 1000
            laser.x = -100
            score += 1


        if laser.colliderect(enemy2):
            enemydiesound = vlc.MediaPlayer("/Users/johnlawall/Library/Mobile Documents/com~apple~QuickTimePlayerX/Documents/enemydie.mov")
            enemydiesound.play()
            enemy2.y = 1000
            laser.x = -100
            score += 1


        if laser.colliderect(enemy3):
            enemydiesound = vlc.MediaPlayer("/Users/johnlawall/Library/Mobile Documents/com~apple~QuickTimePlayerX/Documents/enemydie.mov")
            enemydiesound.play()
            enemy3.y = 1000
            laser.x = -100
            score += 1

        if laser.colliderect(enemy4):
            enemydiesound = vlc.MediaPlayer("/Users/johnlawall/Library/Mobile Documents/com~apple~QuickTimePlayerX/Documents/enemydie.mov")
            enemydiesound.play()
            enemy4.y = 1000
            laser.x = -100
            score += 1

        if laser.colliderect(enemy5):
            enemydiesound = vlc.MediaPlayer("/Users/johnlawall/Library/Mobile Documents/com~apple~QuickTimePlayerX/Documents/enemydie.mov")
            enemydiesound.play()
            enemy5.y = 1000
            laser.x = -100
            score += 1


        if laser.colliderect(enemy6):
            enemydiesound = vlc.MediaPlayer("/Users/johnlawall/Library/Mobile Documents/com~apple~QuickTimePlayerX/Documents/enemydie.mov")
            enemydiesound.play()
            enemy6.y = 1000
            laser.x = -100
            score += 1
        if laser.colliderect(boss):
            bossHP -= 1
            if bossHP <= 0:
                score +=7

                boss.y = 1000
            laser.x = -100

    if laser2 != 0:
        if laser2.colliderect(enemy1):
            enemydiesound = vlc.MediaPlayer("/Users/johnlawall/Library/Mobile Documents/com~apple~QuickTimePlayerX/Documents/enemydie.mov")
            enemydiesound.play()
            enemy1.y = 1000
            laser2.x = -100
            score += 1


        if laser2.colliderect(enemy2):
            enemydiesound = vlc.MediaPlayer("/Users/johnlawall/Library/Mobile Documents/com~apple~QuickTimePlayerX/Documents/enemydie.mov")
            enemydiesound.play()
            enemy2.y = 1000
            laser2.x = -100
            score += 1


        if laser2.colliderect(enemy3):
            enemydiesound = vlc.MediaPlayer("/Users/johnlawall/Library/Mobile Documents/com~apple~QuickTimePlayerX/Documents/enemydie.mov")
            enemydiesound.play()
            enemy3.y = 1000
            laser2.x = -100
            score += 1

        if laser2.colliderect(enemy4):
            enemydiesound = vlc.MediaPlayer("/Users/johnlawall/Library/Mobile Documents/com~apple~QuickTimePlayerX/Documents/enemydie.mov")
            enemydiesound.play()
            enemy4.y = 1000
            laser2.x = -100
            score += 1


        if laser2.colliderect(enemy5):
            enemydiesound = vlc.MediaPlayer("/Users/johnlawall/Library/Mobile Documents/com~apple~QuickTimePlayerX/Documents/enemydie.mov")
            enemydiesound.play()
            enemy5.y = 1000
            laser2.x = -100
            score += 1


        if laser2.colliderect(enemy6):
            enemydiesound = vlc.MediaPlayer("/Users/johnlawall/Library/Mobile Documents/com~apple~QuickTimePlayerX/Documents/enemydie.mov")
            enemydiesound.play()
            enemy6.y = 1000
            laser2.x = -100
            score += 1


        if score >= 6 and bossloadnum ==0:


            boss.x -= 3

            if boss.x < 300:

                bossloadnum += 1








        if laser2.colliderect(boss):
            bossHP -= 1
            if bossHP <= 0:
                score += 1

                boss.y = 1000
            laser2.x = -100
    if fireball.colliderect(player):
        playerY = 1000


def gameovertext():
    if score == 0:

        win_display2 = "GAME OVER"
        font2 = pygame.font.Font('freesansbold.ttf', 30)
        win_text_img2 = font2.render(win_display2, True, (255, 255, 255), (0, 0, 0))
        win_text2 = win_text_img2.get_rect()
        win_text2.x = 225
        win_text2.y = 300
gameovertext()
def playerdeath():
    global playerY

    if enemy1.colliderect(player):
        playerY = 100000
        explosion = vlc.MediaPlayer("/Users/johnlawall/Downloads/09 Die-Start Up Sound.mp3")
        explosion.play()
        gameovertext()
        run = False
    if player.colliderect(enemy2):
        playerY = 100000
        explosion = vlc.MediaPlayer("/Users/johnlawall/Downloads/09 Die-Start Up Sound.mp3")
        explosion.play()
        gameovertext()
        run = False
    if player.colliderect(enemy3):
        playerY = 100000
        explosion = vlc.MediaPlayer("/Users/johnlawall/Downloads/09 Die-Start Up Sound.mp3")
        explosion.play()
        gameovertext()
        run = False
    if player.colliderect(enemy4):
        playerY = 100000
        explosion = vlc.MediaPlayer("/Users/johnlawall/Downloads/09 Die-Start Up Sound.mp3")
        explosion.play()
        gameovertext()
        run = False
    if player.colliderect(enemy5):
        playerY = 100000
        explosion = vlc.MediaPlayer("/Users/johnlawall/Downloads/09 Die-Start Up Sound.mp3")
        explosion.play()
        gameovertext()
        run = False
    if enemy6.colliderect(player):
        playerY = 100000
        explosion = vlc.MediaPlayer("/Users/johnlawall/Downloads/09 Die-Start Up Sound.mp3")
        explosion.play()
        gameovertext()
        run = False



#def Boss():
# if score == 6:
#  boss_img = pygame.image.load('bossboi.png')
# boss = boss_img.get_rect(x= 300 ,y= 100)
#screen.blit(boss_img, boss)




def shoot():
    global laser, laserX, laserY

    laserX = playerX + player.width/2 -5
    laserY = playerY - player.height
    laser_img = pygame.image.load('/Users/johnlawall/Library/Mobile Documents/com~apple~Preview/Documents/laser.png')
    laser = laser_img.get_rect(x= laserX ,y= laserY)


def shoot2():

    global laser2, laser2X, laser2Y


    laser2X = playerX + player.width/2 -5
    laser2Y = playerY - player.height
    laser_img2 = pygame.image.load('/Users/johnlawall/Library/Mobile Documents/com~apple~Preview/Documents/laser.png')
    laser2 = laser_img.get_rect(x= laser2X ,y= laser2Y)


def enemy_movment():
    global enemy1_v, enemy2_v, enemy3_v, enemy4_v, enemy5_v, enemy6_v
    if attack < 500:

        if enemy1.x > 300:
            enemy1_v = -enemy1_v

        if enemy1.x < 0:
            enemy1_v = abs(enemy1_v)

        enemy1.x += enemy1_v

    if attack > 500 and enemy1.y < 900:
        if player.y > enemy1.y:
            enemy1.y += 5
        if player.x > enemy1.x:
            enemy1.x += 2
        if player.x < enemy1.x:
            enemy1.x -= 2
    #enemy2
    if attack < 700:
        if enemy2.x > 400:
            enemy2_v = -enemy2_v

        if enemy2.x < 100:
            enemy2_v = abs(enemy2_v)

        enemy2.x += enemy2_v
    if attack > 700 and enemy2.y < 900:
        if player.y > enemy2.y:
            enemy2.y += 5
        if player.x > enemy2.x:
            enemy2.x += 2
        if player.x < enemy2.x:
            enemy2.x -= 2
    #enemy3


    if attack < 750:
        if enemy3.x > 500:
            enemy3_v = -enemy3_v

        if enemy3.x < 200:
            enemy3_v = abs(enemy3_v)
        enemy3.x += enemy3_v


    if attack > 750 and enemy3.y < 900:
        if player.y > enemy3.y:
            enemy3.y += 5
        if player.x > enemy3.x:
            enemy3.x += 3
        if player.x < enemy3.x:
            enemy3.x -= 3


    #enemy4
    if attack < 800:
        if enemy4.x > 300:
            enemy4_v = -enemy4_v

        if enemy4.x < 0:
            enemy4_v = abs(enemy4_v)

        enemy4.x += enemy4_v
    if attack > 800 and enemy4.y < 900:
        if player.y > enemy4.y:
            enemy4.y += 5
        if player.x > enemy4.x:
            enemy4.x += 2
        if player.x < enemy4.x:
            enemy4.x -= 2


    #enemy5
    if attack < 900:
        if enemy5.x > 400:
            enemy5_v = -enemy5_v

        if enemy5.x < 100:
            enemy5_v = abs(enemy5_v)

        enemy5.x += enemy5_v
    if attack > 900 and enemy5.y < 900:
        if player.y > enemy5.y:
            enemy5.y += 5
        if player.x > enemy5.x:
            enemy5.x += 2
        if player.x < enemy5.x:
            enemy5.x -= 2
    #enemy6
    if attack < 950:
        if enemy6.x > 500:
            enemy6_v = -enemy6_v

        if enemy6.x < 200:
            enemy6_v = abs(enemy6_v)

        enemy6.x += enemy6_v
    if attack > 950 and enemy6.y < 900:
        if player.y > enemy6.y:
            enemy6.y += 5
        if player.x > enemy6.x:
            enemy6.x += 1
        if player.x < enemy6.x:
            enemy6.x -= 1






def doIwin():
    if score >= 7:
        win_display = "VICTORY"
        font = pygame.font.Font('freesansbold.ttf', 30)
        win_text_img = font.render(win_display, True, (255, 255, 255), (0, 0, 0))
        win_text = win_text_img.get_rect()
        win_text.x = 225
        win_text.y = 300

        screen.blit(win_text_img, win_text)


def updategamescreen():
    global attack, bossshot, countfire
    playerdeath()
    player.x = playerX
    player.y = playerY
    laser.y -= 10
    laser2.y -= 10
    fireball.y += 10

    #fireball2.y += 12
    #fireball3.y += 12


    screen.fill((0, 0, 0))


    screen.blit(enemy1_img,enemy1)

    screen.blit(enemy2_img,enemy2)

    screen.blit(enemy3_img,enemy3)

    screen.blit(enemy4_img,enemy4)

    screen.blit(enemy5_img,enemy5)

    screen.blit(enemy6_img,enemy6)

    screen.blit(player_img,player)

    screen.blit(laser_img,laser)

    screen.blit(laser_img2,laser2)


    screen.blit(boss_img,boss)

    screen.blit(fireball_img, fireball)

    Boss()

    doIwin()

    updateScore()
    gameovertext()
    if score >= 6:
        countfire += 1
    if score < 6:

        attack += 1


    #Update the game display every frame
    pygame.display.update()

def handleKeys():
    global playerX
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:

        playerX -= player_v

    if keys[pygame.K_d]:
        #  player.left += velocity
        playerX += player_v

    if keys[pygame.K_w]:
        if laser.y >= 600 or laser.y <= 0:
            lasersound = vlc.MediaPlayer('/Users/johnlawall/Downloads/laser sound.mp3.mov')
            lasersound.play()
            shoot()
            lasersound.stop

        if laser.y < 400 and laser.y > 0:
            if laser2.y >= 600 or laser2.y <= 0:
                lasersound = vlc.MediaPlayer('/Users/johnlawall/Downloads/laser sound.mp3.mov')
                lasersound.play()

                shoot2()
                lasersound.stop

    if keys[pygame.K_s]:
        #  player.bottom += velocity
        pass







while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    handleKeys()

    handle_collisions()

    enemy_movment()




    updategamescreen()




    clock.tick(60)


pygame.quit()
#sounds from https://downloads.khinsider.com/game-soundtracks/album/galaga-arcade