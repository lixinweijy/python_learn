#coding=gbk
def func_a(number_a): # 高阶函数，返回一个函数
    def func_b(number_b):
        print("内嵌函数func_b的参数是:%s,外部函数func_a的参数是:%s"%(number_b,number_a))
        return number_b+number_a
    return func_b
resulte=func_a(10)
print(resulte(30))
# func_b称为闭包

# 闭包里面用的外面的参数是不能改的，要改的话需要在参数前加 nonlocal

def test1():
    func_list=[]
    for i in range(1,4):
        def test2(_i=i): #将i赋值给_i，防止i变化是调出的值全为i=3时的值
            return _i**2
        func_list.append(test2)
    return func_list
f1,f2,f3=test1()
print(f1(),f2(),f3())