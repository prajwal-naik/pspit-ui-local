from socket import *
import time

def heartBeat(pseudoClientName, pseudoClientPort):
    while(1):
        try:
            clientSocket = socket(AF_INET, SOCK_STREAM)
            clientSocket.connect((pseudoClientName,pseudoClientPort))
            clientSocket.send("HEART_BEAT".encode())
            heartbeat_response = clientSocket.recv(1024)
            if(heartbeat_response.decode() == "new"):
                return clientSocket
        except:
            print("Server doesn't have new content...\n")
            if(clientSocket): 
                clientSocket.close()


def main(port = 12000, message = "Hello World"):
    #----------------client to pseudo-client--------------------------
    pseudoClientName = "localhost"
    pseudoClientPort = int(port)
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((pseudoClientName,pseudoClientPort))
    print("Connected to pseudo-client on localhost:12000\n")
    # requestMessage = input("Input lowercase requestMessage:")
    requestMessage = message
    clientSocket.send(requestMessage.encode())
    reqStatus = clientSocket.recv(1024).decode()
    print(reqStatus, "\n")
    clientSocket.close()

    # -----------------heart beat-------------------------------------
    clientSocket = heartBeat(pseudoClientName, pseudoClientPort)

    #---------------pseudo-client to client--------------------------
    print("Pseudo-server response ready\n")
    serverResponse = clientSocket.recv(1024).decode()
    print ("From Server: ", serverResponse)
    clientSocket.close()
    return serverResponse

if __name__ == "__main__":
    main()