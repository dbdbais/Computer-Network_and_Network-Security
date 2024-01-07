from socket import *
import threading    #다중 클라이언트 처리하기 위한 쓰레드 라이브러리
clients = []    #클라이언트 소켓들 저장

def handle_client(sender):
    while True:
        sentence = sender.recv(1024).decode()
        if(sentence): print('sentence received')
        capitalizedSentence = sentence.upper()  #대문자 변환
        for c in clients:
            if c != sender: #보낸 클라이언트는 제외
                c.send(capitalizedSentence.encode())    #대문자로 변환된 문자열 전송

def main():
    serverPort = 12000
    serverName = "192.168.56.1"

    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((serverName, serverPort))
    serverSocket.listen(2)  #2개의 클라이언트 까지 listen
    print("The server is ready to receive")
    while True:
        connectionSocket, addr = serverSocket.accept()
        clients.append(connectionSocket)

        thread = threading.Thread(target=handle_client,args=(connectionSocket,)) #쓰레드 생성후 실행해야 하는 함수와 매개변수(Client A) 넘긴다
        thread.start()  #쓰레드 시작

    serverSocket.close()

main()

