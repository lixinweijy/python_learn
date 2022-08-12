a=input('请输入用户名:')
b=input('请输入密码:')
if a=='lxw' and b=='1211':
    print('登录成功')
else:
    print('用户名或密码不正确')
    print('您还有2次机会！！！')
    a = input('请输入用户名:')
    b = input('请输入密码:')
    if a == 'lxw' and b == '1211':
        print('登录成功')
    else:
        print('用户名或密码不正确')
        print('您还有1次机会！！！')
        a = input('请输入用户名:')
        b = input('请输入密码:')
        if a == 'lxw' and b == '1211':
            print('登录成功')
        else:
            print('用户名或密码不正确')
            print('对不起，三次均输入错误，请联系后台管理员')

print('-------------------------------')
for i in range(1,4):
    name=input('请输入用户名')
    pwd=input('请输入密码')
    if name=='lxw' and pwd=='1211':
        print('登录成功')
    else:
        print('用户名或密码不正确！！！')
        if i<3:
            print('您还有{0}次机会'.format(3-i))
        else:
            print('对不起，三次均输入错误，请联系后台管理员')