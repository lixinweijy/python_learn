def a(c,d):
    num=[]
    for i in c:
        for j in d:
            num.append(abs(i-j))
    num.sort()
    print(num)

a([1, 3, 15, 11, 2],[23, 127, 235, 19, 8])