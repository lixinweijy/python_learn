#coding=gbk
import socket
# 创建套接字（Socket）
s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#可选择AF_INET(用于internet进程通信),AF_UNIX(用于同一台机器进程间通信)
# Type:套接字类型，可以是可以是SOCK_STREAM（流式套接字，主要用于TCP协议）或者SOCK_DGRAM（数据报套接字，主要用于UDP协议）
s2=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print(s1)
print(s2)