# coding=gbk
# �ɵ�������:������forѭ�������Ķ���  Iterable
# ����isinstance()�ж�һ�������Ƿ�ΪIterable����
from collections.abc import Iterable
from collections.abc import Iterator

a=(1,)
b=[1,2]
c={}

def test1(arg):
    if isinstance(arg,Iterable):
        print("arg�����ǿɵ�������")
    else:
        print("arg�����ǿɵ�������")

test1(b)

# ������:Iterator
# ���Ա�next()�������ò����Ϸ�����һ��ֵ�Ķ����Ϊ������
def test2(arg):
    if isinstance(arg,Iterator):
        print("arg�����ǵ�����")
    else:
        print("arg�����ǵ�����")

test2(b)
# Ŀǰѧ����ֻ���������ǵ�����
test2(a for a in range(5))

# ��list,dict,str��ɵ�����
test2(iter(a)) #��iter����
