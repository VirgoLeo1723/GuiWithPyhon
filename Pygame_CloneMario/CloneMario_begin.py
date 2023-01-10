from typing import get_origin
import pygame
from pygame.mixer import fadeout
import snailObject
pygame.init()
pygame.display.set_caption('YK')
screen = pygame.display.set_mode((800,400))
clock= pygame.time.Clock()
textFont=pygame.font.Font('font/Pixeltype.ttf',50)
isProcess=True

#testSurface=pygame.Surface((200,100))
#testSurface.fill("#FFB319")
skySurface=pygame.image.load('graphics/sky.png')
groundSurface=pygame.image.load('graphics/ground.png')
textSurface=textFont.render('Welcome, newbie',False,"#FFB319")

while isProcess:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            isProcess=False
    
    #screen.blit(testSurface,(200,100))
    screen.blit(skySurface,(0,0))
    screen.blit(groundSurface,(0,300))
    screen.blit(textSurface,(290,100))
    pygame.display.update()
    clock.tick(60)

pygame.quit()