from pynput import mouse
import threading
import socket

screen_width, screen_height = 1920, 1080  # Replace with actual screen dimensions

def check_screen_edge(x, y):
    if x <= 0:
        return 'left'
    elif x >= screen_width - 1:
        return 'right'
    elif y <= 0:
        return 'top'
    elif y >= screen_height - 1:
        return 'bottom'
    else:
        return None

def send_control_signal(target_ip, x, y):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((target_ip, 12345))
    data = f"{x},{y}"
    client_socket.sendall(data.encode())
    client_socket.close()

def on_move(x, y):
    edge = check_screen_edge(x, y)
    if edge:
        print(f"Mouse moved to the {edge} edge")
        send_control_signal('target_ip_address', x, y)  # Replace 'target_ip_address' with actual IP

with mouse.Listener(on_move=on_move) as listener:
    listener.join()
