import pygame
from pygame.constants import DROPFILE
from rect import rect

def displayScore():
    global curentTime
    curentTime=pygame.time.get_ticks()-starTime
    scoreSurface=textFont.render(f"Score: {curentTime//500}",False,"#2D2424")
    scoreRect=scoreSurface.get_rect(center=(400,80))
    screen.blit(scoreSurface,scoreRect)
    


pygame.init()
pygame.display.set_caption('YK')
screen = pygame.display.set_mode((800,400))
clock= pygame.time.Clock()
textFont=pygame.font.Font('font/Pixeltype.ttf',40)
isProcess=True

#testSurface=pygame.Surface((200,100))
#testSurface.fill("#FFB319")

skySurface=pygame.image.load('graphics/sky.png').convert()
groundSurface=pygame.image.load('graphics/ground.png').convert()
textSurface=textFont.render(' Welcome, newbie ',False,"#B85C38")
textRect=textSurface.get_rect(center=(400,30))
introSurface=textFont.render(' Runner Game ', False,"#E0C097")
introRect=introSurface.get_rect(center=(400,80))
howtoSurface=textFont.render(' F5: Start     SPACE: Play ', False,"#E0C097")
howtoRect=howtoSurface.get_rect(center=(400,350))

ava=rect('graphics/Player/player_stand.png',400,290,2)
snail=rect('graphics/snail/snail1.png',800,300,1)
users=rect('graphics/Player/player_stand.png',80,300,1)
birds=[rect('graphics/Fly/Fly1.png',1300,250,1),rect('graphics/Fly/Fly2.png',1300,250,1)]
bird=birds[0]

jumpCheck=0
jumpCount=0

gameActive=0
starTime=0
curentTime=0
doubleJump=0
doubleJumpCount=0
isDouble = -1
velocity = 6
timer=pygame.USEREVENT + 1
pygame.time.set_timer(timer,500)

while isProcess:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            isProcess=False
        if gameActive==1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if users.collison((80,290)):
                        jumpCount=-23                        
                        print("jump")
                    elif doubleJump>0:
                        jumpCount=-23
                        doubleJump-=1
            if event.type == timer:
                doubleJumpCount+=1
                if doubleJumpCount%50==0: velocity-=1
                elif doubleJumpCount%10==0: doubleJump+=1
                print(doubleJumpCount," ",doubleJump)
                
        elif event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_F5: 
                gameActive=1
                rect.reset()
                starTime=pygame.time.get_ticks()
                doubleJump=0
                doubleJumpCount=0
            
    #enemies
    if gameActive==1:
        if snail.rect.left >=-100: snail.rect.x-=velocity
        else: snail.rect.x=800
        if bird.rect.left >=-100: bird.rect.x-=velocity
        else: bird.rect.x=1300
        if bird.rect.left %100<50: 
            birds[1].rect.left=bird.rect.left
            bird=birds[1] 
        else: 
            birds[0].rect.left=bird.rect.left
            bird=birds[0]
        #player
        jumpCount+=1
        users.jump(jumpCount)
        
        #collison
        if users.collison(snail): 
            print("Snail")
            gameActive=0
        elif users.collison(bird): 
            print("Bird")
            gameActive=0
    
        screen.blit(skySurface,(0,0))
        screen.blit(groundSurface,(0,300))
        pygame.draw.rect(screen,"#2D2424",textRect)
        pygame.draw.rect(screen,"#2D2424",textRect,6)
        screen.blit(textSurface,textRect)
        
        snail.show(screen)
        bird.show(screen)
        users.show(screen)
        displayScore()
    else:
        screen.fill("#5C3D2E")
        screen.blit(introSurface,introRect)
        if curentTime>0 :
            howtoSurface=textFont.render(f" SCORE: {curentTime//500} ", False,"#E0C097") 
            howtoRect=howtoSurface.get_rect(center=(400,350))
        screen.blit(howtoSurface,howtoRect)
        ava.show(screen)
        velocity=6
    pygame.display.update()
    clock.tick(60)

pygame.quit()