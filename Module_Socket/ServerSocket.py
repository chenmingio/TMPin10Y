import sys
import socket

host = ''
port = 8888

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket

print("Socket Created")

try:
    ss.bind((host, port))  # 绑定socket和ip端口
except socket.error():  # TODO 这块经常报错，回头看看怎么回事
    print("Sending Failed")
    sys.exit()

print("Socket has been bounded")

ss.listen(10)  # 开始监听端口

print("Socket is Ready")

(conn, addr) = ss.accept()  # 开始接受外部的connection。同时建造一个新的子socket作为和客户端的链接用的socket。

# print(addr)
print("Connected with " + addr[0] + ":" + str(addr[1]))


while True:

    data = conn.recv(1024)
    print("OK. " + data.decode())
    if not data:
        break
    conn.sendall(data)

conn.close()
ss.close()

# socket和session是什么关系？Anyway, 客户端的socket只能存活一轮
