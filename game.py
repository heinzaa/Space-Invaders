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

# Abstract Klasse, because we have friendly ships and enemy ships
class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
    def draw(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y, 50, 50))


# Game Settings
def main(): 
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)

    # how manyy steps by on time clicking the key
    plyaer_vel = 5

    ship = Ship(300, 650)

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
        
        # Draw the Ship
        ship.draw(WIN)

        pygame.display.update()



    # Game Loop
    while run:
        clock.tick(FPS)
        redraw_window()

        # every 60 per second pygame give us the event the user does
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        # Set thje movement oft the rectangle
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: # left 
            ship.x -= plyaer_vel
        if keys[pygame.K_d]: # right
            ship.x += plyaer_vel
        if keys[pygame.K_w]: # up 
            ship.y -= plyaer_vel
        if keys[pygame.K_s]: #down
            ship.y += plyaer_vel


main()