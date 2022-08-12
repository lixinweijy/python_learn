#coding='utf-8'
from socket import *

client_socket=socket(AF_INET,SOCK_STREAM)

client_socket.connect(('192.168.85.127',8099))

client_socket.send('hello'.encode('utf-8'))
client_socket.send('laoxiang'.encode('utf-8'))

client_socket.close()