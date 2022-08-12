#coding=gbk
import time
from functools import wraps

def main_logger(log_file='out.log'):
    def logger(func):
        @wraps(func)
        def write_logging(*args,**kwargs):
            log="[info]--ʱ����: %s"%time.strftime('%H:%M:%S',time.localtime())
            print(log)
            with open(log_file,'a')as f:
                f.write(log+"\n")
            func(*args,**kwargs)
        return write_logging
    return logger

@main_logger() #ʹ��װ�����������е�work������־����
def work():
    print("���ڹ���")

@main_logger()
def work1(name):
    print("%s �ڹ���"%name)

@main_logger()
def work2(name,name1):
    print("%s��%s�ڹ���"%(name,name1))
work()

work1("lxw")

work2("lxw","br")

