# coding=gbk
import time
a=time.time()
i=1 #�ź�������������˶��Ĳ���
def tower(n,x,y): #���庯����ʾ�ƶ���ʽ
    global i  #����ȫ�ֱ��������ڽ���������
    print(f"��{i}������{n}��{x}�Ƶ�{y}��")
    i += 1  #�˶�һ��i��1


def sport(n,a,b,c):
    if n == 1:  # ��n==1ʱ��ֹ�ص�
        tower(1, a, c)
    else:
        sport(n-1,a,c,b) # ���ȣ��Ƚ�n-1�����a��ͨ��cŪ��b��
        tower(n,a,c) #�ٽ����һ��ʣ�µ�һ����a����c��
        sport(n-1,b,a,c) #�ٽ���n-1����b��ͨ��aŪ��c

c=int(input("������������:\n"))
sport(c,"A","B","C")
b=time.time()
print(f"��Ҫ{b-a}��")
