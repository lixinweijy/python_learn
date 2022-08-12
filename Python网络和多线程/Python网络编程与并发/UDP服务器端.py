# coding=gbk
from socket import *

# 1、创建一个服务端的Socket
socket_server = socket(AF_INET, SOCK_DGRAM)
# 2、定义服务器端的地址和端口号
host_port = ('192.168.100.127', 8092)
# 3、服务器端的Socket来绑定地址和端口，只有绑定了地址和端口，才能称之为服务器的Socket
socket_server.bind(host_port)
# 4、接受客户端发送过来的数据，每次接受1kb数据，收到的每一个数据报，里面是一个元组，元组第一个值是数据内容，第二个值是源地址和源端口号
data = socket_server.recvfrom(1024)  # 里面填写的数据为数据的大小
print(data[0].decode('utf-8'))
print(data)
# 5、关闭套接字，释放资源
socket_server.close()
