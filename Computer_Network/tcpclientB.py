from socket import *

serverName = "192.168.56.1"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    modifiedSentence = clientSocket.recv(1024).decode() #변환된 문자열을 콘솔창에 계속 띄운다.
    print('From Server:', modifiedSentence)
clientSocket.close()