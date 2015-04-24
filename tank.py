__author__ = 'Purav'

import pygame
import ast
import math
from game_constants import *
from proj import projectile, active_projectiles
from wall import wall
import time
import random

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
    shield = 0

    class FlameSprite:
        def __init__(self):
            super(self.FlameSprite, self).__init__()
            self.flames = []
            self.flames1.append(pygame.image.load("images/flames_trial.png"))
            self.flames2.append(pygame.image.load("images/flames_trial_2.png"))
            self.flames3.append(pygame.image.load("images/flames_trial_3.png"))
            self.index = 0
            self.image = self.flames[self.index]


        def update(self):
            self.index += 1
            if self.index > len(self.flames):
                self.index = 0
            self.image = self.flames[self.index]
    # Constructor
    def __init__(self,(posx,posy),color,orientation):
        self.tank_pos_x = posx
        self.tank_pos_y = posy
        self.tank_color = color
        self.orientation = orientation
        self.shieldUsed = 0
        self.shFlag = 0
        self.shieldImage = pygame.image.load("images/shield.png")
        self.flames1 = (pygame.image.load("images/flames_trial.png"))
        self.flames2 = (pygame.image.load("images/flames_trial_2.png"))
        self.flames3 = (pygame.image.load("images/flames_trial_3.png"))
        self.flames = [self.flames1, self.flames2, self.flames3]
        self.napalm = pygame.image.load("images/fire2.png")
        self.napalmD = pygame.image.load("images/fire1.png")
        self.cannon = pygame.image.load("images/cannon2.png")
        self.cannonD = pygame.image.load("images/cannon1.png")
        self.shieldIc = pygame.image.load("images/shield2.png")
        self.shieldIcD = pygame.image.load("images/shield1.png")

    def drawIcons(self,screen):
        if time.time() - self.lastCast1 > 1.5:
            cannon = self.cannon
        else:
            cannon = self.cannonD
        if time.time() - self.lastCast2 > 7:
            napalm = self.napalm
        else:
            napalm = self.napalmD
        if self.shield == 0:
            shield = self.shieldIc
        else:
            shield = self.shieldIcD
        if self.orientation == 1:
            screen.blit(cannon,(50,100))
            screen.blit(napalm,(120,100))
            if self.shieldUsed == 0:
                screen.blit(shield,(190,100))
        else:
            screen.blit(cannon,(scr_width-100,100))
            screen.blit(napalm,(scr_width-170,100))
            if self.shieldUsed == 0:
                screen.blit(shield,(scr_width-240,100))

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
        if self.shFlag == 1 and self.shield == 0:
            self.shieldUsed = 1
        if self.shield == 1:
            self.shFlag = 1
            surface.blit(self.shieldImage,(self.tank_pos_x-114,self.tank_pos_y-90))
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
        if self.shield == 0:
            if(time.time() - self.lastCast1 > 0.5):
                for x in active_projectiles:
                    if(x.pos_y > scr_height-self.tank_height and x.pos_x < self.tank_pos_x+self.tank_width/2 and x.pos_x > self.tank_pos_x-self.tank_width/2) and x.type == 1:
                        active_projectiles.remove(x)
                        #self.health -= 10
                        return True

    def burnt(self):
        if self.shield == 0:
            left = self.tank_pos_x-self.tank_width/2
            right = self.tank_pos_x+self.tank_width/2
            for x in napalm_region:
                if ((left > napalm_region[x] and left < napalm_region[x]+napalm_width) or (right > napalm_region[x] and right < napalm_region[x]+napalm_width)):
                    if(time.time() - self.gotBurnt > 0.5):
                        self.gotBurnt = time.time()
                        print "Burnt"
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
        surface.blit(self.flag,(self.tank_pos_x,self.tank_height+250))

    def drawNapalm(self,surface):
        rem = 0
        for x in napalm_region:
            i = 0
            if(float(time.time()) - float(x)< 5):
                #pygame.draw.line(surface,(0,0,0),(napalm_region[x],scr_height-10),(napalm_region[x]+napalm_width,scr_height-10),10)
                surface.blit(self.flames[random.randint(0,2)],(napalm_region[x],scr_height-150))
            else:
                rem = x
        try:
            del napalm_region[rem]
        except:
            pass