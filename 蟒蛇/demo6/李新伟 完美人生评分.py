def grow():
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
    return p
    
def talents():
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
    return p

def points():
    def point(m,e,t):
        m_1=3.5*(m/10-5)
        e_1=3*(e/10-5)
        t_1=2.5*(t/10-5)
        averge_point=(m_1+e_1+t_1)/(3.5+3+2.5)
        return averge_point

    m=eval(input('请输入你的数学成绩\n'))
    e=eval(input('请输入你的英语成绩\n'))
    t=eval(input('请输入你的计算机导论成绩\n'))
    if m>90:
        m=90
    if e>90:
        e=90
    if t>90:
        t=90
    p=point(m,e,t)
    print('你的绩点为{:.1f}'.format(p))
    return p

def perfect():
    a=points()
    b=talents()
    c=grow()
    score=(a*20+b+c)/3
    print('你的完美人生得分为{:.1f}'.format(score))
start=input('准备上车，按n退出\n')
while (start!='n'):
    perfect()
    start=input('再来一次，按n退出\n')
print('over')
