import socket
import signal
import sys


HOST = "127.0.0.1"
PORT = 9868


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST,PORT))
server_socket.listen(5)

print("server is listening")

while True:
    try:
        client_socket, addr = server_socket.accept()
        print(f"Got connection from {addr}")
        message  = "This is the message I am sending"
        client_socket.send(message.encode('ascii'))
        client_socket.close()

    except KeyboardInterrupt:
        print("Closing the server")
        server_socket.close()
        sys.exit(0)
