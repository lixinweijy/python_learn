#coding=gbk
from multiprocessing import Process
import os

def func1(name):  #��ͨһ���������ú������ӽ��̵���
    print("��ǰ����id:",os.getpid())  #getpid()��ȡ��ǰ���ú����Ľ���ID
    print("������id:",os.getppid())  #getppif()��ȡ��ǰ���̵ĸ�����ID
    print("��ǰ���̵�����",name)

#���
if __name__ == '__main__':
    #��������ӽ���������func1����
    for i in range(5):
        P=Process(target=func1,args=("����%d"%i,))  #����һ���ӽ��̣�������Ԫ��
        P.start() #��ʼ�ӽ���

    print("�����̴���ִ�����")
    #�����̵Ĵ�����Ĭ��û���κ�������ͬʱ�����̱���ȴ������ӽ��̽���֮��Ż����
