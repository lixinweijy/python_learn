#coding=gbk
print('��ӭ����python��½���������ʼ�����ó̰�')
name=input('����������:')
print('�ۣ������������')
def sex_option():
    try:
        sex=input('��ѡ�������ձ����Ϊ��������f�����ΪŮ������m������������������\n')
    except:
        print('�밴��Ҫ������Ŷ')
        sex_option()
    if sex=='f':
        print('��ӭ׳ʿ��')
    elif sex=='m':
        print('��ӭŮ����')
    else:
        print('���������Ǹ�����')

def age_option():
    try:
        age = int(input('��֪��������\n'))
        if 0 <= age <= 18:
            print('��������������Ϊ')
        elif 40 >= age > 18:
            print('������������ĺ�ʱ��')
        elif 80 >= age > 40:
            print('�Ͻ�����')
        else:
            print('���䲻��Ŷ������������')
            age_option()
    except:
        print('�����ʽ��������һ�ΰ�')
        age_option()

def willing_option():
    print('ǰ����ׯ�е��ˣ�����Ը��������������������')
    option = input('��A���ᱲ֮��       ��B���´�һ��\n')
    if option == 'A':
        print('��л������')
        wuqi_option()
    elif option == 'B':
        print('��Ҫ��������\n��������ˣ�������ǰ�')
        beg_option()

    else:
        print('������������һ��')
        willing_option()

def wuqi_option():
    wuqi = input('������ѡ������������\n��A��С�����    ��B���������µ�\n')
    if wuqi == 'A':
        print('��������С��ɵ�������˰ɣ�')
    elif wuqi == 'B':
        print('�������������µ�նɱ���˰ɣ�')
    else:
        print('Ҫ����A����BŶ')
        wuqi_option()

def beg_option():
    beg=input('��A������̫�����ˣ��Ұ����ǰ�    ��B�������ˣ��ݰ�\n')
    if beg=='A':
        print('лл����')
        wuqi_option()
    elif beg=='B':
        print('��ú��ģ�')
    else:
        print('��������ȷŶ')
        beg_option()

sex_option()
age_option()
willing_option()