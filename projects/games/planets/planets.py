import pygame
import math 

pygame.init()


#setting a window
WIDTH, HEIGHT = 800, 800 
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")


#fixing a loop that keeps my game running
def main():
    run = True

    while run: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 

    pygame.quit()

main()