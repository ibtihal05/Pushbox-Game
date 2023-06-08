from turtle import update
import pygame

class Box(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('box_1.png')
        self.image = self.get_image()
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]

    def move(box, node) :
        k=0
        for i in range(len(node)) :
            for j in range(len(node[0])) :
                if node[i][j]=='B'or node[i][j]=='*' :
                    box[k].position=[48*j, 48*i]
                    k=k+1
                if (k==len(box)) : 
                    break

    def update(self) : 
        self.rect.topleft = self.position
    
    def get_image(self):
        image = pygame.Surface([48,48])
        image.blit(self.sprite_sheet, (0, 0))
        return image