a=input('支付宝支付密码:')
if a.isdecimal():
    print('支付数字合法')
else:
    print('支付数字不合法，支付密码只能是数字！')

print('---------------------------------')
print('支付数字合法' if a.isdecimal() else'支付数字不合法，支付密码只能是数字！')