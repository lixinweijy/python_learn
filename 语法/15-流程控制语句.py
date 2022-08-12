'''
从键盘输入密码，最多三次，如果正确就结束循环
'''
# break 结束当前循环
for item in range(3):
    pwd=input('请输入密码：')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')

a = 0
while a<3:
    pwd=input('请输入密码：')
    if pwd=='8888':
        print('密码正确')
        break # 满足则退出
    else:
        print('密码不正确')
        a +=1

# continue 结束当前循环，进入下一循环
'''
要求输出1到50之间所以5的倍数
与5的余数不为0都不是5的倍数
'''
for item in range(1,51):
    if item % 5 == 0:
        print(item)


print('---------使用continue----------')
for item in range(1,51):
    if item % 5 != 0:
        continue
    print(item)

# ok
