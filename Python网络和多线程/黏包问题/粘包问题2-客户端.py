#coding=gbk
from socket import *
import time #timeģ�鱣֤�ͻ��˷��Ͷ�����ݰ���ʱ�򣬼��ʱ�䳤
client_socket=socket(AF_INET,SOCK_STREAM)

client_socket.connect(('192.168.85.127',8000))

client_socket.send('sbsbsb'.encode('utf-8'))
time.sleep(5) #�õ�ǰ���߳�����5��

client_socket.send('lxw'.encode('utf-8'))

client_socket.close()
