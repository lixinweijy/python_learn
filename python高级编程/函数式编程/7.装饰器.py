#coding=gbk

def test1(func):  # Ҫ��:���Ĳ����Ǹú���������ֵΪһ������
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
print(eat.__name__) # test1