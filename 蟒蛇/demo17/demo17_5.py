def jia(n):
    if n==1:
        return 1
    else:
        return jia(n-1)+1/(2*n-1)

print("{:.4f}".format(jia(6)))
