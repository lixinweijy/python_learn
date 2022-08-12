#coding=gbk
a=int(input("请输入第一个数\n"))
b=int(input("请输入第二个数\n"))

while(a%b):
    r=a%b
    a=b
    b=r
if b!=1:
    print(f"{b}为最大公因数")
else:
    print('没有最大公因数')