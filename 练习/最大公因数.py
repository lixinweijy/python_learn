#coding=gbk
a=int(input("�������һ����\n"))
b=int(input("������ڶ�����\n"))

while(a%b):
    r=a%b
    a=b
    b=r
if b!=1:
    print(f"{b}Ϊ�������")
else:
    print('û���������')