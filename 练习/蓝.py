a=int(input())
sum=0
for i in range(1,a+1):
    b=str(i)
    if str(0) in b or str(1) in b or str(2) in b or str(9) in b:
        sum+=i
        i+=1
print(sum)