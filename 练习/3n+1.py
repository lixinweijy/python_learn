#coding=gbk
a=int(input("��������1000���ڵ���\n"))
flag=0
while(a!=1):
    if a%2==0:
        a/=2
    else:
        b=3*a+1
        a=b/2
    flag+=1
print("��{}��".format(flag))
