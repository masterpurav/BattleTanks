__author__ = 'Purav'

import socket
import select



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
        print i
        if data[i] == "l":
            print "left"
            gameData[player]['tankDir'] = -1
            gameData[player]['fire'] = 0
        elif data[i] == "r":
            gameData[player]['fire'] = 0
            gameData[player]['tankDir'] = 1
        elif data[i] == "t":
            gameData[player]['fire'] = 0
            gameData[player]['tankDir'] = 0
        elif data[i] == "u":
            gameData[player]['fire'] = 0
            gameData[player]['gunDir'] = 1
        elif data[i] == "d":
            gameData[player]['fire'] = 0
            gameData[player]['gunDir'] = -1
        elif data[i] == "g":
            gameData[player]['fire'] = 0
            gameData[player]['gunDir'] = 0
        elif data[i] == "f":
            gameData[player]['fire'] = 1
        elif data[i] == "q":
            print "Client disconnected"
            connections.remove(sock)
    for sock in connections:
        print connections
        try:
            print gameData
            sock.send(str(gameData))
        except:
            sock.close()
            connections.remove(sock)

if __name__ == '__main__':
    gameData = [{
    'health':100,
    'tankDir':0,
    'gunDir':0,
    'fire':0
    },{
    'health':100,
    'tankDir':0,
    'gunDir':0,
    'fire':0
    }]
    player1 = ""
    player2 = ""
    connections = []
    port = 5555
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print "server ",server
    server.bind((socket.gethostname(),port))
    server.listen(3)
    connections.append(server)
    print 'Waiting for clients'
    while 1:
        readable,writable,exceptional = select.select(connections,[],[],0)
        for sock in readable:
            if sock == server:
                sockObj, addr = server.accept()
                connections.append(sockObj)
                if player1 == "":
                    player1 = str(sockObj)
                else:
                    player2 = str(sockObj)
                print 'Client (%s, %s) connected' % addr
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
                    continue

    server.close()

