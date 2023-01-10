import pygame
from pygame.constants import DROPFILE
from rectObj import rect
from random import randint

def displayScore():
    global curentTime
    curentTime=pygame.time.get_ticks()-starTime
    scoreSurface=textFont.render(f"Score: {curentTime//1000}",False,"#2D2424")
    scoreRect=scoreSurface.get_rect(center=(400,80))
    screen.blit(scoreSurface,scoreRect)

def displayJump():
    global doubleJump
    doubSurface=textFont1.render(f" Double jump: {doubleJump} ", False,"#BDC7C9")
    doubRect=doubSurface.get_rect(center=(100,30))
    shieldSurface=textFont1.render(f" Shield: {shield} ", False,"#BDC7C9")
    shieldRect=doubSurface.get_rect(center=(100,60))
    screen.blit(doubSurface,doubRect)
    screen.blit(shieldSurface,shieldRect)
def userAnimation():
    global userIndex
    if user.rect.bottom<300: 
        return userJump.surf
    userIndex+=0.1
    if userIndex > len(usersWalk): userIndex=0
    return usersWalk[int(userIndex)].surf

pygame.init()
pygame.display.set_caption('YK')
screen = pygame.display.set_mode((800,400))
clock= pygame.time.Clock()
textFont=pygame.font.Font('font/Pixeltype.ttf',40)
textFont1=pygame.font.Font('font/Pixeltype.ttf',30)
isProcess=True

#testSurface=pygame.Surface((200,100))
#testSurface.fill("#FFB319")
jumpCheck=0
jumpCount=0

gameActive=0

starTime=0
Count=0
curentTime=0
doubleJump=0
shield=0
isDouble = -1
velocity = 6
pre=400
distace=400
isShield=0

skySurface=pygame.image.load('graphics/sky.png').convert()
groundSurface=pygame.image.load('graphics/ground.png').convert()
textSurface=textFont.render(' Welcome, newbie ',False,"#B85C38")
textRect=textSurface.get_rect(center=(400,30))
introSurface=textFont.render(' Runner Game ', False,"#E0C097")
introRect=introSurface.get_rect(center=(400,80))
howtoSurface=textFont.render(' F5: Start     SPACE: Play ', False,"#E0C097")
howtoRect=howtoSurface.get_rect(center=(400,350))

mainSound=[pygame.mixer.Sound('audio/Yk.mp3'),pygame.mixer.Sound('audio/Yk2.mp3')]
#mainSound[randint(0,1)].play()

ava=rect('graphics/Player/player_stand.png',400,290,2,"avatar")

user=rect('graphics/Player/player_stand.png',80,300,1,"player")
userWalk1=rect('graphics/Player/player_walk_1.png',80,300,1,"")
userWalk2=rect('graphics/Player/player_walk_2.png',80,300,1,"")
userJump=rect('graphics/Player/jump.png',80,300,1,"jump")
usersWalk=[userWalk1,userWalk2]
userIndex=0

snail1=rect('graphics/snail/snail1.png',800,300,1,"obsta")
snail2=rect('graphics/snail/snail2.png',800,300,1,"obsta")
snails=[snail1,snail2]
snailIndex=0
snail=snails[snailIndex]
snailTimer=pygame.USEREVENT + 2
pygame.time.set_timer(snailTimer,500)


bird1=rect('graphics/Fly/Fly1.png',1500,250,1,"obsta")
bird2=rect('graphics/Fly/Fly2.png',1500,250,1,"obsta")
birds=[bird1,bird2]
birdIndex=0
bird=birds[birdIndex]
birdTimer=pygame.USEREVENT + 3
pygame.time.set_timer(birdTimer,300)



challenge_list=["x2 speed", "x2 size","🠕 speed","- speed","+ shield","+ move"]
timer=pygame.USEREVENT + 1
pygame.time.set_timer(timer,1000)



while isProcess:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            isProcess=False
        if gameActive==1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if user.collison((80,290)):
                        jumpCount=-23
                    elif doubleJump>0:
                        jumpCount=-23
                        doubleJump-=1
            if event.type == timer:
                Count+=1
                if Count%10==0: velocity-=1
                elif Count%5==0: doubleJump+=1
                elif Count%15==0: distace+=100
                snail=rect('graphics/snail/snail1.png',pre+400,300,1,"snail")
                if randint(0,2): bird=rect('graphics/Fly/Fly1.png',pre+2*distace,250,1,"bird")
                pre+=400
                
        elif event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_F5: 
                gameActive=1
                starTime=pygame.time.get_ticks()
                doubleJump=0
                Count=0
        if gameActive==1:
            if event.type == snailTimer:
                if snailIndex==0: snailIndex=1
                else: snailIndex=0
                rect.setAnimation(snails[snailIndex],1,0)
            if event.type == birdTimer:
                if birdIndex==0: birdIndex=1
                else: birdIndex=0
                rect.setAnimation(birds[birdIndex],0,1)
    #enemies
    if gameActive==1:
        jumpCount+=1
        user.jump(jumpCount)
    
        screen.blit(skySurface,(0,0))
        screen.blit(groundSurface,(0,300))
        pygame.draw.rect(screen,"#2D2424",textRect)
        pygame.draw.rect(screen,"#2D2424",textRect,6)
        doubSurface=textFont.render(f" Double jump: {doubleJump} ", False,"#E0C097")
        screen.blit(textSurface,textRect) 
        
        if not(rect.listMove(screen,velocity)):
            gameActive=0

        user.surf=userAnimation()
        user.show(screen)
        displayScore()
        displayJump()
    else:
        screen.fill("#5C3D2E")
        screen.blit(introSurface,introRect)
        if curentTime>0 :
            howtoSurface=textFont.render(f" SCORE: {curentTime//1000} ", False,"#E0C097") 
            howtoRect=howtoSurface.get_rect(center=(400,350))
        screen.blit(howtoSurface,howtoRect)
        ava.show(screen)
        velocity=6
        pre=400
    pygame.display.update()
    clock.tick(60)

pygame.quit()