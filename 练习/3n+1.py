#coding=gbk
a=int(input("请输入移1000以内的数\n"))
flag=0
while(a!=1):
    if a%2==0:
        a/=2
    else:
        b=3*a+1
        a=b/2
    flag+=1
print("共{}步".format(flag))
