char=input("请输入大写字母\n")
flag=1
while flag:
    char_1=""
    for i in char:
        i=ord(i)+3
        if i>87:
            i=i-26
        i=chr(i)
        char_1+=i
    print(char_1)
    char=input("是否继续输入(按n退出)\n")
    if char=="n":
        flag=0
    else:
        char=input("请输入大写字母\n")
        
    
        
