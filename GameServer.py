__author__ = 'Purav'

import socket
import select
import game_constants

def formatAngle(number):
    number = round(number,3)
    x,sep,y = str(number).partition('.')
    for x in range(len(y),4):
        number+="0"
    print number

def handleClientData(sock,data):
    player = -1
    if str(sock) == player1:
        player = 0
        print "Player1 played"
    else:
        player = 1
        print "Player2 played"
    print data, " Data"
    for i in range(0,len(data)):
        if data[i] == "l":
            gameData[player]['tankDir'] = -1
        elif data[i] == "r":
            gameData[player]['tankDir'] = 1
        elif data[i] == "t":
            gameData[player]['tankDir'] = 0
        elif data[i] == "u":
            gameData[player]['gunAngle'] += 0.001
        elif data[i] == "d":
            gameData[player]['gunAngle'] -= 0.001
        elif data[i] == "f":
            gameData[player]['fire'] = 1
        elif data[i] == "z":
            gameData[player]['fire'] = 0
        elif data[i] == "h":
            gameData[abs(1-player)]['health'] -= 10
        elif data[i] == "q":
            print "Client disconnected"
            connections.remove(sock)
            print "Removed from here ", sock
            print connections
            gameData[player]['ready'] = 0
        broadcast()

def broadcast():
    for sock in connections:
        print connections
        try:
            print gameData
            sock.send(str(gameData))
        except:
            pass
            #sock.close()
            #connections.remove(sock)
            #print "Removed ",sock

if __name__ == '__main__':
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
    port = 5555
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print "server ",server
    server.bind((socket.gethostname(),port))
    connections.append(server)
    server.listen(3)
    print 'Waiting for clients'
    while 1:
        try:
            readable,writable,exceptional = select.select(connections,[],[],0)
            for sock in readable:
                if sock is server:
                    sockObj, addr = sock.accept()
                    connections.append(sockObj)
                    if player1 == "":
                        player1 = str(sockObj)
                        gameData[0]['ready'] = 1
                    else:
                        player2 = str(sockObj)
                        gameData[1]['ready'] = 1
                        broadcast()
                    #handleClientData(addr,data)

                else:
                    try:
                        data = sock.recv(1024)
                        if data:
                            message = data
                            handleClientData(sock,message)
                    except:
                        print "Client (%s,%s) disconnected" % addr
                        sock.close()
                        connections.remove(sock)
                        print "Removed from main ",sock
                        continue
        except:
            connections.append(server)
            continue
    server.close()

