def jiec(n):
    if n==1:
        return 1
    else:
        return jiec(n-1)*n

print(jiec(5))
