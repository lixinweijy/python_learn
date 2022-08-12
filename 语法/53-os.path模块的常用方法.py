'''
abspath(path)  用于获取文件或目录的绝对路径
exists(path)   用于判断文件和目录是否存在，如果存在返回True，否则返回False
join(path,name)将目录与目录或文件名拼接起来
splitext()     分离文件名和扩展名
basename(path) 从一个目录中提取文件名
dirname(path)  从一个路径中提取文件路径，不包括文件名
isdir(path)    用于判断是否为路径
'''
import os.path
print(os.path.abspath('a.txt'))
print(os.path.exists('a.txt'),os.path.exists('e.txt'))
print(os.path.join('D:','a.txt'))
print(os.path.split('D://a.txt'))  #将目录与文件进行拆分
print(os.path.splitext('D://a.txt')) #拆分文件及后缀名
print(os.path.basename('D://a.txt')) #提取文件名
print(os.path.dirname('D://a.txt'))  #提取文件路径
print(os.path.isdir('D://a.txt'))    #判断是否为路径

print('----------课堂案例---------')
# 列出指定目录下的所有py文件
path=os.getcwd()
lst=os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)

# walk 用于遍历指定目录下所有的文件及目录
lst_files=os.walk(path)
print(lst_files)
for dirpath,dirname,filename in lst_files:
    print(dirpath)
    print(dirname)
    print(filename)
    print('-------------------')
    for dir in dirname:
        print(os.path.join(dirpath,dir))
    for file in filename:
        print(os.path.join(dirpath,file))
    print('----------------------')