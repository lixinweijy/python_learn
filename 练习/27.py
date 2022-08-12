#coding=gbk
#任务五 复杂的凯撒加解密--按3.1415926535897932384626433加解密码
s=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3]
ss=[8,4,1,3,1,3,4,3,2,5,6,2,3,6,9,5,6,4,3,8,7,9,3,9,2,5]
#（ss表是根据s表加密后得出的26个字母顺序重新建立的列表
#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#D C G E J O I N Z M P T V U X S Y W A R Q L K B H F
ask=input('请问你是想对密码进行加密还是解密？\n  A.加密  B.解密\n')
while 1:
#------------------------------------------------加密部分
    if ask=='A':
        string = input("请输入密码\n")
        for x in string:
            if(x==' '):
                print(' ',end='')
            if(64<ord(x)<73 or 73<ord(x)<81 or ord(x)==83 or ord(x)==88):
                a=ord(x)+s[ord(x)-65]           #根据圆周率（s表）进行加密
                if(a>90):
                   a=a-26
                print(chr(a),end ='')           #加密结果与其他字母有重合的字母重新赋予新的字母代替
            if(ord(x)==73):                      #大写字母I
                print (chr(ord(x)+17),end='')
            if(ord(x)==81):                      #大写字母Q
                print (chr(ord(x)+8),end='')
            if(ord(x)==82):                      #大写字母R
                print (chr(ord(x)+5),end='')
            if(ord(x)==84):                      #大写字母T
                print (chr(ord(x)-2),end='')
            if(ord(x)==85):                      #大写字母U
                print (chr(ord(x)-4),end='')
            if(ord(x)==86):                      #大写字母V
                print (chr(ord(x)-10),end='')
            if(ord(x)==87):                      #大写字母W
                print (chr(ord(x)-12),end='')
            if(ord(x)==89):                      #大写字母Y
                print (chr(ord(x)-17),end='')
            if(ord(x)==90):                      #大写字母Z
                print (chr(ord(x)-20),end='')
            if(96<ord(x)<105 or 105<ord(x)<113 or ord(x)==115 or ord(x)==120):
                b=ord(x)+s[ord(x)-97]
                if(b>122):
                   b=b-26
                print(chr(b), end='')
            if(ord(x)==105):                     #小写字母i
                print (chr(ord(x)+17),end='')
            if(ord(x)==113):                     #小写字母q
                print (chr(ord(x)+8),end='')
            if(ord(x)==114):                     #小写字母r
                print (chr(ord(x)+5),end='')
            if(ord(x)==116):                     #小写字母t
                print (chr(ord(x)-2),end='')
            if(ord(x)==117):                     #小写字母u
                print (chr(ord(x)-4),end='')
            if(ord(x)==118):                     #小写字母v
                print (chr(ord(x)-10),end='')
            if(ord(x)==119):                     #小写字母w
                print (chr(ord(x)-12),end='')
            if(ord(x)==121):                     #小写字母y
                print (chr(ord(x)-17),end='')
            if(ord(x)==122):                     #小写字母z
                print (chr(ord(x)-20),end='')
        char=input('\n是否继续输入（按n退出）\n')
        if char=='n':
            break
            print("加密结束")
        else:
            ask=input('请问你是想对密码进行加密还是解密？\n  A.加密  B.解密\n')
#---------------------------------------------------------------解密部分
    else :
        string = input("请输入字符\n")
        for x in string:
            if(x==' '):
                print(' ',end='')
            if(64<ord(x)<70 or 72<ord(x)<75 or 76<ord(x)<81 or ord(x)==71 or 82<ord(x)<87 or ord(x)==88):
                a=ord(x)-ss[ord(x)-65]         #根据ss表进行解密
                if(a<65):
                    a=a+26
                print(chr(a),end ='')          #解密结果与其他字母有重合的字母重新赋予新的字母代替
            if(ord(x)==90):                     #大写字母Z
                print (chr(ord(x)-17),end='')
            if(ord(x)==89):                     #大写字母Y
                print (chr(ord(x)-8),end='')
            if(ord(x)==87):                     #大写字母W
                print (chr(ord(x)-5),end='')
            if(ord(x)==82):                     #大写字母R
                print (chr(ord(x)+2),end='')
            if(ord(x)==81):                     #大写字母Q
                print (chr(ord(x)+4),end='')
            if(ord(x)==76):                     #大写字母L
                print (chr(ord(x)+10),end='')
            if(ord(x)==75):                     #大写字母K
                print (chr(ord(x)+12),end='')
            if(ord(x)==72):                     #大写字母H
                print (chr(ord(x)+17),end='')
            if(ord(x)==70):                     #大写字母F
                print (chr(ord(x)+20),end='')
            if(96<ord(x)<102 or 104<ord(x)<107 or 108<ord(x)<113 or ord(x)==103 or 114<ord(x)<119 or ord(x)==120):
                b=ord(x)-ss[ord(x)-97]
                if(b<97):
                    b=b+26
                print(chr(b), end='')
            if(ord(x)==122):                    #小写字母z
                print (chr(ord(x)-17),end='')
            if(ord(x)==121):                    #小写字母y
                print (chr(ord(x)-8),end='')
            if(ord(x)==119):                    #小写字母w
                print (chr(ord(x)-5),end='')
            if(ord(x)==114):                    #小写字母r
                print (chr(ord(x)+2),end='')
            if(ord(x)==113):                    #小写字母q
                print (chr(ord(x)+4),end='')
            if(ord(x)==108):                    #小写字母l
                print (chr(ord(x)+10),end='')
            if(ord(x)==107):                    #小写字母k
                print (chr(ord(x)+12),end='')
            if(ord(x)==104):                    #小写字母h
                print (chr(ord(x)+17),end='')
            if(ord(x)==102):                    #小写字母f
                print (chr(ord(x)+20),end='')
        char=input('\n是否继续输入（按n退出）\n')
        if char=='n':
            break
            print("加密结束")
        else:
            ask=input('请问你是想对密码进行加密还是解密？\n  A.加密  B.解密\n')

