import pygame
from pygame.locals import *
pygame.init()
import random

screenWitdh = 1280
screemHeigh = 720

screen = pygame.display.set_mode((screenWitdh, screemHeigh), RESIZABLE)
running = True

enemy_list = []

class Player:
    
    def __init__(self, x=600, y=580, w=100, h=25, speed=0.2):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        self.hitbox = pygame.surface.Surface((w, h))
        self.hitbox.fill((255, 100, 200))
        self.rect = self.hitbox.get_rect(center = (x, y))
        #self.original_sprite = pygame.image.load(loadSprite)  
        #self.sprite = self.original_sprite
        #self.rect = self.sprite.get_rect(center = (x, y))
        self.move_right = pygame.K_RIGHT
        self.move_left = pygame.K_LEFT

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[self.move_right]:
            self.x += self.speed
        if keys[self.move_left]:
            self.x -= self.speed
        self.rect = self.hitbox.get_rect(center = (self.x, self.y))

    
    def draw(self):
        screen.blit(self.hitbox, self.rect)


class Enemy:
    def __init__(self, speed, y, x):
        #self.recycle()   # set the position & size initially
        global screenWitdh
        self.speed = speed
        self.y = y
        self.x = x
        self.hitbox = pygame.surface.Surface((50, 50))
        self.hitbox.fill((0, 100, 200))
        #self.y = (random.randrange(1, 100) / * screenWitdh)
        nr = random.randrange(200, 1050)
        self.rect = self.hitbox.get_rect(center = (x, y))#pygame.Rect( nr, self.y, 50, 50 )

    #def recycle( self ):
        # start or re-start an enemy position
        #self.size = random.randint(10,40)
        #self.xval = random.randint(0,700)
        #self.yval = -self.size              # off the screen-top
        #self.rect = pygame.Rect( self.xval, self.yval, self.size, self.size )

    def draw( self ):
        #nr = random.randrange(1, 700)
        pygame.draw.ellipse( screen, (255,255,0), self.rect)

    def create_enemy(self):
        global enemy_list
        nr = random.randrange(200, 1050)
        new_enemy = Enemy(self.speed, self.y, nr)               # create a new Enemy
        enemy_list.append( new_enemy )    # add it to the list
    
    def movedown(self):
        self.y += 0.2
        self.rect = self.hitbox.get_rect(center = (self.x, self.y))
    




player = Player()
enemy = Enemy(5, 10, 0)

while running:
    
    screen.fill((0, 0, 0))    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                enemy.create_enemy()
                


    for enemys in enemy_list:
        enemys.draw()
        enemys.movedown()

        

    player.move()
    player.draw()


    pygame.display.update()
