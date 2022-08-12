#coding=gbk
from socket import *
import time #time模块保证客户端发送多个数据包的时候，间隔时间长
client_socket=socket(AF_INET,SOCK_STREAM)

client_socket.connect(('192.168.85.127',8000))

client_socket.send('sbsbsb'.encode('utf-8'))
time.sleep(5) #让当前的线程休眠5秒

client_socket.send('lxw'.encode('utf-8'))

client_socket.close()
