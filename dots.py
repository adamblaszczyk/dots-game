#
# ---------------------------------------------
# Dots game
# [ main program ]
# ---------------------------------------------
# Author: Adam Blaszczyk
#         http://wyciekpamieci.blogspot.com
# Date:   2019-01-16
# ---------------------------------------------
#
# Requirements:
#         - Python 3.x
#         - Pygame library (pip install pygame)
#

from dotsmod import *
from random import randint

# ====== IMPORT AND INITIALISE PYGAME LIBRARY =================================

import pygame

pygame.init()

# ====== DEFINE AND OPEN MAIN WINDOW ==========================================

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dots")

# ====== INITIALISE VARIOUS VARIABLES AND OBJECTS USED IN THE GAME ============

FPS = 200

clock = pygame.time.Clock()
font1 = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 30)

player = Player(randint(0, WIDTH), randint(0, HEIGHT), 8, GREEN, WIDTH, HEIGHT)
enemy = []
enemy.append(Enemy(randint(0, WIDTH), randint(0, HEIGHT), 8, RED, randint(-1, 1), randint(-1, 1)))
points = 0

game_over = False
run = True
# ====== MAIN PYGAME WHILE LOOP ===============================================

while run:

    # --- Capture Events --------------------------------------------------
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False            
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
    
    # --- Game Logic ------------------------------------------------------
    
    if not game_over:
        player.move()
    
        for i in range(len(enemy)):
            enemy[i].x = enemy[i].x + enemy[i].dx
            if enemy[i].x >= WIDTH:
                enemy[i].dx = -1
            if enemy[i].x <= 0:
                enemy[i].dx = 1      
            enemy[i].y = enemy[i].y + enemy[i].dy
            if enemy[i].y >= HEIGHT:
                enemy[i].dy = -1
            if enemy[i].y <= 0:
                enemy[i].dy = 1
   
        for i in range(len(enemy)):
            if player.x in range(enemy[i].x - enemy[i].r, enemy[i].x + enemy[i].r) \
            and player.y in range(enemy[i].y - enemy[i].r, enemy[i].y + enemy[i].r):
                player.color = WHITE
                enemy[i].color = WHITE
                game_over = True

        points = int(pygame.time.get_ticks() / 1000)
        
        if points > 0 and points % int(points**0.5) == 0 and pygame.time.get_ticks() <= points*1000 + 1000/FPS:
            enemy.append(Enemy(randint(0, WIDTH), randint(0, HEIGHT), 8, RED, randint(-1, 1), randint(-1, 1)))

    # --- Drawing ---------------------------------------------------------
    
    screen.fill((0, 0, 50))
    player.draw(screen)
    for i in range(len(enemy)):
        enemy[i].draw(screen)
    txt_data = "POINTS = " + str(points) 
    text = font2.render(txt_data, True, YELLOW)
    screen.blit(text, [10, 10])
    txt_data = "ENEMIES = " + str(len(enemy)) 
    text = font2.render(txt_data, True, BLUE)
    screen.blit(text, [10, 40])
    txt_data = str(int(clock.get_fps())) + " FPS" 
    text = font2.render(txt_data, True, YELLOW)
    screen.blit(text, [WIDTH - 100, 10])
    
    if game_over:
        text = font1.render("Game Over", True, BLUE)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])

    # ---  Refresh screen -------------------------------------------------
    
    # update the contents of the entire display
    pygame.display.flip()
    
    # frames per second
    clock.tick(FPS)

# ====== END ==================================================================

pygame.quit()
