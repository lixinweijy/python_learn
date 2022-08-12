def point(m,e,t):
    m_1=3.5*(m/10-5)
    e_1=3*(e/10-5)
    t_1=2.5*(t/10-5)
    averge_point=(m_1+e_1+t_1)/(3.5+3+2.5)
    return averge_point

start=input('准备上车，如果退出请按n\n')
while (start!='n'):
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
    start=input('再来一次，如果退出请按n\n')
