s=[7,-5,3,4,-3,100,72,-54]
for j in range(len(s)-1):
    for i in range(len(s)-1-j):
        if s[i]>s[i+1]:
            s[i],s[i+1]=s[i+1],s[i]

print(s)
