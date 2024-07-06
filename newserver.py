import socket
import threading
from pynput.mouse import Controller as MouseController

def handle_client(client_socket):
    mouse = MouseController()
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        x, y = map(int, data.decode().split(','))
        mouse.position = (x, y)
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(5)
    print("Server listening on port 12345")
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

start_server()
