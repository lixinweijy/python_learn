#coding=gbk
import time
from functools import wraps

def main_logger(log_file='out.log'):
    def logger(func):
        @wraps(func)
        def write_logging(*args,**kwargs):
            log="[info]--时间是: %s"%time.strftime('%H:%M:%S',time.localtime())
            print(log)
            with open(log_file,'a')as f:
                f.write(log+"\n")
            func(*args,**kwargs)
        return write_logging
    return logger

@main_logger() #使用装饰器来给所有的work增加日志功能
def work():
    print("我在工作")

@main_logger()
def work1(name):
    print("%s 在工作"%name)

@main_logger()
def work2(name,name1):
    print("%s和%s在工作"%(name,name1))
work()

work1("lxw")

work2("lxw","br")

