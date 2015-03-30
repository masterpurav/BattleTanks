__author__ = 'Purav'

import socket
import select
import game_constants

class Game:

    gameData = [{
        'ready':0,
        'tankDir':0,
        'gunAngle':0,
        'fire':0
        },{
        'ready':0,
        'tankDir':0,
        'gunAngle':0,
        'fire':0
        }]
    player1 = ""
    player2 = ""
    connections = []

    def clearGameData(self):
        self.connections = []
        self.gameData = gameData = [{
        'ready':0,
        'tankDir':0,
        'gunAngle':0,
        'fire':0
        },{
        'ready':0,
        'tankDir':0,
        'gunAngle':0,
        'fire':0
        }]
        self.player1 = ""
        self.player2 = ""

    def __init__(self,player1,player2):
        self.clearGameData()
        self.player1 = str(player1)
        self.player2 = str(player2)
        self.connections.append(player1)
        self.connections.append(player2)
        self.gameData[0]['ready'] = 1
        self.gameData[1]['ready'] = 1
        self.broadcast()
        print "Game instance created"
        print "Connections : ",self.connections
        print "Player 1 : ",self.player1
        print "Player 2 : ",self.player2



    def handleClientData(self,sock,data):
        player = -1
        if str(sock) == self.player1:
            player = 0
            print "Player1 played"
        else:
            player = 1
            print "Player2 played"
        print data, " Data"
        for i in range(0,len(data)):
            if data[i] == "l":
                self.gameData[player]['tankDir'] = -1
            elif data[i] == "r":
                self.gameData[player]['tankDir'] = 1
            elif data[i] == "t":
                self.gameData[player]['tankDir'] = 0
            elif data[i] == "u":
                self.gameData[player]['gunAngle'] += 0.001
            elif data[i] == "d":
                self.gameData[player]['gunAngle'] -= 0.001
            elif data[i] == "f":
                self.gameData[player]['fire'] = 1
            elif data[i] == "z":
                self.gameData[player]['fire'] = 0
            elif data[i] == "h":
                self.gameData[abs(1-player)]['health'] -= 10
            elif data[i] == "q":
                print "Client disconnected"
                self.connections.remove(sock)
                print "Removed from here ", sock
                if player == 0:
                    self.player1 = ""
                    print "Setting player1 to empty",self.player1
                self.gameData[player]['ready'] = 0
                print "Dropped player is ",player

            self.broadcast()

    def broadcast(self):
        for sock in self.connections:
            try:
                print self.gameData
                sock.send(str(self.gameData))
            except:
                pass
                #sock.close()
                #connections.remove(sock)
                #print "Removed ",sock

if __name__ == '__main__':
    games = []
    cgMap = {}
    clients = []
    waitList = []
    port = 5555
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print "server ",server
    server.bind((socket.gethostname(),port))
    clients.append(server)
    server.listen(3)
    print 'Waiting for clients'
    while 1:
        try:
            readable,writable,exceptional = select.select(clients,[],[],0)
            for sock in readable:
                if sock is server:
                    print "Server is readable."
                    sockObj, addr = sock.accept()
                    clients.append(sockObj)
                    print "Added ",sockObj," to clients."
                    waitList.append(sockObj)
                    print "Added ",sockObj," to waitList."
                    print "CG Map : ",cgMap
                    if len(waitList) % 2 == 0:
                        print "Game created "
                        g = Game(waitList[0],waitList[1])
                        print "with id : ",g
                        cgMap[str(waitList[0])] = g
                        cgMap[str(waitList[1])] = g
                        print "Added sockets to cgMap. "
                        print cgMap
                        games.append(g)
                        waitList.remove(waitList[0])
                        waitList.remove(waitList[0])
                    #handleClientData(addr,data)

                else:
                    try:
                        print "Client is readable."
                        print "CG Map : ",cgMap
                        data = sock.recv(1024)
                        if data:
                            message = data
                            print "Games running : ",len(games)
                            game = cgMap[str(sock)]
                            game.handleClientData(sock,message)
                    except Exception as e:
                        print "Exception ",e
                        print "Client (%s,%s) disconnected" % addr
                        sock.close()
                        # Handle this properly later
                        clients.remove(sock)
                        print "Removed from main ",sock
                        continue
        except:
            clients.append(server)
            continue
    server.close()

