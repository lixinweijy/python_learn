#coding=gbk
import functools

print(int("111")) #Ĭ��ʮ����ת��
print(int("123",base=16)) #����16����ת��

def int_2(num,base=2):
    return int(num,base)

print(int_2('1101'))

int_2=functools.partial(int,base=8)
print(int_2('1101'))


#��һ��������ĳЩ�����̶�ס������һ���º���������º��������
