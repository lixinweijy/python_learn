#coding=gbk
from functools import wraps
import time
# 使用类做装饰器
class Logs(object):
    def __init__(self,log_file="out.log",level="info"):
        self.log_file=log_file
        self.level=level

    def __call__(self,func):# 定义装饰器，需要存一个接收函数
        @wraps(func)
        def write_logging(*args, **kwargs):
            log = "[%s]--时间是: %s" %(self.level,time.strftime('%H:%M:%S', time.localtime()))
            print(log)
            with open(self.log_file, 'a') as f:
                f.write(log + "\n")
            func(*args, **kwargs)
        return write_logging

@Logs() #使用装饰器来给所有的work增加日志功能
def work():
    print("我在工作")

@Logs()
def work1(name):
    print("%s 在工作"%name)

@Logs(log_file='work.log',level="WARNING")
def work2(name,name1):
    print("%s和%s在工作"%(name,name1))
work()

work1("lxw")

work2("lxw","br")