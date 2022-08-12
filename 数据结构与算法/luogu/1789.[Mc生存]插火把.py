a=input("").split()
n=int(a[0])
m=int(a[1])
k=int(a[2])
z=[[0 for i in range(n)] for i in range(n)]
print(z)
for i in range(m):
    pass
def fire(i,j):
    z[i][j]+=1
    if i>1:
        z[i-1][j]+=1
        if j>1:
            z[i-1][j-1]+=1

        if i>2:
            z[i-2][j]+=1
    if j>1:
        z[i][j-1]+=1
        if j>2:
            z[i][j-2]+=1
