def talent(d,b,z):
    p=(b+d+z)/3
    return p
def judge(x):
    if x=='a':
        return 100
    elif x=='b':
        return 80
    elif x=='c':
        return 60
    elif x=='d':
        return 40
    elif x=='e':
        return 20

def score():
    A=input('这位同学，你认为你的电脑基础怎么样，请选择\n【a】超好  【b】好  【c】一般  【d】较差  【e】很差\n')
    d=judge(A)
    A=input('这位同学，你认为你的编程能力怎么样，请选择\n【a】超好  【b】好  【c】一般  【d】较差  【e】很差\n')
    b=judge(A)
    A=input('这位同学，你认为你的自学能力怎么样，请选择\n【a】超好  【b】好  【c】一般  【d】较差  【e】很差\n')
    z=judge(A)
    return d,b,z
D,B,Z=score()
p=talent(D,B,Z)
print('你的专业能力评分为{:.1f}'.format(p))

