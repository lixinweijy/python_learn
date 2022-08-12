'''输入一个三行四列的矩形'''
for i in range(1,4):# 行数执行三次，一次一行
    for j in range(1,5):
        print('*',end='\t')# 不换行输出
    print()# 打行

for i in range(1,10):
    for j in range(1,i+1):
        print(j,'*',i,'=',i*j,end='\t')
    print()


# 流程控制语句break与continue在二重循环中的使用
for i in range(5):# 执行5次
    for j in range(1,11):
        if j%2==0:
            break
        print(j)

for i in range(5):# 执行5次
    for j in range(1,11):
        if j%2==0:
            continue
        print(j,end='\t')
    print()