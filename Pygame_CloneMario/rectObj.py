import pygame
class rect:
    enermies=[]
    checkPos=0
    def __init__(self,address,pos_x,pos_y,scale,character):
        self.surf=pygame.image.load(address).convert_alpha()
        self.surf=pygame.transform.rotozoom(self.surf,0,scale)
        self.rect=self.surf.get_rect(midbottom=(pos_x,pos_y))
        self.character=character
        if character=="snail" or character=="bird" :rect.enermies.append(self)
        if character=="player": 
            rect.checkPos=self         
    def show(self,surface):
        surface.blit(self.surf,self.rect)
    def collison(self, obj):
        if type(obj)==rect:
            return self.rect.colliderect(obj.rect)
        elif type(obj)==tuple:
            return self.rect.collidepoint(obj)
    def jump(self,jumpCount):
        self.rect.bottom+=jumpCount
        if self.rect.bottom>=300:
            self.rect.bottom=300
    
    @classmethod
    def listMove(cls,surface,velocity):
        cls.enermies=[x for x in cls.enermies if x.rect.left>-100]
        for enermy in cls.enermies:
            enermy.rect.left-=velocity
            enermy.show(surface)
            if enermy.collison(cls.checkPos):
                rect.listReset()
                return 0
        return 1
    
    @classmethod
    def listReset(cls):
        cls.enermies=[]

    @classmethod
    def setAnimation(cls,objTemp,isSnail,isBird):
        if isSnail:
            for enermy in cls.enermies:
                if enermy.character=="snail":
                    enermy.surf=objTemp.surf
        if isBird:
            for enermy in cls.enermies:
                if enermy.character=="bird":
                    enermy.surf=objTemp.surf
        
        
        