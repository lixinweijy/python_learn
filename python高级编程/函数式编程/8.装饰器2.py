#coding=gbk
from functools import wraps

def test1(func):  # Ҫ��:���Ĳ����Ǹú���������ֵΪһ������
    @wraps(func)  #ʹ��func����װtest1
    def test2():
        print("����ѷ�����")
        func()
        print("ϴ��")
    return test2

@test1 #װ����
def eat():
    print("�����ڳԷ�")

# a=test1(eat)
# a()
# װ����: Ϊ�Ѿ����ڵĴ�����Ӷ���Ĺ���

eat()
print(eat.__name__) # eat