import socket

host = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

message = input("Enter message: ")

client_socket.send(message.encode())

data = client_socket.recv(1024).decode()
print("Received from server:", data)

client_socket.close()