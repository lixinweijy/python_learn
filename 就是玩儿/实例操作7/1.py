a=['白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座','摩羯座','水瓶座','双鱼座']
b=['活力充沛','浪漫美好','思维敏捷','意志顽强','文思敏捷','细心执着','理想主义','神秘独立','优越理性','优越聪慧','宽容冷静','自觉唯美']
c={a:b for a,b in zip(a,b)}
l=input('请输入你的星座:')
# print(l+'的性格特点是:'+c.get(l))
flag=True
for i in c:
    if i==l:
        flag=True
        print(l+'的性格特点为:'+c.get(l))
        break
    else:
        flag=False
        break
if not flag:
    print('对不起，您的输入有误')