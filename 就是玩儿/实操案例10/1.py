def calc(a,b,c):
    if c=='+':
        return add(a,b)
    elif c=='-':
         return sub(a,b)
    elif c=='*':
         return mul(a,b)
    elif c=='/':
         if b!=0:
             return div(a, b)
         else:
             return '除数不能为0'
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)

if __name__ == '__main__':
    a=int(input('请输入第一个整数:'))
    b=int(input('请输入第二个整数:'))
    c=input('请输入运算符:')
    print(calc(a,b,c))