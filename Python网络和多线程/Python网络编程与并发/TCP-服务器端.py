#coding=gbk
from socket import *

#1、创建server-socket
server_socket=socket(AF_INET,SOCK_STREAM)

#2、绑定一个IP和端口
host_port=('',8088)
server_socket.bind(host_port)

#3、服务器的Socket监听,listen让Socket处于被动，就可以接收客户端的连接请求
server_socket.listen(1)

#4、等待客户端的连接请求,当前函数是线程阻塞的函数，accept返回两个值，第一个：新的Socket
new_socket,client_addr=server_socket.accept()

#5、服务器接受客户端发送过来的数据,recv一般用于TCP协议的接收数据，recvfrom用于UDP
data=new_socket.recv(1024)#data是字节数据

print('服务器端接收的数据是:',data.decode('utf-8'))

#6、服务器发送数据给客户端
new_socket.send('Thank you!'.encode('utf-8'))

#7、关闭套接字
new_socket.close()#new_socket关闭意味着当前客户端的服务已经完成

server_socket.close()#关闭整个服务器