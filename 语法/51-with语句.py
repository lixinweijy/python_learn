# with语句可以自动管理上下文文件，不论什么原因跳出with块，都能保证文件关闭正确，以此来达到释放资源的目的
print(type(open('a.txt','r')))
with open('a.txt','r') as file:
    print(file.read()) #自动关闭资源
'''
MyContenMgr实现了特殊方法__enter__().__exit__()称为该类对象遵守了上下文管理器协议
该类对象的实例对象称为上下文管理器
'''

class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用执行了')
        return self

    def __exit__(self,exc_type,exc_val,exc_tb):
        print('exit方法被调用了')

    def show(self):
        print('show方法被调用执行了')

with MyContentMgr() as file:  #相当于file=MyContentMgr（）
    file.show() #无论是否产生异常都调用特殊方法


with open('a.txt','rb') as src_file:
    with open('copya.txt','wb') as target_flie:
        target_flie.write(src_file.read())
# 自动关闭，不用手动关闭