#coding=gbk
#������ ���ӵĿ����ӽ���--��3.1415926535897932384626433�ӽ�����
s=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3]
ss=[8,4,1,3,1,3,4,3,2,5,6,2,3,6,9,5,6,4,3,8,7,9,3,9,2,5]
#��ss���Ǹ���s����ܺ�ó���26����ĸ˳�����½������б�
#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#D C G E J O I N Z M P T V U X S Y W A R Q L K B H F
ask=input('�����������������м��ܻ��ǽ��ܣ�\n  A.����  B.����\n')
while 1:
#------------------------------------------------���ܲ���
    if ask=='A':
        string = input("����������\n")
        for x in string:
            if(x==' '):
                print(' ',end='')
            if(64<ord(x)<73 or 73<ord(x)<81 or ord(x)==83 or ord(x)==88):
                a=ord(x)+s[ord(x)-65]           #����Բ���ʣ�s�����м���
                if(a>90):
                   a=a-26
                print(chr(a),end ='')           #���ܽ����������ĸ���غϵ���ĸ���¸����µ���ĸ����
            if(ord(x)==73):                      #��д��ĸI
                print (chr(ord(x)+17),end='')
            if(ord(x)==81):                      #��д��ĸQ
                print (chr(ord(x)+8),end='')
            if(ord(x)==82):                      #��д��ĸR
                print (chr(ord(x)+5),end='')
            if(ord(x)==84):                      #��д��ĸT
                print (chr(ord(x)-2),end='')
            if(ord(x)==85):                      #��д��ĸU
                print (chr(ord(x)-4),end='')
            if(ord(x)==86):                      #��д��ĸV
                print (chr(ord(x)-10),end='')
            if(ord(x)==87):                      #��д��ĸW
                print (chr(ord(x)-12),end='')
            if(ord(x)==89):                      #��д��ĸY
                print (chr(ord(x)-17),end='')
            if(ord(x)==90):                      #��д��ĸZ
                print (chr(ord(x)-20),end='')
            if(96<ord(x)<105 or 105<ord(x)<113 or ord(x)==115 or ord(x)==120):
                b=ord(x)+s[ord(x)-97]
                if(b>122):
                   b=b-26
                print(chr(b), end='')
            if(ord(x)==105):                     #Сд��ĸi
                print (chr(ord(x)+17),end='')
            if(ord(x)==113):                     #Сд��ĸq
                print (chr(ord(x)+8),end='')
            if(ord(x)==114):                     #Сд��ĸr
                print (chr(ord(x)+5),end='')
            if(ord(x)==116):                     #Сд��ĸt
                print (chr(ord(x)-2),end='')
            if(ord(x)==117):                     #Сд��ĸu
                print (chr(ord(x)-4),end='')
            if(ord(x)==118):                     #Сд��ĸv
                print (chr(ord(x)-10),end='')
            if(ord(x)==119):                     #Сд��ĸw
                print (chr(ord(x)-12),end='')
            if(ord(x)==121):                     #Сд��ĸy
                print (chr(ord(x)-17),end='')
            if(ord(x)==122):                     #Сд��ĸz
                print (chr(ord(x)-20),end='')
        char=input('\n�Ƿ�������루��n�˳���\n')
        if char=='n':
            break
            print("���ܽ���")
        else:
            ask=input('�����������������м��ܻ��ǽ��ܣ�\n  A.����  B.����\n')
#---------------------------------------------------------------���ܲ���
    else :
        string = input("�������ַ�\n")
        for x in string:
            if(x==' '):
                print(' ',end='')
            if(64<ord(x)<70 or 72<ord(x)<75 or 76<ord(x)<81 or ord(x)==71 or 82<ord(x)<87 or ord(x)==88):
                a=ord(x)-ss[ord(x)-65]         #����ss����н���
                if(a<65):
                    a=a+26
                print(chr(a),end ='')          #���ܽ����������ĸ���غϵ���ĸ���¸����µ���ĸ����
            if(ord(x)==90):                     #��д��ĸZ
                print (chr(ord(x)-17),end='')
            if(ord(x)==89):                     #��д��ĸY
                print (chr(ord(x)-8),end='')
            if(ord(x)==87):                     #��д��ĸW
                print (chr(ord(x)-5),end='')
            if(ord(x)==82):                     #��д��ĸR
                print (chr(ord(x)+2),end='')
            if(ord(x)==81):                     #��д��ĸQ
                print (chr(ord(x)+4),end='')
            if(ord(x)==76):                     #��д��ĸL
                print (chr(ord(x)+10),end='')
            if(ord(x)==75):                     #��д��ĸK
                print (chr(ord(x)+12),end='')
            if(ord(x)==72):                     #��д��ĸH
                print (chr(ord(x)+17),end='')
            if(ord(x)==70):                     #��д��ĸF
                print (chr(ord(x)+20),end='')
            if(96<ord(x)<102 or 104<ord(x)<107 or 108<ord(x)<113 or ord(x)==103 or 114<ord(x)<119 or ord(x)==120):
                b=ord(x)-ss[ord(x)-97]
                if(b<97):
                    b=b+26
                print(chr(b), end='')
            if(ord(x)==122):                    #Сд��ĸz
                print (chr(ord(x)-17),end='')
            if(ord(x)==121):                    #Сд��ĸy
                print (chr(ord(x)-8),end='')
            if(ord(x)==119):                    #Сд��ĸw
                print (chr(ord(x)-5),end='')
            if(ord(x)==114):                    #Сд��ĸr
                print (chr(ord(x)+2),end='')
            if(ord(x)==113):                    #Сд��ĸq
                print (chr(ord(x)+4),end='')
            if(ord(x)==108):                    #Сд��ĸl
                print (chr(ord(x)+10),end='')
            if(ord(x)==107):                    #Сд��ĸk
                print (chr(ord(x)+12),end='')
            if(ord(x)==104):                    #Сд��ĸh
                print (chr(ord(x)+17),end='')
            if(ord(x)==102):                    #Сд��ĸf
                print (chr(ord(x)+20),end='')
        char=input('\n�Ƿ�������루��n�˳���\n')
        if char=='n':
            break
            print("���ܽ���")
        else:
            ask=input('�����������������м��ܻ��ǽ��ܣ�\n  A.����  B.����\n')

