# -*- coding:utf-8 -*-
db=[[],[45]]
z=[]
for i in range(len(db)):
    print(i)
    if bool(db[i])==False:
        z.append(i-len(z))
for i in z:
    db.pop(i)

print(db)