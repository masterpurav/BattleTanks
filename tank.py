__author__ = 'Purav'

import pygame
import math
from pygame.locals import *
from projectile import projectile, active_projectiles

class tank:
    # Tank attributes initialization
    orientation = 1         # 1 for left, -1 for right
    tank_height = 61        # Tank dimensions
    tank_width = 167
    gun_length = 70         # Tank gun dimensions
    gun_dir = 0             # Direction of gun movement - 1 for anti-clockwise, -1 for clockwise, 0 for stationary
    dir = 0                 # Direction of tank movement - 1 for right, -1 for left
    speed = 250             # Tank movement speed
    tank_pos_x = 0          # Co-ordinates of tank
    tank_pos_y = 0
    angle = 0               # Gun angle
    tank_color = (01,0,0)   # Tank color
    gun_velocity = 0.001   # Angular velocity of gun rotation
    gun_x = 0
    gun_y = 0

    # Constructor
    def __init__(self,(posx,posy),color,orientation):
        self.tank_pos_x = posx
        self.tank_pos_y = posy
        self.tank_color = color
        self.orientation = orientation

    # Move left
    def moveLeft(self):
        self.dir = -1

    # Move Right
    def moveRight(self):
        self.dir = 1

    # Gun up
    def gunUp(self):
        self.gun_dir = 1

    # Gun down
    def gunDown(self):
        self.gun_dir = -1

    # Draws the tank on the specified surface with its state at specified time
    def drawTank(self,surface, time):
        if self.orientation == 1:
            self.image = pygame.image.load("images/tank_left.gif")
        else:
            self.image = pygame.image.load("images/tank_right.gif")
        self.gun_x = self.tank_pos_x+self.orientation*self.gun_length*math.cos(self.angle*57.3)
        self.gun_y = self.tank_pos_y-self.tank_height/2-self.gun_length*math.sin(self.angle*57.3)
        pygame.draw.line(surface,(211,54,0),(self.tank_pos_x,self.tank_pos_y-self.tank_height/2),(self.gun_x,self.gun_y),5)
        #pygame.draw.rect(surface,self.tank_color,Rect((self.tank_pos_x-self.tank_width/2,self.tank_pos_y-self.tank_height),(self.tank_width,self.tank_height)))
        surface.blit(self.image,(self.tank_pos_x-self.tank_width/2,self.tank_pos_y-self.tank_height))
        self.tank_pos_x += time*self.speed*self.dir
        self.angle += self.gun_dir * self.gun_velocity
        for x in active_projectiles:
            x.drawProjectile(surface,time,self.orientation)

    def fire(self):
        p = projectile((self.gun_x,self.gun_y),self.angle)
        active_projectiles.append(p)