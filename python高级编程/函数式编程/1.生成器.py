#coding=gbk
import time
# 1
lst1=[1,2,3,4,5,6,7,8,9]
# 2
lst2=[x for x in range(1,10)]

# ������:һ�����󣬱����˲���Ԫ�ص��㷨��ͬʱ���¼�α��λ��
# ����������: 1.ͨ���б�������������
#           2.ͨ������������������(yield)
# �����������е�Ԫ������:
#        1.ͨ��next(g),����������û�����ݵ�ʱ���׳��쳣:StopIteration
#        2.ͨ��forѭ������
#        3.object���õ�__next__,����������û�����ݵ�ʱ���׳��쳣:StopIteration
#        4.send�������������ĵ�һ��ֵ����ʹ��send(None),�����ֵ������


# 1.ͨ���б�������������
g=(x for x in range(1,10))
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# time.sleep(5)
# print(next(g))
# print(next(g))

next(g)
for i in g:
    print(i,"-----")

g2=(x for x in range(1,10) if x%2==0)
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))

print("_____________________________________________________")
def test1(times):
    a,b=0,1
    n= 0
    while n<times:  # yieldһ�����ڴ���������:�������غ���ı���ֵ��������
        yield b  # print(b)  # bΪ쳲����������е�һ��Ԫ��
        a, b = b, (a+b)
        n += 1

g3=test1(6)
for i in g3:
    print(i)

print("_____________________________________________________")
def test2():
    a,b=0,1
    while b<10000:  # yieldһ�����ڴ���������:�������غ���ı���ֵ��������
        yield b  # print(b)  # bΪ쳲����������е�һ��Ԫ��
        a, b = b, (a+b)

g4=test2() # g4�������10000�������е�쳲���������
for i in g4:
    print(i)

# next=__next__
print("______________________________________________________")
# print(g4.send(None))
