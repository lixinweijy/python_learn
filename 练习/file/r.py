# -*- coding:utf-8 -*-
file=open('file_w.txt','r',encoding="utf-8")
# print(file.tell()) #0
# print(file.read(2)) # 读取两个内容
# print(file.tell()) #4
# print(file.read(1))
# print(file.tell()) #6
# print(file.readline()) #读一行
# print(file.tell()) #12
# print(file.readlines()) #读每一行
# print(file.tell()) #32
# print("-------------------------------")
file.seek(0,2)
print(file.tell())  #5
# print(file.read(1)) #读换行
# print(file.tell()) #6
# file.seek(1)
# print(file.read())
file.close()
# print(len("abcdefg\nabcdefg"))  #15
# print(1,end="\n")
# print("")
# print(2)
print()