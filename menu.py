import pygame
from game_constants import *
from pygame.locals import *
import BattleTanks

class Main():
    def __init__(self):
        pygame.mixer.pre_init(44100,16,2,4096)
        pygame.init()
        self.running = True
        self.mBg = pygame.image.load("images/menu_background.png")
        self.screen = pygame.display.set_mode((scr_width,scr_height),pygame.FULLSCREEN,32)
        self.quitCon = pygame.image.load("images/ball.png")
        self.play = pygame.image.load("images/play.png")
        self.panel = pygame.image.load("images/right_panel.png").convert_alpha()
        self.state = "mainMenu"
        self.playF = pygame.image.load("images/play_f.png")
        self.quit = pygame.image.load("images/quit.png")
        self.quitF = pygame.image.load("images/quit_f.png")
        self.quitWindow = pygame.image.load("images/quit_window.png")
        self.leftPanelPos = (96,200)
        self.rightPanelPos = (697,200)
        self.quitPos = (200,352)
        self.quitConPos = (385,273)
        self.playPos = (200,240)
        button = self.play

    def menuQuit(self):
        self.state = "quit"
        #self.running = False

    def run(self):
        x = 0
        mouseOver = pygame.mixer.Sound("sounds/mouseover.mp3")
        playButton = self.play
        quitButton = self.quit
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.menuQuit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False
                if self.play.get_rect().move(self.playPos).collidepoint(pygame.mouse.get_pos()) and self.state == "mainMenu":
                    #channel = mouseOver.play()
                    playButton = self.playF
                else:
                    playButton = self.play
                if self.quit.get_rect().move(self.quitPos).collidepoint(pygame.mouse.get_pos()) and self.state == "mainMenu":
                    quitButton = self.quitF
                else:
                    quitButton = self.quit
                if event.type == MOUSEBUTTONDOWN:
                    print event.pos
                    print pygame.mouse.get_pos()
                    if playButton.get_rect().move(self.playPos).collidepoint(event.pos) and self.state == "mainMenu":
                        self.running = False
                        client = BattleTanks.Client()
                        client.run()
                    if quitButton.get_rect().move(self.quitPos).collidepoint(event.pos) and self.state == "mainMenu":
                        self.menuQuit()
                    #if self.quitCon.get_rect().move(self.quitConPos).collidepoint(event.pos) and self.state == "quit":
                        #self.state = "menuMain"
                        #self.running = False
            self.screen.blit(self.mBg,(0,0))
            self.screen.blit(self.panel,self.leftPanelPos)
            self.screen.blit(self.panel,self.rightPanelPos)
            self.screen.blit(quitButton,self.quitPos)
            self.screen.blit(playButton,self.playPos)
            #self.screen.blit(self.button2,self.quitPos)
            if self.state == "quit":
                self.screen.blit(self.quitWindow,self.quitConPos)
            pygame.display.update()

if __name__ == "__main__":
    menu = Main()
    menu.run()