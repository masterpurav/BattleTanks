__author__ = 'Purav'

import pygame
import ast
import math
from game_constants import *
from proj import projectile, active_projectiles
from wall import wall
import time

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
    lastCast1 = time.time()
    lastCast2 = time.time()
    gotBurnt = time.time()
    health = 100
    flag = ""

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
    def drawTank(self,surface,time):
        if self.orientation == 1:
            self.image = pygame.image.load("images/tank_left.png")
        else:
            self.image = pygame.image.load("images/tank_right.gif")
        self.gun_x = self.tank_pos_x+self.orientation*self.gun_length*math.cos(self.angle*57.3)
        self.gun_y = self.tank_pos_y-self.tank_height/2-15-self.gun_length*math.sin(self.angle*57.3)
        pygame.draw.line(surface,(97,124,50),(self.tank_pos_x,self.tank_pos_y-self.tank_height/2-15),(self.gun_x,self.gun_y),5)
        surface.blit(self.image,(self.tank_pos_x-self.tank_width/2,self.tank_pos_y-self.tank_height))
        if self.orientation == 1:
            self.tank_pos_x = min(self.tank_pos_x+time*self.speed*self.dir,scr_width/2-wall.wall_width/2-self.tank_width/2)
            self.tank_pos_x = max(self.tank_pos_x+time*self.speed*self.dir,self.tank_width/2)
        else:
            self.tank_pos_x = min(self.tank_pos_x+time*self.speed*self.dir,scr_width-self.tank_width/2)
            self.tank_pos_x = max(self.tank_pos_x+time*self.speed*self.dir,scr_width/2+wall.wall_width/2+self.tank_width/2)
        self.angle += self.gun_dir * self.gun_velocity
        self.drawHealthBar(surface)
        #self.gotHit()

    def fire(self,type):
        gunshot = pygame.mixer.Sound("sounds/gunshot.wav")
        curTime = time.time()
        if (curTime - self.lastCast1 > 1.5 and type == 1):
            self.lastCast1 = time.time()
            p = projectile((self.gun_x,self.gun_y),self.angle,self.orientation,type)
            channel = gunshot.play()
            if channel is not None:
                left,right = self.stereopan(self.tank_pos_x,scr_width)
                channel.set_volume(left,right)
        if (curTime - self.lastCast2 > 7 and type == 2):
            self.lastCast2 = time.time()
            p = projectile((self.gun_x,self.gun_y),self.angle,self.orientation,type)
            channel = gunshot.play()
            if channel is not None:
                left,right = self.stereopan(self.tank_pos_x,scr_width)
                channel.set_volume(left,right)

    def gotHit(self):
        if(time.time() - self.lastCast1 > 0.5):
            for x in active_projectiles:
                if(x.pos_y > scr_height-self.tank_height and x.pos_x < self.tank_pos_x+self.tank_width/2 and x.pos_x > self.tank_pos_x-self.tank_width/2):
                    active_projectiles.remove(x)
                    #self.health -= 10
                    return True
        left = self.tank_pos_x-self.tank_width/2
        right = self.tank_pos_x+self.tank_width/2
        for x in napalm_region:
            if ((left > napalm_region[x] and left < napalm_region[x]+napalm_width) or (right > napalm_region[x] and right < napalm_region[x]+napalm_width)):
                if(time.time() - self.gotBurnt > 0.5):
                    return True


    def drawHealthBar(self, surface):
        if self.health > 25:
            color_health_remaining = (53,155,41)
        else:
            color_health_remaining = (233,25,18)
        color_health_lost = (255,255,225)
        if self.orientation == 1:
            healthRemaining = ((50,50),(0.4*scr_width*self.health/100.,30))
            healthLost = ((50+0.4*scr_width*self.health/100.,50),(0.4*scr_width-0.4*scr_width*self.health/100.,30))
        else:
            healthLost = ((scr_width/2+80,50),(0.4*scr_width-0.4*scr_width*self.health/100,30))
            healthRemaining = ((scr_width/2+80+0.4*scr_width-0.4*scr_width*self.health/100,50),(0.4*scr_width*self.health/100,30))
        pygame.draw.rect(surface,color_health_remaining,healthRemaining)
        pygame.draw.rect(surface,color_health_lost,healthLost)

    def stereopan(self,position, width):
        rightVol = float(position)/width
        leftVol = 1.0 - rightVol
        return (leftVol,rightVol)

    def victory(self,surface):
        self.flag = pygame.image.load("images/flag.png")
        print "In Victory"
        print self.tank_pos_x,self.tank_height
        surface.blit(self.flag,(self.tank_pos_x,self.tank_height+250))

    def drawNapalm(self,surface):
        print napalm_region
        rem = 0
        for x in napalm_region:
            print float(x) - float(time.time())
            if(float(time.time()) - float(x)< 5):
                pygame.draw.line(surface,(0,0,0),(napalm_region[x],scr_height-10),(napalm_region[x]+napalm_width,scr_height-10),10)
            else:
                rem = x
        try:
            del napalm_region[rem]
        except:
            pass