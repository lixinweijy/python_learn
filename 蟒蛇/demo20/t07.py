#新知识点1：正则表达式（通配符）
#新知识点2：文件指针与定位
#【高级】1）学习画出文件内存图；2）理解“utf-8”，“ANSI”编码格式
import re
li=re.findall('".*?"', 'hello“我们”, 为人治病，"大"自称"大贤良师"“super”自称"天公将军"，张宝称"地公将军"，fdsf“fs”')
#.表示至少1个字符，*表示0-N个字符，?表示"XXXXX"格式只匹配1次
print(li)
'''
for i in range(len(li)):
    li[i]=li[i].replace('"','')
print(li)
'''

fi=open('data7.txt','r',encoding='utf-8')
a=[]

a.append(fi.readline())
print(a)
print(fi.tell())

a.append(fi.readline())
print(a)
print(fi.tell())

a.append(fi.readline())
print(a)
print(fi.tell())

a.append(fi.readline())
print(a)
print(fi.tell())

'''
fi=open('sg.txt','r',encoding='utf-8')
print(fi.tell())
txt=fi.readlines()
print(fi.tell())
fi.seek(0, 0)
print(fi.tell())


a.append(fi.read(1))
print(fi.tell())
a.append(fi.read(2))
print(fi.tell())
a.append(fi.read(3))
print(fi.tell())
print(a)

for i in range(3):
    a.append(fi.readline())
    print(a)
    print(fi.tell())
'''
