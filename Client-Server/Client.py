
import socket

HOST = '127.0.0.1'  # Server address
PORT = 65432        # Same port as server

filename = input("Enter file name to request: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:

    client_socket.connect((HOST, PORT))

    client_socket.sendall(filename.encode())

    data = client_socket.recv(4096).decode()

    print("\n--- File Content ---")
    print(data)
