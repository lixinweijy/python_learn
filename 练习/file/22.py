# -*- coding:utf-8 -*-
with open("aaa.txt","w") as f:
    f.write("a2sdjfdkhsdkfjssfk撒卡卡的21233")
with open("aaa.txt","r") as file:
    print(file.tell())  # 0
    print(file.read(2))  # 读取两个内容
    print(file.tell())  # 2
    print(file.read(1))
    print(file.tell())  # 3
    print(file.readline())  # 读一行
    print(file.tell())  # 12
    print(file.readlines())  # 读每一行
    print(file.tell())  # 32