def num(n):
    if n==1:
        return 1
    else:
        if n%2:
            k=1/(2*n-1)
        else:
            k=1/(1-2*n)
        return num(n-1)+k


print("{:.4f}".format(num(7)))
