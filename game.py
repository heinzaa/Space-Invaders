import pygame
import os
import time
import random

#Set our Display
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter Game")

# Load Images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))

# Main Layer ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Load Laser
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# BG 
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))


# Game Settings
def main(): 
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    def redraw_window():
        #Pygame Surface, BLIT drwas it to the window to the given location -> 0,0 is top left 
        WIN.blit(BG, (0,0))
        pygame.display.update()



    # Game Loop
    while run:
        clock.tick(FPS)
        redraw_window()

        # every 60 per second pygame give us the event the user does
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

main()