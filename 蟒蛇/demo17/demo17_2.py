def tao(a):
    if a==10:
        return 1
    else:
        return (tao(a+1)+1)*2

print(tao(1))
