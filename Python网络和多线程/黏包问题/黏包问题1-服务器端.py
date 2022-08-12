#coding=gbk
#UDP中在缓冲区数据过多时会丢失数据，因此不会黏包
#TCP中不会丢失数据，但是会黏包
'''
TCP中黏包的三个原因
1.数据包太小，一起接收读取
2.数据包太大，缓冲区只能接收读取到一部分
3.为了提高效率，TCP协议会将几个小的且发送间隔较短的数据包合并发送
'''

import socket
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(('',8099))

server_socket.listen(5)

new_socket,client_addr=server_socket.accept()

data1=new_socket.recv(1024)
data2=new_socket.recv(1024)

print('第一条数据:',data1)
print('第二条数据:',data2)

new_socket.close()
server_socket.close()