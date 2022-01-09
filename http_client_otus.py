import socket
import random

LOCALHOST = "127.0.0.1"
PORT = random.randint(20000, 30000)
my_socket = socket.socket()
address_and_port = (LOCALHOST, PORT)
my_socket.bind(address_and_port)
print("Started socket on", address_and_port)

my_socket.listen(10)

conn, addr = my_socket.accept()
print("Got connection", conn, addr)

# Получаем данные из соединения
data = conn.recv(1024)
print("Got data", data.decode("utf-8"))
headers = data.decode("utf-8")

# Отправляем ответ
conn.send(f"HTTP/1.1 200 OK\n Content-Length: 100\n Connection: close\n Content-Type: text/html\n\n <h1>{headers}</h1>".encode("utf-8"))

my_socket.close()