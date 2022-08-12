s=[7,-5,3,4,-3]
for i in range(1,5):
    if s[0]>s[i]:
        s[0],s[i]=s[i],s[0]
print(s)
