#coding=gbk
import os.path
from socket import *
import struct
import os

client=socket(AF_INET,SOCK_STREAM)
client.connect(('192.168.143.127',8001))

#�ͻ��˴���һ���ļ��������� gift2.png
file_path='gift2.png'
f=open(file_path,'rb')

#�ڷ����������ļ�����֮ǰ,��׼��һ����ͷ
size=os.path.getsize(file_path) #�ļ����ֽڳ���
#����һ����ͷ��iΪ4���ֽڵ�int
header=struct.pack('!i',size) #���շ���ʹ��struct������õ�һ��int��������
client.send(header)

#�����ļ�����
while True:
    data=f.read(1024) #ÿ�ζ�ȡ1024�ֽ�
    if not data:
        break
    client.send(data) #���͸����������ļ�����

print('�ͻ����ϴ��ļ����')
client.close()
f.close()