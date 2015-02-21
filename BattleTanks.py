__author__ = 'Purav'


import pygame
from pygame.locals import *
from sys import exit
import math

scr_height = 480
scr_width = 640
time = 0
class tank:
    orientation = 1
    tank_height = 50
    tank_width = 75
    gun_length = 70
    gun_dir = 0
    dir = 0
    speed = 250
    tank_pos_x = 0
    tank_pos_y = 0
    angle = 0
    tank_color = (01,0,0)
    gun_velocity = 0.0001
    # Constructor
    def __init__(self,(posx,posy),color,orientation):
        self.tank_pos_x = posx
        self.tank_pos_y = posy
        self.tank_color = color
        self.orientation = orientation
    # Move left
    def moveLeft(self):
        print "In move left"
        self.dir = -1

    # Move Right
    def moveRight(self):
        print "In move right"
        self.dir = 1

    # Gun up
    def gunUp(self):
        print "In gun up"
        self.gun_dir = 1

    # Gun down
    def gunDown(self):
        self.gun_dir = -1

    def drawTank(self):
        global time
        pygame.draw.line(screen,(211,54,0),(self.tank_pos_x,self.tank_pos_y-self.tank_height/2),(self.tank_pos_x+self.orientation*self.gun_length*math.cos(self.angle*57.3),self.tank_pos_y-self.tank_height/2-self.gun_length*math.sin(self.angle*57.3)),5)
        pygame.draw.rect(screen,self.tank_color,Rect((self.tank_pos_x-self.tank_width/2,self.tank_pos_y-self.tank_height),(self.tank_width,self.tank_height)))
        self.tank_pos_x += time*self.speed*self.dir
        self.angle += self.gun_dir * self.gun_velocity

pygame.init()
background = pygame.image.load("images/background.jpg")
screen = pygame.display.set_mode((scr_width,scr_height),0,32)
clock = pygame.time.Clock()
A = tank((100,scr_height),(211,0,0),1)
B = tank((scr_width - 100,scr_height),(0,100,0),-1)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                A.moveLeft()
            if event.key == K_RIGHT:
                A.moveRight()
            if event.key == K_UP:
                A.gunUp()
            if event.key == K_DOWN:
                A.gunDown()
        if event.type == KEYUP:
            A.dir = 0
            A.gun_dir = 0
    screen.blit(background,(0,0))

    time = clock.tick()/1000.
    A.drawTank()
    B.drawTank()
    pygame.display.update()
