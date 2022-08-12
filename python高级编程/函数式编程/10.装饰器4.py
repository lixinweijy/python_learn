#coding=gbk
from functools import wraps
import time
# ʹ������װ����
class Logs(object):
    def __init__(self,log_file="out.log",level="info"):
        self.log_file=log_file
        self.level=level

    def __call__(self,func):# ����װ��������Ҫ��һ�����պ���
        @wraps(func)
        def write_logging(*args, **kwargs):
            log = "[%s]--ʱ����: %s" %(self.level,time.strftime('%H:%M:%S', time.localtime()))
            print(log)
            with open(self.log_file, 'a') as f:
                f.write(log + "\n")
            func(*args, **kwargs)
        return write_logging

@Logs() #ʹ��װ�����������е�work������־����
def work():
    print("���ڹ���")

@Logs()
def work1(name):
    print("%s �ڹ���"%name)

@Logs(log_file='work.log',level="WARNING")
def work2(name,name1):
    print("%s��%s�ڹ���"%(name,name1))
work()

work1("lxw")

work2("lxw","br")