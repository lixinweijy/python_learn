#coding=gbk
from socket import *
import time

recv_socket=socket(AF_INET,SOCK_STREAM)

recv_socket.bind(('',8000))

recv_socket.listen(5)

reserve_data,reserve_addr=recv_socket.accept()

print('连接成功',reserve_addr)

data1=reserve_data.recv(4)#第一次没有接受完整
print('第一个数据包',data1.decode('utf-8'))
time.sleep(6)
data2=reserve_data.recv(5)#第二次会接收旧数据，然后如果还有空间再接收后面的数据
print('第二个数据包',data2.decode('utf-8'))

reserve_data.close()
recv_socket.close()

