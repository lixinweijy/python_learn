# coding=gbk
from socket import *
# ����һ��UDPЭ����׽��֣�Ȼ����һ�����ݵ������ϵ���һ������

# 1�������׽���
client_socket = socket(AF_INET, SOCK_DGRAM)
# 2������һ��������Ϣ��Ŀ��,8080��һ��Ŀ��������Ķ˿ڣ�127.0.0.1��Ŀ���������ַ
server_host_port = ('192.168.100.127', 8092)
# 3��׼���������ݣ�encode��ʾ����һ�ֱ����ʽ�����ݱ���ֽ�����bytes
# ����һ�����ֽ����ݲ��ܷ���
data = input('������:').encode('utf-8')
# 4����������,��ʶһ��������ͨ��IP+�˿�+Э��
client_socket.sendto(data, server_host_port)
print('�������')
# 5���ر��׽��֣���ʵ�����ͷ���ϵͳ��Դ
client_socket.close()
