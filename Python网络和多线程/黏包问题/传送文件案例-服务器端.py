#coding=gbk
import struct
from socket import *

server=socket(AF_INET,SOCK_STREAM)
server.bind(('',8001))
server.listen(5)

recv_data,recv_addr=server.accept()

f=open(r'D:\������.png','wb')

header_data=recv_data.recv(4)
size=struct.unpack('!i',header_data)[0] #������û�е�ַ��unpack���صĶ���һ��Ԫ�飬Ԫ��ĵ�һ��ֵ���ǳ���

recv_size=0 #�Ѿ����յ��೤������
while recv_size<size:
    data=recv_data.recv(1024)
    recv_size+=len(data) #���յ��ֽڳ���Ҫ�ۼ�
    f.write(data)

print()
f.close()
recv_data.close()