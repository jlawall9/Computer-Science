import pygame



# Will load the pygame objects into your RAM
pygame.init()

# Sets a window size for the game
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Creates a clock
# Used to slow down frames per second (FPS)
clock = pygame.time.Clock()

# Sets the window title for the game (optional)
pygame.display.set_caption("Galaga")

# VARIABLES
playerX = 300
playerY = 550
player_v = 7

enemy1_v = 2
enemy2_v = 2
enemy3_v = 2
enemy4_v = 1
enemy5_v = 1
enemy6_v = 1

laserX = 0
laserY = 0
laser_v = 1

laser2X = 0
laser2Y = 0

score = 0

global player, laser, laser_img, laser2, laser_img2
laser = 0

laser_img = pygame.image.load('laser.png')
laser = laser_img.get_rect(x=-1000, y=-100)

laser2 = 0
laser_img2 = pygame.image.load('laser.png')
laser2 = laser_img2.get_rect(x=1000, y=-100)

# player ship
player_img = pygame.image.load('player ship.png')
player = player_img.get_rect(x=playerX, y=playerY)

# enemy ships
# ROW 1
enemy1_img = pygame.image.load('enemy ship.png')
enemy1 = enemy1_img.get_rect(x=100, y=50)

enemy2_img = pygame.image.load('enemy ship.png')
enemy2 = enemy2_img.get_rect(x=200, y=50)

enemy3_img = pygame.image.load('enemy ship.png')
enemy3 = enemy3_img.get_rect(x=300, y=50)

# ROW 2
enemy4_img = pygame.image.load('enemy ship.png')
enemy4 = enemy4_img.get_rect(x=100, y=125)

enemy5_img = pygame.image.load('enemy ship.png')
enemy5 = enemy5_img.get_rect(x=200, y=125)

enemy6_img = pygame.image.load('enemy ship.png')
enemy6 = enemy6_img.get_rect(x=300, y=125)


def updateScore():
    global score
    score_display = "Score: " + str(score)
    font = pygame.font.Font('freesansbold.ttf', 22)
    score_text_img = font.render(score_display, True, (225, 225, 225), (0, 0, 0))
    score_text = score_text_img.get_rect()
    score_text.x = 500
    score_text.y = 575
    # draw score
    screen.blit(score_text_img, score_text)


# helper functions
def handle_collisions():
    global score, laser, laser2, player, enemy1, enemy2, enemy3
    if laser != 0:
        if laser.colliderect(enemy1):
            enemy1.y = 1000
            laser.x = -100
            score += 1

        if laser.colliderect(enemy2):
            enemy2.y = 1000
            laser.x = -100
            score += 1

        if laser.colliderect(enemy3):
            enemy3.y = 1000
            laser.x = -100
            score += 1

        if laser.colliderect(enemy4):
            enemy4.y = 1000
            laser.x = -100
            score += 1

        if laser.colliderect(enemy5):
            enemy5.y = 1000
            laser.x = -100
            score += 1

        if laser.colliderect(enemy6):
            enemy6.y = 1000
            laser.x = -100
            score += 1

    if laser2 != 0:
        if laser2.colliderect(enemy1):
            enemy1.y = 1000
            laser2.x = -100
            score += 1

        if laser2.colliderect(enemy2):
            enemy2.y = 1000
            laser2.x = -100
            score += 1

        if laser2.colliderect(enemy3):
            enemy3.y = 1000
            laser2.x = -100
            score += 1

        if laser.colliderect(enemy4):
            enemy4.y = 1000
            laser.x = -100
            score += 1

        if laser.colliderect(enemy5):
            enemy5.y = 1000
            laser.x = -100
            score += 1

        if laser.colliderect(enemy6):
            enemy6.y = 1000
            laser.x = -100
            score += 1


def shoot():
    global laser, laserX, laserY
    laserX = playerX + player.width / 2 - 5
    laserY = playerY - player.height
    laser_img = pygame.image.load('laser.png')
    laser = laser_img.get_rect(x=laserX, y=laserY)


