from turtle import update
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('player_1.png')
        self.image = self.get_image()
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        #self.speed = 48

    def move(self, node) :
        for i in range(len(node)) :
            for j in range(len(node[0])) :
                if node[i][j]=='R' or node[i][j]=='.' :
                    self.position=[48*j, 48*i]
                    break

    def update(self) : 
        self.rect.topleft = self.position
    
    def get_image(self):
        image = pygame.Surface([48,48])
        image.blit(self.sprite_sheet, (0, 0))
        return image