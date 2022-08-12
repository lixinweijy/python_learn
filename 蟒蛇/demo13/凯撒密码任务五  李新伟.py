#coding=gbk
# 选择加密还是解密--------------------------------------------------------------
select=input("请选择你需要解密还是需要加密\n[a]加密         [b]解密\n")
if select=="a":
    select=1
else:
    select=-1
char=input("请输入字母(按回车退出)\n")    #输入字母
#初始化两个数组，用于之后数组改变-----------------------------------------------
pi=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3]
pi_1=[3,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#开始加密解密，输入字母时回车即退出---------------------------------------------
while char!="":
    #更新数组pi的值，使得不会出现输入两个字母通过加密或解密得到同一字母的情况---
    flag = 1  #创建一个flag用来控制循环进行
    while flag:
        flag=0  #初始化flag，便于判断数组pi是否更新
        for i in range(len(pi)):
            for j in range(i):
                if i +pi[i]==j+pi[j] or i +pi[i]-26==j+pi[j]:
                    pi[i] += 1
                    flag+=1

    #如果之前输入的是解密，则更新数组pi_1,使得通过解密可以得到原本的字母--------
    if select != 1:
        for i in range(len(pi)):
            for j in range(len(pi)):
                if pi[j] + j == i or pi[j] + j == 26 + i:
                    pi_1[i] = pi[j]
                    break
        #使用pi_1解密
        pi=pi_1
    #分别将每个字母进行加密或解密-----------------------------------------------
    for i in char:
        i=ord(i)
        #输入大写字母
        if i<91:
            j=i-65
            i=i+pi[j]*select
            #打印 "," 或 "." 时直接打印原值
            if i-pi[j]*select==44 or i-pi[j]*select==46:
                i=i-pi[j]*select
                print(chr(i), end="")
                continue
            #超出范围时进行调整
            if i>90:
                i=i-26
            if i<65:
                i=i+26
        #输入小写字母
        else:
            j = i - 97
            i=i+pi[j]*select
            #超出范围时进行调整
            if i>122:
                i=i-26
            if i<97:
                i = i +26
        #打印结果
        print(chr(i),end="")
    print("")
    #再次选择加密还是解密
    select = input("请选择你需要解密还是需要加密\n[a]加密         [b]解密\n")
    if select == "a":
        select = 1
    else:
        select = -1
    #重置pi
    pi = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3]
    #选择是否再来一次
    char=input("请输入字母(按回车退出)\n")
print("加密结束")
