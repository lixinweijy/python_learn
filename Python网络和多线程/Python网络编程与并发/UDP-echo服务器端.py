#coding=gbk
from socket import *
#1���ͻ��˿��Է��Ͷ��� 2���ͻ����������һ��'exit'��ͻ����˳� 3�����������յ�ʲô�ͷ���ʲô

#1������һ������˵�Socket
socket_server=socket(AF_INET,SOCK_DGRAM)


#2������������˵ĵ�ַ�Ͷ˿ں�
host_port=('',8093)#�������������ʵ������С�ͷ�������IP��ַ�кܶ࣬Ҫ�κα�����IP��ַ���󶨾�ֻ��''

#3���������˵�Socket���󶨵�ַ�Ͷ˿ڣ�ֻ�а��˵�ַ�Ͷ˿ڣ����ܳ�֮Ϊ��������Socket
socket_server.bind(host_port)

while True:

    #4�����ܿͻ��˷��͹��������ݣ�ÿ�ν���1kb���ݣ��յ���ÿһ�����ݱ���������һ��Ԫ�飬Ԫ���һ��ֵ���������ݣ��ڶ���ֵ��Դ��ַ��Դ�˿ں�
    data=socket_server.recvfrom(1024)#������д������Ϊ���ݵĴ�С

    #�������յ�����֮��ԭ�ⲻ�����أ��������յ��ĸ��ͻ��˵���Ϣ�ͷ��ظ��ĸ��ͻ���
    socket_server.sendto(data[0],data[1])

    print(data[0].decode('utf-8'))


#5���ر��׽��֣��ͷ���Դ
socket_server.close()
