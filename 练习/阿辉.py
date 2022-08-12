# coding=gbk
a = input('请输入你的分数（若输入回车、n、N则退出）\n')

while (a != '' and a != 'n' and a != 'N'):
    for i in a:
        if i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9':
            b = 1
        else:
            b = 0

    if b==0:
        print('输入错误，再来一次')
        a = input('请输入你的分数（若输入回车、n、N则退出）\n')

    else:
        c = eval(a)
        if c == 100:
            print('满分')
        elif c >= 90:
            print('优秀')
        elif c >= 80:
            print('良好')
        elif c >= 70:
            print('中等')
        elif c >= 60:
            print('及格')
        else:
            print('不及格')
        a = input('请输入你的分数:（输入回车或者n/N结束输入）\n')



