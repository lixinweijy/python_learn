#coding=gbk
import random as r
x=r.randint(1,99)
print(x)
b=0
c=0
flag=0
a=input('�������һ��1~99�����֣�������²�~(���س��˳�)\n')
while(a!=''):
    for i in a:
        if(i!='0'and i!='1'and i!='2'and i!='3'and i!='4'and i!='5'and i!='6'and i!='7'and i!='8'and i!='9'):
            c+=1
    if(c==0):
        # a = eval(a)
        while(b<8):
            b+=1
            try:
                a=eval(a)
            except:
                break
            if(x==a):
                flag=1
                break
            elif(a<1 or a>99):
                print('������Χ��Ӵ~')
                a=input('�����������~(���س��˳�)\n')
            elif(x>a):
                print('���С��')
                a=input('�����²�~(���س��˳�)\n')
            elif(x<a):
                print('�´���Ӵ')
                a=input('�����²�~(���س��˳�)\n')
        if flag!=1:
            try:
                a = eval(a)
            except:
                continue
        if(b<5):
            print('�����{}�ξͲ�����'.format(b))
            print('��������ţ�')
        elif(b<7):
            print('�����{}�ξͲ�����'.format(b))
            print('��̫�����ˣ�')
        elif(b<8):
            print('�����{}�ξͲ�����'.format(b))
            print('������Ŷ~')
        elif(b==8):
            print('��������Ŷ~')
    else:
        print('���������Ӧ�����봿���֡�')
        a=input('�����²�~(���س��˳�)\n')
        c=0
        continue
    c=0
    x=r.randint(1,99)
    print()
    print(x)
    a=input('���������һ��1~99�����֣��ٲ�һ�°�~(���س��˳�)\n')
    b=0
