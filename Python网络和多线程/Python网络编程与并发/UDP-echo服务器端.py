#coding=gbk
from socket import *
#1、客户端可以发送多条 2、客户端如果发送一个'exit'则客户端退出 3、服务器端收到什么就返回什么

#1、创建一个服务端的Socket
socket_server=socket(AF_INET,SOCK_DGRAM)


#2、定义服务器端的地址和端口号
host_port=('',8093)#如果服务器是真实的物理小型服务器，IP地址有很多，要任何本机的IP地址都绑定就只用''

#3、服务器端的Socket来绑定地址和端口，只有绑定了地址和端口，才能称之为服务器的Socket
socket_server.bind(host_port)

while True:

    #4、接受客户端发送过来的数据，每次接受1kb数据，收到的每一个数据报，里面是一个元组，元组第一个值是数据内容，第二个值是源地址和源端口号
    data=socket_server.recvfrom(1024)#里面填写的数据为数据的大小

    #服务器收到数据之后原封不动返回，而且是收到哪个客户端的信息就返回给哪个客户端
    socket_server.sendto(data[0],data[1])

    print(data[0].decode('utf-8'))


#5、关闭套接字，释放资源
socket_server.close()
