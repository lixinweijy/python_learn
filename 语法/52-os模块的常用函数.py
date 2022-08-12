# os模块是与操作系统相关的一个模块
import os
# os.system('notepad.exe')
# os.system('calc.exe')
# 直接调用可执行文件
os.startfile(r'C:\Program Files (x86)\Tencent\QQ\Bin\qq.exe')
'''
getcwd()  返回当前的工作目录
listdir（path）  返回指定路径下的文件和目录信息
mkdir（path[,mode])  创建目录
makedirs（path1/path2...[,mode])  创建多级目录
rmdir（path）  删除目录
removedirs（path1/path2......)  删除多级目录
chdir（path）  将path设置为当前工作目录
'''

print(os.getcwd())

lst=os.listdir('../语法')
print(lst)

# os.mkdir('newdir')  创建目录
# os.makedirs('A/B/C')  创建多级目录
# os.rmdir('newdir')  删除目录
# os.removedirs('A/B/C')  删除多级目录
# os.chdir('C:\Program Files (x86)\Tencent\QQ\Bin')  将路径设为当前目录