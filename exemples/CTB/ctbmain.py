import pygame
from pygame.locals import *
import random

pygame.init()


class Enemy:
    def __init__(self, speed, y, x):
        global screenWitdh
        self.speed = speed
        self.y = y
        self.x = x
        self.hitbox = pygame.surface.Surface((50, 50))
        self.hitbox.fill((0, 100, 200))
        self.rect = self.hitbox.get_rect(center = (x, y))


screenWitdh = 1280
screemHeigh = 720

screen = pygame.display.set_mode((screenWitdh, screemHeigh), RESIZABLE)
running = True





popList = []



while running:
    
    screen.fill((0, 0, 0))    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

pygame.display.update()
