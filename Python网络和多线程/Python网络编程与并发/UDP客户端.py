# coding=gbk
from socket import *
# 创建一个UDP协议的套接字，然后发送一条数据到网络上的另一个进程

# 1、创建套接字
client_socket = socket(AF_INET, SOCK_DGRAM)
# 2、定义一个接受消息的目标,8080是一个目标服务器的端口，127.0.0.1是目标服务器地址
server_host_port = ('192.168.100.127', 8092)
# 3、准备发送数据，encode表示按照一种编码格式把数据变成字节数组bytes
# 数据一定是字节数据才能发送
data = input('请输入:').encode('utf-8')
# 4、发送数据,标识一个进程是通过IP+端口+协议
client_socket.sendto(data, server_host_port)
print('发送完成')
# 5、关闭套接字，其实就是释放了系统资源
client_socket.close()
