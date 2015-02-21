__author__ = 'Purav'

import pygame
import math
from pygame.locals import *

g = 1000

active_projectiles = []

class projectile:
    pos_x = 0
    pos_y = 0
    vel_y = 0
    vel_x = 0
    color = (10,10,10)
    dir_x = 1
    dir_y = 1
    launch_velocity = 900
    def __init__(self,(posx,posy),angle):
        self.pos_x = posx
        self.pos_y = posy
        self.vel_x = self.launch_velocity*math.cos(angle*57.3)
        self.vel_y = self.launch_velocity*math.sin(angle*57.3)

    def drawProjectile(self,surface,time,orientation):
        self.pos_x += time*self.vel_x*orientation
        self.vel_y += g*time*self.dir_y
        self.pos_y += time*self.vel_y*self.dir_y
        pygame.draw.circle(surface,self.color,(int(self.pos_x), int(self.pos_y)),6,0)