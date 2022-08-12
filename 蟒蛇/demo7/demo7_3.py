s=[7,-5,3,4,-3]
for i in range(4):
        if s[i]>s[i+1]:
            s[i],s[i+1]=s[i+1],s[i]

print(s)
