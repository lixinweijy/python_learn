s=[7,-5,3,4,-3,51,-62]
for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        if s[i]>s[j]:
            s[i],s[j]=s[j],s[i]
print(s)
