#  1,2,3,4组成无重复数字的三位数，共有哪几种解法，一多少种
m=0
for i in range(1,5):
    for j in range(1,5):
        for l in range(1,5):
            if i!=j!=l and i!=l :
                print(i*100+j*10+l)
                m+=1
print('共有',m,'种组合')