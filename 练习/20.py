#coding=gbk
ss=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3]
def jia():
    w='' #�����ۼ�����
    for i in sr:#��ֿ���
        a=ord(i)
        if(64<a and a<91):#��д��ĸ
            a=a+ss[a-65]
            if (a>90):#asc�볬����Ӧ��Χʱ��26
                a=a-26
        elif(96<a and a<123):#Сд��ĸ
            a=a+ss[a-97]
            if (a>122):#asc�볬����Ӧ��Χʱ��26
                a=a-26
        w=w+chr(a)#�ۼ�����
    print(w)
sr=input('������Ҫ���ܵĿ��')
jia()