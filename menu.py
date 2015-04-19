import pygame
from game_constants import *
from pygame.locals import *
import BattleTanks

class Main():
    def __init__(self):
        pygame.mixer.pre_init(44100,16,2,4096)
        pygame.init()
        self.my_font = pygame.font.Font("fonts/ArmyRust.ttf",24)
        self.running = True
        self.state = "mainMenu"
        self.screen = pygame.display.set_mode((scr_width,scr_height),pygame.FULLSCREEN,32)
        self.mBg = pygame.image.load("images/menu_background.png")
        self.addrPrompt = pygame.image.load("images/server.png")
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
        self.cancel = pygame.image.load("images/cancel.png")
        self.cancelF = pygame.image.load("images/cancel_f.png")
        self.connect = pygame.image.load("images/connect.png")
        self.connectF = pygame.image.load("images/connect_f.png")
        self.textbox = pygame.image.load("images/ip.png")
        self.errorPanel = pygame.image.load("images/unable_server.png")
        self.ok = pygame.image.load("images/ok.png")
        self.okF = pygame.image.load("images/ok_f.png")
        self.leftPanelPos = (96,200)
        self.rightPanelPos = (697,200)
        self.quitPos = (200,352)
        self.quitConPos = (385,273)
        self.playPos = (200,240)
        self.yesPos = (468,390)
        self.noPos = (660,390)
        self.connectPos = (464,432)
        self.cancelPos = (666,432)
        self.textboxPos = (478,356)
        self.okPos = (556,396)
        x,y = self.textboxPos
        self.fontPos = (x+10,y+7)
        self.ip = ""

    def menuQuit(self):
        self.state = "quit"

    def menuPlay(self):
        self.ip = ""
        self.state = "play"
        #self.running = False

    def beginPlay(self):
        try:
            client = BattleTanks.Client()
            client.setServer(''.join(self.ip.split(" ")))
            client.run()
        except Exception as e:
            self.state = "error"

            print str(e.__unicode__())
    def handleInput(self):
        self.ip = ""


    def run(self):
        x = 0
        mouseOver = pygame.mixer.Sound("sounds/mouseover.mp3")
        playButton = self.play
        quitButton = self.quit
        yesButton = self.yes
        noButton = self.no
        cancelButton = self.cancel
        connectButton = self.connect
        okButton = self.ok
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.menuQuit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.menuQuit()
                    if event.key == K_0 or event.key == K_KP0:
                        self.ip += " 0"
                    if event.key == K_1 or event.key == K_KP1:
                        self.ip += " 1"
                    if event.key == K_2 or event.key == K_KP2:
                        self.ip += " 2"
                    if event.key == K_3 or event.key == K_KP3:
                        self.ip += " 3"
                    if event.key == K_4 or event.key == K_KP4:
                        self.ip += " 4"
                    if event.key == K_5 or event.key == K_KP5:
                        self.ip += " 5"
                    if event.key == K_6 or event.key == K_KP6:
                        self.ip += " 6"
                    if event.key == K_7 or event.key == K_KP7:
                        self.ip += " 7"
                    if event.key == K_8 or event.key == K_KP8:
                        self.ip += " 8"
                    if event.key == K_9 or event.key == K_KP9:
                        self.ip += " 9"
                    if event.key == K_KP_PERIOD or event.key == K_PERIOD:
                        self.ip += " ."
                    if event.key == K_BACKSPACE:
                        self.ip = self.ip[:-2]
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
                if self.connect.get_rect().move(self.connectPos).collidepoint(pygame.mouse.get_pos()):
                    connectButton = self.connectF
                else:
                    connectButton = self.connect
                if self.cancel.get_rect().move(self.cancelPos).collidepoint(pygame.mouse.get_pos()):
                    cancelButton = self.cancelF
                else:
                    cancelButton = self.cancel
                if self.ok.get_rect().move(self.okPos).collidepoint(pygame.mouse.get_pos()):
                    okButton = self.okF
                else:
                    okButton = self.ok
                if event.type == MOUSEBUTTONDOWN:
                    print event.pos
                    cancelPos = event.pos
                    if playButton.get_rect().move(self.playPos).collidepoint(event.pos) and self.state == "mainMenu":
                        self.menuPlay()
                    if quitButton.get_rect().move(self.quitPos).collidepoint(event.pos) and self.state == "mainMenu":
                        self.menuQuit()
                    if yesButton.get_rect().move(self.yesPos).collidepoint(event.pos) and self.state == "quit":
                        self.running = False
                    if noButton.get_rect().move(self.noPos).collidepoint(event.pos) and self.state == "quit":
                        self.state = "mainMenu"
                    if connectButton.get_rect().move(self.connectPos).collidepoint(event.pos) and self.state == "play":
                        self.beginPlay()
                    if cancelButton.get_rect().move(self.cancelPos).collidepoint(event.pos) and self.state == "play":
                        self.state = "mainMenu"
                    if self.textbox.get_rect().move(self.textboxPos).collidepoint(event.pos) and self.state == "play":
                        self.handleInput()
                    if okButton.get_rect().move(self.okPos).collidepoint(event.pos) and self.state == "error":
                        self.state = "mainMenu"
            self.screen.blit(self.mBg,(0,0))
            self.screen.blit(self.panel,self.leftPanelPos)
            self.screen.blit(self.panel,self.rightPanelPos)
            self.screen.blit(quitButton,self.quitPos)
            self.screen.blit(playButton,self.playPos)
            if self.state == "quit":
                self.screen.blit(self.quitWindow,self.quitConPos)
                self.screen.blit(yesButton,self.yesPos)
                self.screen.blit(noButton,self.noPos)
            if self.state == "play":
                self.screen.blit(self.addrPrompt,self.quitConPos)
                self.screen.blit(connectButton,self.connectPos)
                self.screen.blit(cancelButton,self.cancelPos)
                self.screen.blit(self.textbox,self.textboxPos)
                img = self.my_font.render(self.ip,True,(24,123,54))
                self.screen.blit(img,self.fontPos)
            if self.state == "error":
                self.screen.blit(self.errorPanel,self.quitConPos)
                self.screen.blit(okButton,self.okPos)
            pygame.display.update()

if __name__ == "__main__":
    menu = Main()
    menu.run()