#coding=gbk
from multiprocessing import Process
import os
import time
class MyProcess(Process):
    def __init__(self,xname):
        Process.__init__(self) #���ظ����ṩ�Ĺ���
        self.name=xname

    def run(self):  #�ӽ��������й�����ִ�еĺ���
        print("��ǰ����id:", os.getpid())  # getpid()��ȡ��ǰ���ú����Ľ���ID
        print("������id:", os.getppid())  # getppif()��ȡ��ǰ���̵ĸ�����ID
        print("��ǰ���̵�����", self.name)
        time.sleep(3)
if __name__ == '__main__':
    start=time.time()
    process_list=[]
    for i in range(10):
        #����10���ӽ��̷���һ���б���
        p=MyProcess("process-%d"%(i+1))#�����Զ���ĺ���
        p.start()
        process_list.append(p)  #���ӽ��̷����б���
    for p in process_list:
        #����һ�㶼����Ҫ�����̵ȴ������ӽ��̽�������ִ�к���Ĵ��룬join�ȴ���ǰ�ӽ��̽���
        p.join() #join()��һ�������ĺ���
    #�����ӽ��̽�����
    r=time.time()-start
    print("ʮ���ӽ���ִ�е�ʱ����{}".format(r))
# �ӽ��̲����޸ĸ������еı���