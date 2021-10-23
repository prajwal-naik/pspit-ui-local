from socket import *
import time

def respondHeartBeat(toServerPort):
    toServerSocket = socket(AF_INET, SOCK_STREAM)
    toServerSocket.bind(("", toServerPort))
    toServerSocket.listen(1)
    print("Listening to heart beat...\n")
    toServerConnSocket, ServerAddr = toServerSocket.accept()
    hb = toServerConnSocket.recv(1024).decode()
    toServerConnSocket.send("new".encode())
    print("Responded to heartbeat...\n")
    return toServerConnSocket, toServerSocket

#-----------------pseudo-client to pseudo-server--------------------------------
# time.sleep(5)
fromPseudoClientPort = 13000
fromPseudoClientSocket = socket(AF_INET, SOCK_STREAM)
fromPseudoClientSocket.bind(("26.252.9.38", fromPseudoClientPort)) #add pseudo-server ip address
print("Listening for client request...\n")
fromPseudoClientSocket.listen(1)
fromPseudoClientConnSocket, pseudoClientAddr = fromPseudoClientSocket.accept()
clientReq = fromPseudoClientConnSocket.recv(1024).decode()
print("From client: {}\n".format(clientReq))
fromPseudoClientSocket.close()
fromPseudoClientConnSocket.close()
#print("line 27 closed\n")

#---------------pseudo-server to server-----------------------------------------

# time.sleep(5)
serverPort = 14000
serverName = "localhost"
toServerConnSocket, toServerSocket = respondHeartBeat(serverPort)
toServerConnSocket.send(clientReq.encode())

#---------------server to pseudo-server-----------------------------------------
res = toServerConnSocket.recv(1024).decode()
print("Response from server:{}\n".format(res))
toServerConnSocket.close() 
toServerSocket.close()
#print("line 42 closed\n")

#----------------timer for demo purpose-----------------------------------------
print(".....Sleeping for 10 secs for demo purposes only.....")
time.sleep(10)
#---------------pseudo-server_ pseudo-client--------------------------------------------

toPseudoClientSocket = socket(AF_INET, SOCK_STREAM)
toPseudoClientSocket.bind(("26.252.9.38", fromPseudoClientPort)) #add pseudo-server ip address
toPseudoClientSocket.listen(1)
toPseudoClientConnSocket, pseudoClientAddr = toPseudoClientSocket.accept()

toPseudoClientConnSocket.send(res.encode())

toPseudoClientConnSocket.close()
toPseudoClientSocket.close()
#print("line 56 closed\n")





