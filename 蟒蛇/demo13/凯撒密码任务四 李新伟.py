#coding=gbk
char=input("请输入字母\n")
pi=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3]
while char!="":
    char_1=""
    for i in char:
        i=ord(i)
        if i<91:
            j=i-65
            i=i+pi[j]
            if i-pi[j]==44 or i-pi[j]==46:
                i=i-pi[j]
            if i>90:
                i=i-26
        else:
            j = i - 97
            i=i+pi[j]
            if i>122:
                i=i-26
        i=chr(i)
        char_1+=i
    print(char_1)
    char=input("请输入字母(按回车退出)\n")
print("加密结束")