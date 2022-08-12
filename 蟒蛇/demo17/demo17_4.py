def fb(n):
    if n==1 or n==2:
        return 1
    else:
        return fb(n-1)+fb(n-2)

print(fb(15))
