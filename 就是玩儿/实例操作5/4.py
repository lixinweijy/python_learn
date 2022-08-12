print('计算100-999之间的水仙花数')
for item in range(100,1000):
    ge=int(item%10)
    shi=int(item//10%10)
    bai=int(item//100)
    if item==ge**3+shi**3+bai**3:
        print(item)
        item+=1
    else:
        continue

print('-----------------------')
import math
for i in range(100,1000):
    if math.pow((i%10),3)+math.pow((i//10%10),3)+math.pow((i//100),3)==i:
        print(i)