#选择排序法
ss=[[7,5,8,-5,-7,87,-2,-82,90],[5,-62,-3,2,8,-1,4,7],[1,-62,-3,4,-5,-8,10]]
for i in range(len(ss)):
    for m in range(len(ss[i])-1):
        for j in range(m+1,len(ss[i])):
            if ss[i][m]>ss[i][j]:
                ss[i][m],ss[i][j]=ss[i][j],ss[i][m]
print(ss)
