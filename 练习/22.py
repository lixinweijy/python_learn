#coding=gbk
select=input("请选择你需要解密还是需要加密\n[a]加密         [b]解密\n")
if select=="a":
    select=1
else:
    select=-1
char=input("请输入字母(按回车退出)\n")
pi=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3]
pi_1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
while char!="":
    flag = 1
    while flag:
        flag=0
        for i in range(len(pi)):
            for j in range(i):
                if i - j == pi[j] - pi[i] or i - j == pi[j] - pi[i]+26:
                    pi[i] += 1
                    flag+=1
    z=0
    if select != 1:
        for i in range(26):
            for j in range(26):
                if pi[j] + j == i or pi[j] + j == 26 + i:
                    pi_1[i] = pi[j]
                    break
    if select!=1:
        pi=pi_1
    for i in char:
        i=ord(i)
        if i<91:
            j=i-65
            i=i+pi[j]*select
            if i-pi[j]*select==44 or i-pi[j]*select==46:
                i=i-pi[j]*select
                print(chr(i), end="")
                continue
            if i>90:
                i=i-26
            if i<65:
                i=i+26
        else:
            j = i - 97
            i=i+pi[j]*select
            if i>122:
                i=i-26
            if i<97:
                i = i +26
        print(chr(i),end="")
    print("")
    select = input("请选择你需要解密还是需要加密\n[a]加密         [b]解密\n")
    if select == "a":
        select = 1
    else:
        select = -1
    pi = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3]
    char=input("请输入字母(按回车退出)\n")
print("加密结束")