def shoot2():
    global laser2, laser2X, laser2Y
    laser2X = playerX + player.width / 2 - 5
    laser2Y = playerY - player.height
    laser_img2 = pygame.image.load('laser.png')
    laser2 = laser_img.get_rect(x=laser2X, y=laser2Y)


def enemy_movment():
    global enemy1_v, enemy2_v, enemy3_v, enemy4_v, enemy5_v, enemy6_v
    if enemy1.x > 300:
        enemy1_v = -enemy1_v

    if enemy1.x < 0:
        enemy1_v = abs(enemy1_v)

    enemy1.x += enemy1_v
    # enemy2
    if enemy2.x > 400:
        enemy2_v = -enemy2_v

    if enemy2.x < 100:
        enemy2_v = abs(enemy2_v)

    enemy2.x += enemy2_v
    # enemy3
    if enemy3.x > 500:
        enemy3_v = -enemy3_v

    if enemy3.x < 200:
        enemy3_v = abs(enemy3_v)

    enemy3.x += enemy3_v
    # enemy4
    if enemy4.x > 300:
        enemy4_v = -enemy4_v

    if enemy4.x < 0:
        enemy4_v = abs(enemy4_v)

    enemy4.x += enemy4_v
    # enemy5
    if enemy5.x > 400:
        enemy5_v = -enemy5_v

    if enemy5.x < 100:
        enemy5_v = abs(enemy5_v)

    enemy5.x += enemy5_v
    # enemy6
    if enemy6.x > 500:
        enemy6_v = -enemy6_v

    if enemy6.x < 200:
        enemy6_v = abs(enemy6_v)

    enemy6.x += enemy6_v


def check_death():
    global player
    if player.colliderect(enemy1):
        if player.colliderect(enemy2):
            if player.colliderect(enemy3):
                player.x = -100


def doIwin():
    if score >= 6:
        win_display = "VICTORY"
        font = pygame.font.Font('freesansbold.ttf', 30)
        win_text_img = font.render(win_display, True, (255, 255, 255), (0, 0, 0))
        win_text = win_text_img.get_rect()
        win_text.x = 225
        win_text.y = 300

        screen.blit(win_text_img, win_text)


def updategamescreen():
    player.x = playerX
    player.y = playerY
    laser.y -= 10
    laser2.y -= 10

    screen.fill((0, 0, 0))

    # rings
    screen.blit(enemy1_img, enemy1)

    screen.blit(enemy2_img, enemy2)

    screen.blit(enemy3_img, enemy3)

    screen.blit(enemy4_img, enemy4)

    screen.blit(enemy5_img, enemy5)

    screen.blit(enemy6_img, enemy6)

    screen.blit(player_img, player)

    screen.blit(laser_img, laser)

    screen.blit(laser_img2, laser2)

    doIwin()

    updateScore()

    # Update the game display every frame
    pygame.display.update()


def handleKeys():
    global playerX
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        #  player.left -= velocity
        playerX -= player_v

    if keys[pygame.K_d]:
        #  player.left += velocity
        playerX += player_v

    if keys[pygame.K_w]:
        if laser.y >= 600 or laser.y <= 0:
            shoot()
        if laser.y < 400 and laser.y > 0:
            if laser2.y >= 600 or laser2.y <= 0:
                shoot2()

    if keys[pygame.K_s]:
        #  player.bottom += velocity
        pass


run = True

# RE-RUNS for every frame of the game
while run:
    # CLEAR THE RAM when you exit the game window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # while Blasers <= 600 and laser.y >= 0:
    # keys[pygame.K_w] = False
    # else:
    # keys[pygame.K_w] = True

    # WRITE YOUR GAME CODE

    handleKeys()

    handle_collisions()

    enemy_movment()

    updategamescreen()

    check_death()

    clock.tick(60)

pygame.quit()
# sounds from https://downloads.khinsider.com/game-soundtracks/album/galaga-arcade