#coding=gbk
from socket import*

server_socket=socket(AF_INET,SOCK_STREAM)
host_port=('192.168.178.1',8009)
server_socket.bind(host_port)
server_socket.listen(1)
print("-----lxw----")
while True:
    new_socket,clien_socket=server_socket.accept()

    while True:
        recv_data=new_socket.recv(1024)
        if len(recv_data)>0:#�ͻ���û���˳������ҷ������ݵ���������
            print('lxw:',recv_data.decode('utf-8'))
        if recv_data.decode('utf-8')=='exit':
            print('lxw�Ѿ��˳�����')
            break

        #�������ݸ��ͻ���
        send_data=input('lzy:')
        if len(send_data)>0:
            new_socket.send(send_data.encode('utf-8'))

    new_socket.close()

server_socket.close()
