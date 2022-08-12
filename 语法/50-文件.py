#文件的读写原理
'''
从外到内存叫读
从内存到外叫写
'''
file=open('a.txt','r')
print(file.readlines())  #readlines读取所有内容，以集合的形式写出来
file.close()

# 常用的文件打开模式
'''
r 以只读模式打开文件，文件的指针将会放在文件开头
w 以只读模式打开文件，文件不存在则创建，存在则覆盖原有内容，文件指针在文件开头
a 以追加模式打开文件，不存在则创建，指针在文件开头，存在则在文件末尾追加内容，文件指针在原文件末尾
b 以二进制方式打开，不能单独使用，需要与其他模式一起使用，rb，或者wb
+ 以读写方式打开文件，不能单独使用，需要与其他模式一起使用
'''
file=open('b.txt','w')
file.write('python ')
file.write("lalall")
file.close()

file=open('b.txt','a')
file.write('python')
file.close()
'''
src_file=open('logo.png','rb') # 要在有这个图片的时候使用

target_file=open('copylogo.png','wb')

target_file.write(src_file.read())

target_file.close()
src_file.close()
'''

# 文件对象的常用方法
file=open('a.txt','r')
print(file.read(2)) # 读取两个内容
print(file.readline()) #读一行
print(file.readlines()) #读每一行

file=open('c.txt','a')
# file.write('hello') 将字符串str写入文件
lst=['java','go','python'] # 将字符串列表写入文本文件,不添加换行符
file.writelines(lst)
file.close()
print('------------------')
file=open('a.txt','r')
file.seek(2) #文件指针移到新位置,0从开头计算,1从当前位置计算,2从末尾计算
print(file.read())
print(file.tell()) #返回文件指针当前位置
file.close()

# flush 把缓冲区的资源写进文件,不关闭资源
# close 写内容并关闭一切资源
file=open('d.txt','a')
file.write('hello')
file.flush()
file.write('world') #flush之后可以继续写内容,但不关闭资源
file.close()
