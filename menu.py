import pygame
from game_constants import *
from pygame.locals import *
import BattleTanks

class Main():
    def __init__(self):
        pygame.mixer.pre_init(44100,16,2,4096)
        pygame.init()
        self.running = True
        self.state = "mainMenu"
        self.screen = pygame.display.set_mode((scr_width,scr_height),pygame.FULLSCREEN,32)
        self.mBg = pygame.image.load("images/menu_background.png")
        self.quitCon = pygame.image.load("images/ball.png")
        self.play = pygame.image.load("images/play.png")
        self.yes = pygame.image.load("images/yes.png")
        self.yesF = pygame.image.load("images/yes_f.png")
        self.no = pygame.image.load("images/no.png")
        self.noF = pygame.image.load("images/no_f.png")
        self.panel = pygame.image.load("images/right_panel.png").convert_alpha()
        self.playF = pygame.image.load("images/play_f.png")
        self.quit = pygame.image.load("images/quit.png")
        self.quitF = pygame.image.load("images/quit_f.png")
        self.quitWindow = pygame.image.load("images/quit_window.png")
        self.leftPanelPos = (96,200)
        self.rightPanelPos = (697,200)
        self.quitPos = (200,352)
        self.quitConPos = (385,273)
        self.playPos = (200,240)
        self.yesPos = (468,390)
        self.noPos = (660,390)
        button = self.play

    def menuQuit(self):
        self.state = "quit"
        #self.running = False

    def run(self):
        x = 0
        mouseOver = pygame.mixer.Sound("sounds/mouseover.mp3")
        playButton = self.play
        quitButton = self.quit
        yesButton = self.yes
        noButton = self.no
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.menuQuit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.menuQuit()
                if self.play.get_rect().move(self.playPos).collidepoint(pygame.mouse.get_pos()) and self.state == "mainMenu":
                    #channel = mouseOver.play()
                    playButton = self.playF
                else:
                    playButton = self.play
                if self.quit.get_rect().move(self.quitPos).collidepoint(pygame.mouse.get_pos()) and self.state == "mainMenu":
                    quitButton = self.quitF
                else:
                    quitButton = self.quit
                if self.yes.get_rect().move(self.yesPos).collidepoint(pygame.mouse.get_pos()):
                    yesButton = self.yesF
                else:
                    yesButton = self.yes
                if self.no.get_rect().move(self.noPos).collidepoint(pygame.mouse.get_pos()):
                    noButton = self.noF
                else:
                    noButton = self.no
                if event.type == MOUSEBUTTONDOWN:
                    print event.pos
                    if playButton.get_rect().move(self.playPos).collidepoint(event.pos) and self.state == "mainMenu":
                        self.running = False
                        client = BattleTanks.Client()
                        client.run()
                    if quitButton.get_rect().move(self.quitPos).collidepoint(event.pos) and self.state == "mainMenu":
                        self.menuQuit()
                    if yesButton.get_rect().move(self.yesPos).collidepoint(event.pos) and self.state == "quit":
                        self.running = False
                    if noButton.get_rect().move(self.noPos).collidepoint(event.pos) and self.state == "quit":
                        self.state = "mainMenu"
            self.screen.blit(self.mBg,(0,0))
            self.screen.blit(self.panel,self.leftPanelPos)
            self.screen.blit(self.panel,self.rightPanelPos)
            self.screen.blit(quitButton,self.quitPos)
            self.screen.blit(playButton,self.playPos)
            #self.screen.blit(self.button2,self.quitPos)
            if self.state == "quit":
                self.screen.blit(self.quitWindow,self.quitConPos)
                self.screen.blit(yesButton,self.yesPos)
                self.screen.blit(noButton,self.noPos)
            pygame.display.update()

if __name__ == "__main__":
    menu = Main()
    menu.run()