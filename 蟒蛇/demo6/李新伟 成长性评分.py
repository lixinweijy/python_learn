def talent(d,b,z):
    p=(b+d+z)/3-x
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
    A=input('这位同学，你认为你的人际关系怎么样，请选择\n【a】超好  【b】好  【c】一般  【d】较差  【e】很差\n')
    d=judge(A)
    A=input('这位同学，你认为你的自我反省能力怎么样，请选择\n【a】超好  【b】好  【c】一般  【d】较差  【e】很差\n')
    b=judge(A)
    A=input('这位同学，你认为你的学习能力怎么样，请选择\n【a】超好  【b】好  【c】一般  【d】较差  【e】很差\n')
    z=judge(A)
    return d,b,z
D,B,Z=score()
x=0
if D==40:
    x+=10
elif D==20:
    x+=20

if B==40:
    x+=10
elif B==20:
    x+=20

if Z==40:
    x+=10
elif Z==20:
    x+=20
p=talent(D,B,Z)

print('你的成长性评分为{:.1f}'.format(p))
