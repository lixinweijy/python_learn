#coding=gbk
#UDP���ڻ��������ݹ���ʱ�ᶪʧ���ݣ���˲�����
#TCP�в��ᶪʧ���ݣ����ǻ���
'''
TCP����������ԭ��
1.���ݰ�̫С��һ����ն�ȡ
2.���ݰ�̫�󣬻�����ֻ�ܽ��ն�ȡ��һ����
3.Ϊ�����Ч�ʣ�TCPЭ��Ὣ����С���ҷ��ͼ���϶̵����ݰ��ϲ�����
'''

import socket
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(('',8099))

server_socket.listen(5)

new_socket,client_addr=server_socket.accept()

data1=new_socket.recv(1024)
data2=new_socket.recv(1024)

print('��һ������:',data1)
print('�ڶ�������:',data2)

new_socket.close()
server_socket.close()