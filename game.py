import pygame
import os
import time
import random

#initialze the Fonts in pygame
pygame.font.init()

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
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)


    clock = pygame.time.Clock()


    # Update the window (inside method to have access to the variables)
    def redraw_window():
        #Pygame Surface, BLIT drwas it to the window to the given location -> 0,0 is top left 
        WIN.blit(BG, (0,0))

        # draw Text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,0,0))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))   

        # Blit the Level and Lives to the Surface
        WIN.blit(lives_label, (10,10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))


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