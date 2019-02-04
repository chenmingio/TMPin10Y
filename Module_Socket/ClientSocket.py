import sys
import socket

# 造了一个插头，名字叫cs。它connect了什么/实际做了什么事情？
try:
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Failed to connect")
    sys.exit()

# bug trace/显示你这一步成功了
print("Socket Created")


host = "localhost"
port = 8888
myip = '107.151.181.184'

# 使用socket.gethostbyname()来DNS解析
try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror():
    print("Hostname can not be resolved")
    sys.exit()

# 改成某个网站后，虽然DNS反馈了ip地址，但没法链接，同时也没有进入error的loop。后来一分钟以后反馈：[Errno 60] Operation timed out


print("IP Address: " + remote_ip)

# 插头cs和远端的ip端口链接
cs.connect((myip, port))

print("Socket Connected to " + host + " using IP " + remote_ip)

# 用http格式发送请求

message = "GET / HTTP/1.1\r\n\r\n"

try:
    cs.sendall(message.encode())
    print(message.encode())
except socket.error():
    print("Did not send successfully")
    sys.exit()

print("Message Sent successfully!")

reply = cs.recv(4096)

print(reply.decode())

cs.close()
