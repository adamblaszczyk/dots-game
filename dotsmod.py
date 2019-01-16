#
# ---------------------------------------------
# Dots game
# [ module ]
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

import pygame


WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


class Player(object):

    def __init__(self, x, y, r, color, xmax, ymax):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.xmax = xmax
        self.ymax = ymax
        
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= 2
        if keys[pygame.K_DOWN]:
            self.y += 2
        if keys[pygame.K_LEFT]:
            self.x -= 2
        if keys[pygame.K_RIGHT]:
            self.x += 2
            
        if self.x >= self.xmax:
            self.x = self.xmax
        if self.x <= 0:
            self.x = 0
        if self.y >= self.ymax:
           self.y = self.ymax
        if self.y <=0:
           self.y = 0
            
    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.r)


class Enemy(object):

    def __init__(self, x, y, r, color, dx, dy):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dx = dx
        self.dy = dy

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.r)

