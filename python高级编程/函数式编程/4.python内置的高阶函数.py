# coding=gbk
# 1.map:��һ���ɵ��������е�ÿ��Ԫ��ת����һ���µĶ�����󷵻�һ���µĿɵ�������
list1=[1,2,3,4,5,6]
it1 = map(lambda x:x**2,list1)
print(list(it1))

# 2.reduce:��һ���ɵ���������ÿ��Ԫ�����ۺϴ�����󷵻�һ���ۺϵ�ֵ
from functools import reduce

a=reduce(lambda x,y:x+y,list1)
print(a)

# �������ֵ
def getMax(x,y):
    if x>y:
        return x
    else:
        return y

print(reduce(getMax,list1))
# 3.filter��һ���ɵ��������е�Ԫ�������˲��������func����ֵΪTrue�����£�������˵�

emps=[
    {"name":"zhangshan","age":18,"salary":3000},
    {"name":"lisi","age":28,"salary":6000},
    {"name":"wangwu","age":38,"salary":9000}
]

# ���󣬹������´���18��õ�Ա��������һ��������
print(list(filter(lambda x:x["age"]>18,emps)))

# 4.max��min
# ����н�����
print(max(emps,key=lambda x:x["salary"]))
# ����н�����
print(min(emps,key=lambda x:x["salary"]))

# 5.sorted ��һ���ɵ������������ÿ��Ԫ�����򣬷���һ���б�
print(sorted(emps,key=lambda x:x["age"],reverse=True))


