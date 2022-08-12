b=open('D:/key.txt','a')
print('helloworld',file=b)
b.close()
# a 附加方式打开，不可读  a+ 附加方式读写打开，可读可写  创建
# w新建只写，w+新建读写，二者都会将文件内容清零
# r只读，r+读写，不创建
fd = open("1.txt",'w+')

fd.write('123')

fd = open("1.txt",'r+')

fd.write('456')

fd = open("1.txt",'a+')

fd.write('789')

fd=open("1.txt",'w+') #w、w+、r、r+为覆盖，a、a+为附加

fd.write('123456')
fd.read()

print('我懂啦！！！！！！')