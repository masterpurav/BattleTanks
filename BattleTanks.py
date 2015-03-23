__author__ = 'Purav'

import socket
import select
import pygame
import ast
from pygame.locals import *
from sys import exit
from tank import tank
from game_constants import *
from projectile import active_projectiles, projectile
from wall import wall
import time
import threading

class Client():

    def __init__(self):
        self.lastUpdate = time.time()
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server = "192.168.1.6"
        self.serverPort = 5555
        self.readList = [self.client]
        #try:
            #self.client.sendto("c",(self.server,self.serverPort))
        self.client.connect((self.server,self.serverPort))
        #except:
            #print 'Unable to connect to server'
            #exit()
        #self.client.send("c")
        print 'Successfully connected to server'
        self.initializeGame()

    def initializeGame(self):
        pygame.mixer.pre_init(44100,16,2,4096)
        pygame.init()
        self.background = pygame.image.load("images/background.jpg")
        self.screen = pygame.display.set_mode((scr_width,scr_height),pygame.FULLSCREEN,32)
        self.gameClock = pygame.time.Clock()
        self.separatorWall = wall()
        self.A = tank((100,scr_height),(211,0,0),1)
        self.B = tank((scr_width - 100,scr_height),(0,100,0),-1)

    def handleKey(self,action):
        if action == "left":
            self.client.sendto("l",(self.server,self.serverPort))
        elif action == "right":
            self.client.sendto("r",(self.server,self.serverPort))
        elif action == "up":
            self.client.sendto("u",(self.server,self.serverPort))
        elif action == "down":
            self.client.sendto("d",(self.server,self.serverPort))
        elif action == "space":
            self.client.sendto("f",(self.server,self.serverPort))
        elif action == "tankZero":
            self.client.sendto("t",(self.server,self.serverPort))
        elif action == "gunZero":
            self.client.sendto("g",(self.server,self.serverPort))
        elif action == "fireZero":
            self.client.sendto("z",(self.server,self.serverPort))
        elif action == "hit":
            self.client.sendto("h",(self.server,self.serverPort))
        elif action == "quit":
            self.client.sendto("q",(self.server,self.serverPort))
            self.client.close()
            exit()

    def handleData(self,data):
        data = data[0:181]
        print data
        try:
            data = ast.literal_eval(data)
        except:
            print "Malformed string, ", data
            return
        self.A.dir = data[0]['tankDir']
        self.B.dir = data[1]['tankDir']
        #self.A.angle = data[0]['gunAngle']
        #self.B.gun_dir = data[1]['gunAngle']
        self.A.angle = data[0]['gunAngle']
        self.B.angle = data[1]['gunAngle']
        '''
        self.A.tank_pos_x = data[0]['tankpos']
        self.B.tank_pos_x = data[1]['tankpos']
        self.A.angle = data[0]['gunAngle']
        self.B.angle = data[1]['gunAngle']
        '''
        #self.A.health = data[0]['health']
        #self.B.health = data[1]['health']
        if data[0]['fire'] == 1:
            self.A.fire()
        if data[1]['fire'] == 1:
            self.B.fire()

    def run(self):
        running = True
        while running:
            readable, writable, exceptional = select.select(self.readList,[],[],0)
            for r in readable:
                data = r.recv(181)
                if not data:
                    print 'Server disconnected'
                    exit()
                else:
                    print data
                    self.handleData(data)
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.handleKey("quit")
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.handleKey("left")
                    if event.key == K_RIGHT:
                        self.handleKey("right")
                    if event.key == K_UP:
                        self.handleKey("up")
                    if event.key == K_DOWN:
                        self.handleKey("down")
                    if event.key == K_SPACE:
                        self.handleKey("space")
                    if event.key == K_ESCAPE:
                        self.handleKey("quit")
                if event.type == KEYUP:
                    if event.key == K_LEFT or event.key == K_RIGHT:
                        self.handleKey("tankZero")
                    if event.key == K_UP or event.key == K_DOWN:
                        self.handleKey("gunZero")
                    if event.key == K_SPACE:
                        self.handleKey("fireZero")
            self.screen.blit(self.background,(0,0))
            ctime = self.gameClock.tick()/1000.
            self.A.drawTank(self.screen,ctime)
            self.B.drawTank(self.screen,ctime)
            self.separatorWall.draw(self.screen)
            self.separatorWall.hit_wall()
            for x in active_projectiles:
                x.drawProjectile(self.screen,ctime)
            pygame.display.update()

if __name__ == '__main__':
    client = Client()
    client.run()