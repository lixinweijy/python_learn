#coding=gbk
def func_a(number_a): # �߽׺���������һ������
    def func_b(number_b):
        print("��Ƕ����func_b�Ĳ�����:%s,�ⲿ����func_a�Ĳ�����:%s"%(number_b,number_a))
        return number_b+number_a
    return func_b
resulte=func_a(10)
print(resulte(30))
# func_b��Ϊ�հ�

# �հ������õ�����Ĳ����ǲ��ܸĵģ�Ҫ�ĵĻ���Ҫ�ڲ���ǰ�� nonlocal

def test1():
    func_list=[]
    for i in range(1,4):
        def test2(_i=i): #��i��ֵ��_i����ֹi�仯�ǵ�����ֵȫΪi=3ʱ��ֵ
            return _i**2
        func_list.append(test2)
    return func_list
f1,f2,f3=test1()
print(f1(),f2(),f3())