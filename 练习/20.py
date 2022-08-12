#coding=gbk
ss=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3]
def jia():
    w='' #用于累加密码
    for i in sr:#拆分口令
        a=ord(i)
        if(64<a and a<91):#大写字母
            a=a+ss[a-65]
            if (a>90):#asc码超出相应范围时减26
                a=a-26
        elif(96<a and a<123):#小写字母
            a=a+ss[a-97]
            if (a>122):#asc码超出相应范围时减26
                a=a-26
        w=w+chr(a)#累加密码
    print(w)
sr=input('请输入要加密的口令：')
jia()