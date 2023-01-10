import pygame
class rect:
    enermies=[]
    def __init__(self,address,pos_x,pos_y,scale):
        self.x=pos_x
        self.y=pos_y
        self.surf=pygame.image.load(address).convert_alpha()
        self.surf=pygame.transform.rotozoom(self.surf,0,scale)
        self.rect=self.surf.get_rect(midbottom=(pos_x,pos_y))
        self.enermies.append(self)
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
    def reset(cls):
        for enermy in cls.enermies:
            enermy.rect=enermy.surf.get_rect(midbottom=(enermy.x,enermy.y))