# coding=gbk
def get_sum(*args):
    def tt():  # ���庯��
        s=0
        for n in args:
            s+=n
        return s
    return tt()  #���غ���
f1=get_sum(1,2,3,4,5,6)
print(f1)

print("______________________________________________")
# ����: �õ�����С��100����������
# 1����С��2
# 2����2������ż������������
# 3��˼·:�ȵõ����д���1������ ����������������,�ٰ��������е�����Ԫ�ع��ˣ�ȥ�����Ա�С��Ԫ�ر�ʡ������������

def odd_num(): #�õ����д���1��������������
    n=1
    while True:
        n+=2
        yield n  #nΪ����1����������

g1=odd_num()

def my_filter(n): # �ж��Ƿ��ܹ������ĺ���,n��������������õ���һ������
    return lambda  x:x%n>0 # xΪһ��������nΪС�ڵ�ǰx��һ������

# ����һ������������������С��������2
def zhishu():
    yield 2
    g=odd_num() #�õ����д���1������
    while True:
        x=next(g) #�����������õ�һ������
        g=filter(my_filter(x),g) # ����֮���ڸ�ֵ��g
        yield x

for n in zhishu():
    if n <100:
        print(n)
    else:
        break