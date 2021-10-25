from socket import *
import time

def respondHeartBeat(toClientPort):
    toClientSocket = socket(AF_INET, SOCK_STREAM)
    toClientSocket.bind(("", toClientPort))
    toClientSocket.listen(1)
    print("Listening to heart beat...\n")
    toClientConnSocket, clientAddr = toClientSocket.accept()
    hb = toClientConnSocket.recv(1024).decode()
    toClientConnSocket.send("new".encode())
    return toClientConnSocket, toClientSocket


# def main():
#---------------------client to pseudo-client------------------------------------------
fromClientPort = 12000
fromClientSocket = socket(AF_INET, SOCK_STREAM)
fromClientSocket.bind(("", fromClientPort))
fromClientSocket.listen(1)
print("Listening for client request...\n")
fromClientConnSocket, clientAddr = fromClientSocket.accept()
dataFromClient = fromClientConnSocket.recv(1024).decode()
print("Data from client: {}\n".format(dataFromClient))
fromClientConnSocket.send("Pseudo-client has recieved request".encode())
fromClientConnSocket.close()
fromClientSocket.close()

#----------------------------------pseudo-client to pseudo-server------------------------
# time.sleep(5)
toPseudoServerPort = 13000
toPseudoServerName = "26.252.9.38"  #added pseudo-server ip address
toPseudoServerSocket = socket(AF_INET, SOCK_STREAM)
toPseudoServerSocket.connect((toPseudoServerName,toPseudoServerPort))
toPseudoServerSocket.send(dataFromClient.encode())
toPseudoServerSocket.close()
while(1):
    try: 
        time.sleep(1)
        fromPseudoServerSocket = socket(AF_INET, SOCK_STREAM)
        fromPseudoServerSocket.connect((toPseudoServerName,toPseudoServerPort))
        print("Connection to pseudo-server re-established\n")
        break
    except:
        # pass
        print("Pseudo-server does not have new reponse...")
        time.sleep(1)


#-------------pseudo-server to pseudo-client--------------------------------------------

# while(1):
#     try:
#         responseFromServer = fromPseudoServerSocket.recv(1024).decode()
#         break
#     except:
#         pass
# time.sleep(10)

fromPseudoServerSocket.send("Pseudo-client is ready to recieve reponse".encode())
print("SUCCESSFULLY SENT RTS")
responseFromServer = fromPseudoServerSocket.recv(1024).decode()



print("Response recieved from server: {}\n".format(responseFromServer))
fromPseudoServerSocket.close()

#----------------timer for demo purpose-----------------------------------------

print(".....Sleeping for 10 secs for demo purposes only.....")
time.sleep(10)


#------------------pseudo-client to client----------------------------------------------
toClientConnSocket, toClientSocket = respondHeartBeat(fromClientPort)
toClientConnSocket.send(responseFromServer.encode())
print("Sent server response...\n")
toClientConnSocket.close()
toClientSocket.close()


# if __name__ == "__main__":
#     main()







