a=int(input(""))
b=input().split()
flag=0
for i in range(len(b)-1):
    for j in range(len(b)-1):
        if int(b[j])>int(b[j+1]):
            b[j+1],b[j]=b[j],b[j+1]
            flag+=1
print(flag)