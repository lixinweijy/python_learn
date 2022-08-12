#coding=gbk
from socket import*

client_socket=socket(AF_INET,SOCK_STREAM)

server_ip_port=('192.168.178.1',8009)
client_socket.connect(server_ip_port)
print("-----lzy----")
while True:
    send_data=input('lxw:')
    if len(send_data)>0:
        client_socket.send(send_data.encode('utf-8'))
    if send_data=='exit':
        client_socket.close()
        break

    #客户端接收服务器返回的数据
    recv_data=client_socket.recv(1024)
    print('lzy:',recv_data.decode('utf-8'))

client_socket.close()