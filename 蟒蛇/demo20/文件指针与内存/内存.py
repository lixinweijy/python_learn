# -*- coding:utf-8 -*-
import ctypes
import sys
# value = 13242343543234243243242  # 定义一个字符串变量
# num=sys.getsizeof(value)
# print(num)
# value2 = 13242343543234243243243  # 定义一个字符串变量
# address = id(value)  # 获取value的地址，赋给address
# address2=id(value2)
# get_value = ctypes.cast(address, ctypes.py_object).value  # 读取地址中的变量
# print(address2-address)

# value =2**24  # 定义一个字符串变量
# num=sys.getsizeof(value)
# print(num,type(num))
# value2 =2**24+1  # 定义一个字符串变量
# address = id(value)  # 获取value的地址，赋给address
# address2=id(value2)
# get_value = ctypes.cast(address+32, ctypes.py_object).value  # 读取地址中的变量
# print(address2-address)
# print(get_value)

print("李".encode("gbk"))
print("李".encode("utf-8"))
with open("img/熊哥.jpg",'rb') as aa:
    img=aa.read()
    print(img)
    # with open("ss.jpg",'wb') as bb:
    #     bb.write(img)