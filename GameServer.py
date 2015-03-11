__author__ = 'Purav'

import socket
import select

def handleClientData(sock,data):
    for sock in connections:
        try:
            sock.send(data)
        except:
            sock.close()
            connections.remove(sock)

if __name__ == '__main__':
    connections = []
    port = 5555
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((socket.gethostname(),port))
    server.listen(2)
    connections.append(server)
    print 'Waiting for clients'
    while 1:
        readable,writable,exceptional = select.select(connections,[],[],0)
        for sock in readable:
            if sock == server:
                sockObj, addr = server.accept()
                connections.append(sockObj)
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

