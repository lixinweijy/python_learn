#coding=gbk
from socket import *
import struct
#�������˵�socket
s=socket(AF_INET,SOCK_DGRAM)

#��IP�Ͷ˿ں�
s.bind(('',68))

def download(filename,client_ip,client_port):
    #����һ���µ�socket�����Ʒ����ļ����ݵ����ݰ����ͻ���
    new_socket=socket(AF_INET,SOCK_DGRAM)

    #�ļ��������ݰ��ļ�����,��ʵ���ǿ�ı��
    num=1

    #����ͻ����˳��ı�ǩ
    flag=True
    try:
        f=open(filename,'rb')
    except:
        error_package=struct.pack('!HH5sb',5,5,'error'.encode('utf-8'),0) #H ��ʾpython��Integerת��C��û�з��ŵ�short��5s ��ʾ��Python�а���5���ַ����ַ���ת��C���ַ�����
        new_socket.sendto(error_package,(client_ip,client_port)) #�Ѵ������ݷ����ͻ���
        exit() #��ǰ�߳̽�������ǰ�ͻ����˳�������
        flag=False
    #����ļ����ڣ���ô��Ҫ���ļ��������г�һ���������ݰ����͸��ͻ��ˣ�һ�����ݰ���������Ϊ512�ֽ�
    while flag:
        #���ļ����ݻ��ܶ�ȡ512�ֽ�
        read_data=f.read(512)
        #����һ�����ݰ�
        data_package=struct.pack('!HH',3,num)+read_data
        #�������ݰ�
        new_socket.sendto(data_package,(client_ip,client_port))
        if len(read_data)<512:#�ļ����ݵ����ݸպö���
            print("�ͻ���:%s,�ļ��������"%client_ip)
            break#��ǰ�ͻ����˳�
        #����������ACK��ȷ������
        recv_ack=new_socket.recvfrom(1024)
        operator_code,ack_num=struct.unpack('!HH',recv_ack[0])
        print('�ͻ���:%s����ȷ����Ϣ��'%client_ip,ack_num)
        num+=1
        #�����Դ���
        if int(operator_code)!=4 or int(ack_num)<1:#��������ack��ȷ����Ϣ
            break
    if f:
        f.close()
    new_socket.close()#�ͻ��������˳���




def server():
    while True:
        #���������ſͻ��˷��͹������ݣ�Ȼ����Ž���
        recv_data,(client_ip,client_port)=s.recvfrom(1024)
        print(recv_data,client_ip,client_port)
        #�ж����ݰ��Ƿ��ǣ��ͻ�����������ݰ�
        if struct.unpack('!b5sb',recv_data[-7:])==(0,b'octet',0):
            #�õ��������ֵ
            operator_code=struct.unpack('!H',recv_data[:2])
            #�õ��ļ���
            file_name=recv_data[2:-7].decode('utf-8')

            if operator_code[0]==1:#�������1�������ص��������ݰ�
                print('�ͻ����������ļ�:%s'%file_name)
                download(file_name,client_ip,client_port)

if __name__ == '__main__':
    server()
