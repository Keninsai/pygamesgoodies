import pygame
import sys

pygame.init()

WIDTH = 600
HEIGHT = 400

main = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

while True:
    
    #Pygame event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Fill window with colour(background)
    main.fill((1,1,1)) 


    pygame.display.update()
