import socket

print("This tool was built by Israel")

Websocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Websocket.bind(('localhost', 81))

Websocket.listen(5)

while True:
    print('Waiting for connections')
    (recvSocket, address)= Websocket.accept()
    print('HTTP request received:')
    print(recvSocket.recv(1024))
    recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n <html><body><h1> Hello from Hackers-Arise!</h1></body></h1> \r\n", 'utf-8'))
    recvSocket.close()
