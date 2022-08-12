score=input('请输入你的分数:\n')
while (score!=''and score!='n' and score!='N'):
    a=eval(score)
    if a==100:
        print('满分')
    elif a>=90:
         print('优秀')
    elif a>=80:
         print('良好')
    elif a>=70:
         print('中等')
    elif a>=60:
         print('及格')
    else:
        print('不及格')
    score=input('请输入你的分数:（输入回车或者n/N结束输入）\n')
print('结束')
