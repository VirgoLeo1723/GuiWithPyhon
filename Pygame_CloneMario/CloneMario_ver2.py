import pygame
from random import choices, randint, uniform
from pygame import sprite

from pygame.constants import K_SPACE, K_m

class User(pygame.sprite.Sprite):
    def __init__(self,x,press):
        super().__init__()
        self.pos=x
        self.input=press
        self.size=1
        self.shield=0
        self.jumpSound=pygame.mixer.Sound('audio/jump.mp3')
        self.image = pygame.image.load("graphics/Player/player_stand.png")
        self.rect = self.image.get_rect(midbottom=(self.pos,300))
        
        userWalk1=pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        userWalk2=pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
        self.Jump=pygame.image.load('graphics/Player/jump.png').convert_alpha()
        self.Walks=[userWalk1,userWalk2]
        self.Index=0
        self.gravity = 0
    def player_input(self):
        keys=pygame.key.get_pressed()
        if keys[self.input]:
            if self.rect.bottom >= 300:
                self.gravity=-21
    def apply_gravity(self):
        self.gravity+=1
        self.rect.y+=self.gravity
        if self.rect.bottom>=300:
            self.rect.bottom=300
    def apply_animation(self):
        if self.rect.bottom < 300:
            self.image=self.Jump
        else:
            self.Index+=0.1
            if self.Index>len(self.Walks): self.Index=0
            self.image=self.Walks[int(self.Index)]
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.apply_animation()

class Enermy(pygame.sprite.Sprite):
    speed=6
    def __init__(self,type):
        super().__init__()
        if type==['bird']:
            bird1=pygame.image.load('graphics/fly/Fly1.png').convert_alpha()
            bird2=pygame.image.load('graphics/fly/Fly2.png').convert_alpha()
            self.frame=[bird1,bird2]
            y_pos=250
        else:
            snail1=pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail2=pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frame=[snail1,snail2]
            y_pos=300
        self.speed=Enermy.speed
        self.Index=0
        self.image=self.frame[self.Index]
        self.rect=self.image.get_rect(midbottom=(randint(900,1100),y_pos))
    def apply_animation(self):
        self.Index+=0.1
        if self.Index>len(self.frame): self.Index=0
        self.image=self.frame[int(self.Index)]
    def destroy(self):
        if self.rect.  x<-100: self.kill()
    def update(self):
        self.apply_animation()
        self.rect.x-=self.speed
        self.destroy()
    @staticmethod
    def changeSpeed(temp):
        if temp>0: Enermy.speed=int(Enermy.speed+temp)
        else: Enermy.speed=int(Enermy.speed+temp)
    @staticmethod
    def resetSpeed():
        Enermy.speed=6


def collisionSprite(playerTemp):
    if pygame.sprite.spritecollide(playerTemp.sprite,enermy_group,False):
        return False
    else: return True

def resetGroup():
    enermy_group.empty()

def displayScore():
    global curentTime
    curentTime=pygame.time.get_ticks()-startTime
    scoreSurface=textFont.render(f"Score: {curentTime//1000}",False,"#2D2424")
    scoreRect=scoreSurface.get_rect(center=(400,80))
    screen.blit(scoreSurface,scoreRect)

def contiueCondition():
    global userDead
    
    isActive1=collisionSprite(player1)
    isActive2=collisionSprite(player2)
    if isActive1:
        if userDead!=1:
            player1.draw(screen)
            player1.update()  
    else: 
        if userDead==2: return 0
        else: userDead=1
            
    if isActive2:
        if userDead!=2:
            player2.draw(screen)
            player2.update()       
    else: 
        if userDead==1: return 0
        else: userDead=2
    
    return 1

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
mainSound=[pygame.mixer.Sound('audio/Yk.mp3'),pygame.mixer.Sound('audio/Yk2.mp3')]
mainSound[randint(0,1)].play()
avaObject=pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
avaObject=pygame.transform.rotozoom(avaObject,0,2)
avaRect=avaObject.get_rect(center=(400,200))

player1=pygame.sprite.GroupSingle()
player1.add(User(80,K_SPACE))
player2=pygame.sprite.GroupSingle()
player2.add(User(200,K_m))
enermy_group=pygame.sprite.Group()


isActive1=0
isActive2=0
isActive=0
userDead=0
curentTime=0
velocity=6
startTime=0
curentTime=0
countEvent=0
doubJump=0
userTimer=pygame.USEREVENT + 1
pygame.time.set_timer(userTimer,1000)



while isProcess:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            isProcess=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F5:
                isActive=1
                startTime=pygame.time.get_ticks()
        if event.type == userTimer and isActive==1:
            enermy_group.add(Enermy(choices(["bird","bird","snail","snail"])))
            countEvent+=1
            if countEvent%6 == 0: Enermy.changeSpeed(1)
            if countEvent%7 == 0: Enermy.changeSpeed(2)
            if countEvent%8 == 0: Enermy.changeSpeed(-4)

    if isActive==1:
        
        screen.blit(skySurface,(0,0))
        screen.blit(groundSurface,(0,300))
        pygame.draw.rect(screen,"#2D2424",textRect)
        pygame.draw.rect(screen,"#2D2424",textRect,6)
        screen.blit(textSurface,textRect)
        

        isActive=contiueCondition()
        enermy_group.draw(screen)
        enermy_group.update()
        displayScore()  

    elif isActive==0:
        screen.fill("#5C3D2E")
        screen.blit(introSurface,introRect)
        if curentTime>0 :
            howtoSurface=textFont.render(f" SCORE: {curentTime//1000} ", False,"#E0C097") 
            howtoRect=howtoSurface.get_rect(center=(400,350))
        screen.blit(howtoSurface,howtoRect)
        screen.blit(avaObject,avaRect)
        userDead=0
        resetGroup()
        Enermy.resetSpeed()
        countEvent=0
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()