#coding=gbk
from socket import *
import time

recv_socket=socket(AF_INET,SOCK_STREAM)

recv_socket.bind(('',8000))

recv_socket.listen(5)

reserve_data,reserve_addr=recv_socket.accept()

print('���ӳɹ�',reserve_addr)

data1=reserve_data.recv(4)#��һ��û�н�������
print('��һ�����ݰ�',data1.decode('utf-8'))
time.sleep(6)
data2=reserve_data.recv(5)#�ڶ��λ���վ����ݣ�Ȼ��������пռ��ٽ��պ��������
print('�ڶ������ݰ�',data2.decode('utf-8'))

reserve_data.close()
recv_socket.close()

