#coding=gbk
import socket
# �����׽��֣�Socket��
s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#��ѡ��AF_INET(����internet����ͨ��),AF_UNIX(����ͬһ̨�������̼�ͨ��)
# Type:�׽������ͣ������ǿ�����SOCK_STREAM����ʽ�׽��֣���Ҫ����TCPЭ�飩����SOCK_DGRAM�����ݱ��׽��֣���Ҫ����UDPЭ�飩
s2=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print(s1)
print(s2)