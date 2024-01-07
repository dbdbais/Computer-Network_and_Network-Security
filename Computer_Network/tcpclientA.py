from socket import *

serverName = "192.168.56.1"
serverPort = 12000

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
while True:
    sentence = input('Input lowercase sentence:')   #입력 받아서 서버로 전송만 수행
    clientSocket.send(sentence.encode())

#modifiedSentence = clientSocket.recv(1024)
#print('From Server:', modifiedSentence.decode())
clientSocket.close()