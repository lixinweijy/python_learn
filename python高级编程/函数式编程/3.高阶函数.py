# coding=gbk

# ����һ������������һ���б�[1,2,3,4,5,6,7],����һ���µ��б� [ÿ�����Ľײ�]

# �������һ�����ֵĽײ�ĺ���
def test1(num):
    if num==1:
        return 1
    else:
        return num*test1(num-1)

# �������һ�����еĽӴ��ĺ���
def test2(list,func):
    new_list=[]
    for i in list:
        new_list.append(func(i))
    return new_list

list1=[1,2,3,4,5,6,7]
print(test2(list1,test1))
