#coding=gbk
from socket import *

#1������server-socket
server_socket=socket(AF_INET,SOCK_STREAM)

#2����һ��IP�Ͷ˿�
host_port=('',8088)
server_socket.bind(host_port)

#3����������Socket����,listen��Socket���ڱ������Ϳ��Խ��տͻ��˵���������
server_socket.listen(1)

#4���ȴ��ͻ��˵���������,��ǰ�������߳������ĺ�����accept��������ֵ����һ�����µ�Socket
new_socket,client_addr=server_socket.accept()

#5�����������ܿͻ��˷��͹���������,recvһ������TCPЭ��Ľ������ݣ�recvfrom����UDP
data=new_socket.recv(1024)#data���ֽ�����

print('�������˽��յ�������:',data.decode('utf-8'))

#6���������������ݸ��ͻ���
new_socket.send('Thank you!'.encode('utf-8'))

#7���ر��׽���
new_socket.close()#new_socket�ر���ζ�ŵ�ǰ�ͻ��˵ķ����Ѿ����

server_socket.close()#�ر�����������