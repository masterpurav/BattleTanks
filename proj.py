__author__ = 'Purav'

import pygame
import math
import time
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
    napalmTime = time.time()
    image = pygame.image.load("images/fire_2.png")
    def __init__(self,(posx,posy),angle,orientation,type):
        self.type = type
        self.pos_x = posx
        self.pos_y = posy
        self.vel_x = self.launch_velocity*math.cos(angle*57.3)
        self.vel_y = self.launch_velocity*math.sin(angle*57.3)
        self.orientation = orientation
        active_projectiles.append(self)

    def drawProjectile(self,surface,time,type):
        self.pos_x += time*self.vel_x*self.orientation
        self.vel_y += g*time*self.dir_y
        self.pos_y -= time*self.vel_y*self.dir_y
        if(self.pos_y > scr_height):
            active_projectiles.remove(self)
        if type == 1:
            pygame.draw.circle(surface,self.color,(int(self.pos_x), int(self.pos_y)),6,0)
        else:
            surface.blit(self.image,(int(self.pos_x), int(self.pos_y)))

    def napalmStrike(self,surface,time):

        for x in active_projectiles:
            if x.type == 2:
                if x.pos_y > scr_height:
                    surface.blit(self.napalm,(int(x.pos_x)-napalm_width/2, scr_height))
                    if(int(x.pos_x) > scr_width/2):
                        napalm_region[1] = int(x.pos_x)
                    else:
                        napalm_region[0] = int(x.pos_x)
                    active_projectiles.remove(x)

def drawNapalm(surface):
    pygame.draw.line(surface,(32,43,232),(napalm_region[0],scr_width-10),(napalm_region[0]+napalm_width,scr_width-10),10)
    pygame.draw.line(surface,(32,43,232),(napalm_region[1],scr_width-10),(napalm_region[1]+napalm_width,scr_width-10),10)



