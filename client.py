import socket
import pyautogui

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9868

client_socket.connect((host,port))

message = client_socket.recv(1024)

print(message.decode('ascii'))
client_socket.close()
