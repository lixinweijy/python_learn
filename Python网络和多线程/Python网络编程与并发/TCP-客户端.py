#coding=gbk
from socket import*

client_socket=socket(AF_INET,SOCK_STREAM)

#�ͻ��˷������ӵ����󣨲��Ǵ������ݣ�

#Ŀ���������IP�Ͷ˿ں�
server_ip_port=('192.168.178.1',8088)
client_socket.connect(server_ip_port)

send_data=input('�����룺')
client_socket.send(send_data.encode('utf-8'))

#���շ��������ص�����
recv_data=client_socket.recv(1024)

print('�ͻ��˽��յ��ķ���������Ϊ��',recv_data.decode('utf-8'))

client_socket.close()
