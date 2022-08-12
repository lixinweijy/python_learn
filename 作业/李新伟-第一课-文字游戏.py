#coding=gbk
print('欢迎来到python大陆，请大侠开始您的旅程吧')
name=input('您的姓名是:')
print('哇，真霸气的名字')
def sex_option():
    try:
        sex=input('请选择您的姓别：如果为男请输入f，如果为女请输入m，如果保密则随便输入\n')
    except:
        print('请按照要求输入哦')
        sex_option()
    if sex=='f':
        print('欢迎壮士！')
    elif sex=='m':
        print('欢迎女侠！')
    else:
        print('大侠还真是高冷呢')

def age_option():
    try:
        age = int(input('不知大侠年龄\n'))
        if 0 <= age <= 18:
            print('大侠真是年少有为')
        elif 40 >= age > 18:
            print('真是行侠仗义的好时间')
        elif 80 >= age > 40:
            print('老江湖啊')
        else:
            print('年龄不对哦，请重新输入')
            age_option()
    except:
        print('输入格式有误，再来一次吧')
        age_option()

def willing_option():
    print('前方村庄有盗匪，大侠愿意加入行侠仗义的行列吗')
    option = input('【A】吾辈之责       【B】下次一定\n')
    if option == 'A':
        print('感谢大侠！')
        wuqi_option()
    elif option == 'B':
        print('不要这样啊！\n求求大侠了，帮帮我们吧')
        beg_option()

    else:
        print('输入有误，再来一次')
        willing_option()

def wuqi_option():
    wuqi = input('下面请选择您的武器吧\n【A】小李飞镖    【B】青龙偃月刀\n')
    if wuqi == 'A':
        print('大侠带着小李飞刀消灭盗匪吧！')
    elif wuqi == 'B':
        print('大侠用青龙偃月刀斩杀盗匪吧！')
    else:
        print('要输入A或者B哦')
        wuqi_option()

def beg_option():
    beg=input('【A】你们太可怜了，我帮你们吧    【B】我走了，拜拜\n')
    if beg=='A':
        print('谢谢大侠')
        wuqi_option()
    elif beg=='B':
        print('你好狠心！')
    else:
        print('请输入正确哦')
        beg_option()

sex_option()
age_option()
willing_option()