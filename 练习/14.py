#coding=gbk
import random as r
x=r.randint(1,99)
print(x)
b=0
def hhh():
        while(1):
            try:
                global a
                a = eval(a)
                break
            except:
                print('�������Ӧ������1~99�Ĵ�����')
                a = input('������һ�ΰ�~\n')
                continue
a=0
while(a!=""):
        while(b<9):
            if b==0:
                a = input('�������һ��1~99���������������~(���س��˳�)\n')
            else:
                a=input()
            hhh()
            b+=1
            print("��������{}��".format(b))
            if(x==a):
                break
            elif(a<1 or a>99):
                print('������Χ����������һ��1~99������')
            elif(x>a):
                print('���С��')
            elif(x<a):
                print('�´���Ӵ')

        if(x==a):
                print('��¶���~')
        if(b<6):
            print('�����{}�ξͲ�����'.format(b))
            print('��������ţ�\n')
        elif(b<7):
            print('�����{}�ξͲ�����'.format(b))
            print('��̫�����ˣ�\n')
        elif(b<9):
            print('�����{}�ξͲ�����'.format(b))
            print('������Ŷ~\n')
        elif(b==9):
            print('��������Ŷ~\n')
        b=0
        x=r.randint(1,99)
        print(x)