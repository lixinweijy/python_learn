# coding=gbk
a = input('��������ķ�����������س���n��N���˳���\n')

while (a != '' and a != 'n' and a != 'N'):
    for i in a:
        if i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9':
            b = 1
        else:
            b = 0

    if b==0:
        print('�����������һ��')
        a = input('��������ķ�����������س���n��N���˳���\n')

    else:
        c = eval(a)
        if c == 100:
            print('����')
        elif c >= 90:
            print('����')
        elif c >= 80:
            print('����')
        elif c >= 70:
            print('�е�')
        elif c >= 60:
            print('����')
        else:
            print('������')
        a = input('��������ķ���:������س�����n/N�������룩\n')



