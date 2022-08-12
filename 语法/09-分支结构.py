# 单分支结构
money=1000 # 余额
s=int(input('请输入取款金额')) # 取款余额
# 判断金额是否充足
if money>=s:
    money=money-s
    print('取款成功，800余额为：',money)


# 双分支结构
# 从键盘输入一个数，计算机判断是奇数还是偶数
print('判断奇偶')
num=int(input('请输入一个整数'))
if num%2==0:
    print(num,'是偶数')
else:
    print(num,'是奇数')


# 多分支结构
'''
从键盘录入一个整数成绩
90-100  A
80-89   B
70-79   C
60-69   D
0-59    E
大于100或小于0为非法数据
'''
print('----------lxw期末成绩----------')
score=int(input('输入一个数据'))
if  score>=90 and score<=100:
    print('A级')
elif score>=80 and score<=89:
    print('B级')
elif score>=70 and score<=79:
    print('C级')
elif score>=60 and score<=69:
    print('D级')
elif score<=59 and score>=0:
    print('E级')
else:
    print('对不起，成绩不在有效范围')

# 镶嵌if的使用
'''
会员  >=200  8折
     >=100  9折
     否则不打折
非会员 >=200  9.5折
      否则不打折
'''
answer=input('您是会员吗？yes/no')
money=float(input('请输入您的购物金额：'))
# 判断是否为会员
if  answer=='yes':# 会员
    if money>=200:
        print('打八折，付款金额为：',money*0.8)
    elif money>=100:
        print('打九折，付款金额为',money*0.9)
    else:
        print('不打折，付款金额为',money)
else:#非会员
    if money>=200:
        print('打九点五折，付款金额为：',money*9.5)
    else:
        print('不打折，付款金额为：',money)

# ok
