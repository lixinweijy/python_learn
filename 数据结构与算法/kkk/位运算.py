#coding=gbk
def num(i):
    a=0
    for b in range(32):
        if (i>>b&1)==1:
            a+=1
    print(a,end="\t")

a=int(input(""))
b=list(i for i in range(1,a+1))

def start():
    for i in b:
        num(i)
start()