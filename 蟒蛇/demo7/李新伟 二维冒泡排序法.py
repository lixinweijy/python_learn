#冒泡排序法
ss=[[7,5,8,-5,-7],[2,8,-1,4,7],[1,4,-5,-8,10]]
for m in range(len(ss)):
    for j in range(len(ss[m])-1):
        for i in range(len(ss[m])-1):
            if ss[m][i]>ss[m][i+1]:
                ss[m][i],ss[m][i+1]=ss[m][i+1],ss[m][i]

print(ss)
