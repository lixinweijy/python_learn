# -*- coding:utf-8 -*-
with open('商品基本库文件.txt', 'r+', encoding="utf-8") as rfile:
    txt_1=rfile.readline()
    lst_1=eval(txt_1.strip('\n').split(',')[0])

