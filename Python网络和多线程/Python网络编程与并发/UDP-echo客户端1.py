#coding=gbk
from socket import *
#1���ͻ��˿��Է��Ͷ��� 2���ͻ����������һ��'exit'��ͻ����˳� 3�����������յ�ʲô�ͷ���ʲô

# ����һ��UDPЭ����׽��֣�Ȼ����һ�����ݵ������ϵ���һ������

#1�������׽���
client_socket=socket(AF_INET,SOCK_DGRAM)

#����������Ƿ��˳��ͻ��˵ı��
flag=True

# 2������һ��������Ϣ��Ŀ��,8080��һ��Ŀ��������Ķ˿ڣ�127.0.0.1��Ŀ���������ַ
server_host_port = ('192.168.112.127', 8093)

while flag:
    #3��׼���������ݣ�encode��ʾ����һ�ֱ����ʽ�����ݱ���ֽ�����bytes
    #����һ�����ֽ����ݲ��ܷ���
    datas=input('������:').encode('utf-8')

    #4����������,��ʶһ��������ͨ��IP+�˿�+Э��
    client_socket.sendto(datas,server_host_port)

    #һ�����Դӷ��������յ��Żع��������ݣ���ӡ��������ӡ������
    print("���ص�������:",client_socket.recvfrom(1024)[0].decode('utf-8'))

    if datas.decode('utf-8')=='exit':
        flag=False

#5���ر��׽��֣���ʵ�����ͷ���ϵͳ��Դ
client_socket.close()