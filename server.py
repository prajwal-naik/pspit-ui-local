from socket import *

def heartBeat(pseudoServerName, pseudoServerPort):
    while(1):
        try:
            pseudoServerSocket = socket(AF_INET, SOCK_STREAM)
            pseudoServerSocket.connect((pseudoServerName,pseudoServerPort))
            pseudoServerSocket.send("HEART_BEAT".encode())
            heartbeat_response = pseudoServerSocket.recv(1024)
            if(heartbeat_response.decode() == "new"):
                return pseudoServerSocket
        except:
            print("Pseudo-server doesn't have new request...\n")
            if(pseudoServerSocket):
                pseudoServerSocket.close()


def main():
    pseudoServerName = "localhost"
    pseudoServerPort = 14000
    while(1):
#------------------send heart beats to pseudo-server----------------------------
        pseudoServerSocket = heartBeat(pseudoServerName, pseudoServerPort)

#------------------recieve request from pseudo-server---------------------------
        clientReq = pseudoServerSocket.recv(1024)
        print("Server recieved request: {}\n".format(clientReq.decode()))
        print("Server preparing response...\n")
        #response = clientReq.decode()
        response=input().encode()

#-----------------send request to pseudo-server----------------------------------------
        pseudoServerSocket.send(response)
        print("Server sent response...\n")
        pseudoServerSocket.close()


if __name__ == "__main__":
    main()
