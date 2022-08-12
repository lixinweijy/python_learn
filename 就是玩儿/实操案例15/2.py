def find_answer(question):
    with open('replay.txt','r',encoding='utf-8') as file:
        while True:
            line=file.readline()
            if not line:#if line==''到文件末尾退出
                break
            #字符串的分割
            keyword=line.split('|')[0]
            reply=line.split('|')[1]
            if keyword in question:
                return reply
    return False
if __name__ == '__main__':
    question=input('Hi,您好，小李在此很久了，有什么烦恼和小李说吧')
    while True:
        if question=='bye':
            break
        # 开始在文件当中查找
        replay=find_answer(question)
        if not replay:  # 如果回复的是False, not False——>True
            question=input('小李不知道您在说什么，您可以问一下关于订单、物流、账户、支付等问题（退出请输入bye）')
        else:
            print(replay)
            question=input('小主，您还可以继续问一些关于订单、物流、账户、支付等问题')
    print('小主再见')
