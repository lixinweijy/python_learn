#coding=gbk
import functools

print(int("111")) #默认十进制转化
print(int("123",base=16)) #按照16进制转换

def int_2(num,base=2):
    return int(num,base)

print(int_2('1101'))

int_2=functools.partial(int,base=8)
print(int_2('1101'))


#把一个函数的某些参数固定住，返回一个新函数，这个新函数会更简单
