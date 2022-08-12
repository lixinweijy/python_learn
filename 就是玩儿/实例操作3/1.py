def fun():
    print('十进制转二进制')  # bin用来十进制转二进制
    num = int(input('请输入一个十进制整数:'))
    print(num, '转化为二进制为:', bin(num))
    print('{0}转化为二进制为:{1}'.format(num, bin(num)))
    print(f'{num}转化为二进制为:{bin(num)}')
    print('%s转化为二进制为:%s' % (num, bin(num)))
    print(str(num) + '转化为二进制为:' + bin(num))

    print('十进制转八进制')  # oct
    print(f'{num}转化为八进制为:{oct(num)}')

    print('十进制转十六进制')  # hex
    print(f'{num}转化为十六进制为:{hex(num)}')

    print('二进制转十进制')
    print(int(bin(num), 2))

    print('八进制转十进制')
    print(int(oct(num), 8))

    print('十六进制转十进制')
    print(int(hex(num), 16))

if __name__ == '__main__':
    while True:
        try:
            fun()
            break
        except:
            print('只能输入整数!程序出错，请重新输入')