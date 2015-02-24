__author__ = 'Purav'


import pygame
from pygame.locals import *
from sys import exit
from tank import tank
from game_constants import *
from projectile import active_projectiles, projectile

pygame.init()
background = pygame.image.load("images/background.jpg")
screen = pygame.display.set_mode((scr_width,scr_height),pygame.FULLSCREEN,32)
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
            if event.key == K_SPACE:
                A.fire()
            if event.key == K_ESCAPE:
                exit()
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                A.dir = 0
            if event.key == K_UP or event.key == K_DOWN:
                A.gun_dir = 0
    screen.blit(background,(0,0))
    time = clock.tick()/1000.
    A.drawTank(screen,time)
    B.drawTank(screen,time)
    B.gotHit()
    A.gotHit()
    A.drawHealthBar(screen)
    B.drawHealthBar(screen)
    for x in active_projectiles:
        x.drawProjectile(screen,time)
    pygame.display.update()
