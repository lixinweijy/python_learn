#coding=gbk
from socket import *
import struct  #����python���ݽṹ��c�������ݽṹת��

file_name=input('�������ļ���:')
#�ͻ���
s=socket(AF_INET,SOCK_DGRAM)

#����Ŀ��������ĵ�ַ�Ͷ˿ں�
host_port=('192.168.148.101',68)

#'!H%dsb5sb'�����ʽ:!��ͷ����������ݰ�
data_package=struct.pack('!H%dsb5sb'%len(file_name),1,file_name.encode('utf-8'),0,'octet'.encode('utf-8'),0)

#�����ݰ����͵�Ŀ�������
s.sendto(data_package,host_port)

#�ͻ�������Ҫ����һ���հ׵��ļ�
f=open('client_'+file_name,'ab')

while True:
    #�ͻ��˽��շ����������������ݣ�����ֻ������:1�������ļ��������ݰ� 2��error��Ϣ��
    recv_data,(server_ip,server_port)=s.recvfrom(1024)

    operator_code,num=struct.unpack('!HH',recv_data[:4])#��ǰ�ĸ��ֽڵ����ݽ������

    if int(operator_code)==5:#�ж����ݰ��Ƿ���error��Ϣ��
        print('���������أ���Ҫ���ص��ļ������ڣ�')
        break
    #������ļ����ݵ����ݣ���Ҫ�����ļ�����

    f.write(recv_data[4:])

    if len(recv_data) <516:#��ζ�ŷ��������͹������ļ��Ѿ���������
        print('�ͻ������سɹ�')
        break

    #�ͻ����յ����ݰ�֮�󣬻���Ҫ����һ��ȷ��ACK��������
    ack_package=struct.pack('!HH',4,num)
    s.sendto(ack_package,(server_ip,server_port))
#�ͷ���Դ
f.close()
s.close()

