#coding=gbk
"""
һ��ʽ˳�����ͷ��Ԫ�ص�ַ����
�ص㣺����
����ʽ˳���: ��ͷ��Ԫ�ص�ַ�����������Ǵ�����Ԫ�ص�ַ
�ص�: ������չ
�б���Ԫ�����õķ���ʽ˳���
"""
import sys
lst=[]
init_allocated=sys.getsizeof(lst) #����һ������ռ�õ��ڴ棬���ֽ�Ϊ��λ

for i in range(1,100):
    lst.append(i)
    now_allocated=sys.getsizeof(lst)-init_allocated
    print(f'��ǰԪ�ص�����:{i},��ǰ��ռ���ڴ�:{now_allocated}  ��ǰ��������:{now_allocated//8}')