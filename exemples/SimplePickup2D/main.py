import pygame
import math

pygame.init()

WIDTH = 600
HEIGHT = 400

window = pygame.display.set_mode((WIDTH, HEIGHT))

class itemPickup:
    
    def __init__(self, loadSprite, x=150, y=150, w=25, h=25):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.original_sprite = pygame.image.load(loadSprite)  
        self.sprite = self.original_sprite
        self.rect = self.sprite.get_rect(center = (x, y))
    
    def pickedUp(self):
        mousex, mousey = pygame.mouse.get_pos()
        
        self.x = mousex
        self.y = mousey

        self.rect = self.sprite.get_rect(center = (self.x, self.y))
    
    def draw(self, scene):
        scene.blit(self.sprite, self.rect)


item = itemPickup("box.png")

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    #if left mouse button is pressed and the cursor is in collison area
    if pygame.mouse.get_pressed()[0] and item.rect.collidepoint(pygame.mouse.get_pos()):
        item.pickedUp()


    window.fill((1,1,1))

        


    item.draw(window)    


    pygame.display.update()
