a=8
print('手机原有话费为:\033[0;35m{0}元\033[m'.format(a))
money=int(input('请用户输入充值金额:'))
print('当前可用余额为:\033[0;35m{0}元\033[m'.format(a+money))