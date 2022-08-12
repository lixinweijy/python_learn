# -*- coding:utf-8 -*-
from tempfile import TemporaryFile
file=TemporaryFile("w+")
file.write("老师我，我是学生")
file.seek(0)
print(file.readlines())
print(file.name)
input("你先别结束，我先去找找\n")  #所以的确会存在这么一个文件，但是程序结束后文件就没了
file.close()


with TemporaryFile("w+") as file:
    file.write("杨老师最好了")
    file.seek(2)
    print(file.readlines())
