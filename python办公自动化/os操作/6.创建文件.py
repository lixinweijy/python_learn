# -*- coding:utf-8 -*-
import os

# 在创建文件夹之前，要先判断要创建的文件夹是否存在，不存在就创建
# mkdir创建单层文件夹
if not os.path.exists("mkdir创建的文件夹"):
    os.mkdir("mkdir创建的文件夹")  # 只能创建不存在的文件夹

# makedirs()  创建多层文件夹 ，当最里面那层文件夹存在是，程序会报错
if not os.path.exists("第一层文件夹/第二次文件夹"):
    os.makedirs("第一层文件夹/第二次文件夹")
