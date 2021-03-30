import pygame
import random
import math
pygame.mixer.init()
#initialize the pygame
pygame.init()
#create the screen
screen = pygame.display.set_mode((800, 600))
#background 
background = pygame.image.load("background.png")
#bgm
pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)
#title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
#player
playerImage = pygame.image.load('player.png')
playerX = 370
playerY = 450
playerX_Change = 0
#MULTI ENEMIES
enemyImage = []
enemyX = []
enemyY = []
enemyX_Change = []
enemyY_Change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    #enemy
    enemyImage.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(50,150))
    enemyX_Change.append(0.2)
    enemyY_Change.append(30)
#bullet
bulletImage = pygame.image.load('1bullet.png')
bulletX = 0
bulletY = 480
bulletX_Change = 0
bulletY_Change = 2
#ready - you cant see the bullet on screen
bullet_state = "ready"
#respawn of enemy
# def enemyrespawn():
#     enemyX = random.randint(0,735)
#     enemyY = random.randint(50,150)
#for the appearing of player and enemy
def player():
    screen.blit(playerImage, (playerX, playerY))
def enemy():
    screen.blit(enemyImage, (enemyX, enemyY))
def bullet():
    screen.blit(enemyImage, (enemyX, enemyY))
def player(x,y):
    screen.blit(playerImage, (x,y))
def enemy(x,y,i):
    screen.blit(enemyImage[i], (x,y))
def bullet(x,y):
    screen.blit(bulletImage, (x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImage, (x,y))
#collision detection
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2) + (math.pow(enemyY-bulletY,2)))
    if distance<27:
        return True
    else:
        return False
#score
score=0
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
testX = 10
testY = 10
def showScore(x,y):
    score = font.render("Score :" + str(score_value),True, (255,255,0))
    screen.blit(score,(x,y))
#gameover Font
game_over_font = pygame.font.Font("stocky.ttf", 70)
def game_over_text():
    game_over = game_over_font.render("GAME OVER",True, (255,255,0))
    screen.blit(game_over,(200,250))
#game loop
running = True
while running:
    #RGB
    screen.fill((0,0,0))
    #background image
    screen.blit(background, (0,0))
    # FOR CLOSING    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #if any key stroke is being pressed
        #keydown responds to all the key strokes
        if event.type == pygame.KEYDOWN:
            #left
            if event.key == pygame.K_LEFT:
                #print("left is pressed")
                playerX_Change = -0.3
            #right
            if event.key == pygame.K_RIGHT:
                #print("Right is pressed")
                playerX_Change = 0.3
            #if the space key is pressed then bullet is fired only the
            #when its ready state. and x state should be same and shouldnot change when 
            #untill the bullet passes the screen end
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = pygame.mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)
        #if key is released stop
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                #print("keystroke has been released")
                playerX_Change = 0 #to stop when we release
    #making boundaries of spaceship
    playerX += playerX_Change  
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    #enemy
    for i in range(num_of_enemies):
        #gameover
        if enemyY[i] >400:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        #enemy movement
        enemyX[i] += enemyX_Change[i]
        if enemyX[i] <= 0:
            enemyX_Change[i] = 0.3
            enemyY[i] += enemyY_Change[i]
        elif enemyX[i] >= 736:
            enemyX_Change[i] = -0.3
            enemyY[i] += enemyY_Change[i]
        #Collision
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            explosion_sound = pygame.mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 450
            bullet_state = "ready"
            score_value += 1
            #print(score)
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)
        enemy(enemyX[i], enemyY[i],i)
    #bullet travel
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_Change
    if bulletY<=0:
        bulletY = 450
        bullet_state = "ready"
    #playerImage
    #player()
    player(playerX, playerY)
    #enemyImage
    #bulletṇṇ
    #bullet(bulletX, bulletY)
    #showScore
    showScore(testX,testY)
    #updating display
    pygame.display.update()

