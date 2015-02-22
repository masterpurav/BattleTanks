__author__ = 'Purav'

import pygame
import math
from pygame.locals import *
from game_constants import *

active_projectiles = []

class projectile:
    pos_x = 0.
    pos_y = 0.
    vel_y = 0.
    vel_x = 0.
    color = (10,10,10)
    dir_x = 1
    dir_y = 1
    launch_velocity = 1000
    orientation = 1
    def __init__(self,(posx,posy),angle,orientation):
        self.pos_x = posx
        self.pos_y = posy
        self.vel_x = self.launch_velocity*math.cos(angle*57.3)
        self.vel_y = self.launch_velocity*math.sin(angle*57.3)
        self.orientation = orientation

    def drawProjectile(self,surface,time):
        self.pos_x += time*self.vel_x*self.orientation
        self.vel_y += g*time*self.dir_y
        self.pos_y -= time*self.vel_y*self.dir_y
        if(self.pos_y > scr_height):
            active_projectiles.remove(self)
        pygame.draw.circle(surface,self.color,(int(self.pos_x), int(self.pos_y)),6,0)


