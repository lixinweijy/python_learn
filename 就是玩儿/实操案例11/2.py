try:
    a = int(input('请输入第一边:'))
    b = int(input('请输入第二边:'))
    c = int(input('请输入第三边:'))
    if a + b > c and a + c > b and b + c > a:
        print(f'三角形的边长为a={a},b={b},c={c}')
    elif a<0 or b<0 or c<0:
        print('边长不能为负数')
    else:
        print(f'a={a},b={b},c={c},不可以构成三角形')
except Exception as e:
    print(e)