#coding=gbk
import struct
from socket import *

server=socket(AF_INET,SOCK_STREAM)
server.bind(('',8001))
server.listen(5)

recv_data,recv_addr=server.accept()

f=open(r'D:\服务器.png','wb')

header_data=recv_data.recv(4)
size=struct.unpack('!i',header_data)[0] #不管有没有地址，unpack返回的都是一个元组，元组的第一个值就是长度

recv_size=0 #已经接收到多长的数据
while recv_size<size:
    data=recv_data.recv(1024)
    recv_size+=len(data) #接收的字节长度要累加
    f.write(data)

print()
f.close()
recv_data.close()