# coding=gbk
from socket import *

# 1������һ������˵�Socket
socket_server = socket(AF_INET, SOCK_DGRAM)
# 2������������˵ĵ�ַ�Ͷ˿ں�
host_port = ('192.168.100.127', 8092)
# 3���������˵�Socket���󶨵�ַ�Ͷ˿ڣ�ֻ�а��˵�ַ�Ͷ˿ڣ����ܳ�֮Ϊ��������Socket
socket_server.bind(host_port)
# 4�����ܿͻ��˷��͹��������ݣ�ÿ�ν���1kb���ݣ��յ���ÿһ�����ݱ���������һ��Ԫ�飬Ԫ���һ��ֵ���������ݣ��ڶ���ֵ��Դ��ַ��Դ�˿ں�
data = socket_server.recvfrom(1024)  # ������д������Ϊ���ݵĴ�С
print(data[0].decode('utf-8'))
print(data)
# 5���ر��׽��֣��ͷ���Դ
socket_server.close()
