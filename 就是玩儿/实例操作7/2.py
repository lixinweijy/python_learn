dict_ticket={'G1569':['北京南-天津南','18:05','18:39','00:34'],
             'G1567':['北京南-天津南','18:15','18:49','00:34'],
             'G8917':['北京南-天津南','18:25','18:59','00:34'],
             'G203':['北京南-天津南','18:35','19:09','00:34']}
print('车次\t\t出发站-到达站\t\t出发时间\t\t到达时间\t\t历时时长')
for item in dict_ticket:
    print(item,end='   ')
    for i in dict_ticket[item]:
        print(i,end='\t\t')
    print() #换行

try:
    buy = input('请输入要购买的车次:')
    person = input('请输入乘车人，如果是多人请用逗号分隔')
    s = f'您已购买了{buy}次列车'
    s1 = dict_ticket[buy]
    print(s + ',' + s1[0] + ' ' + s1[1] + '开，请' + person + '尽快换取纸质车票。【铁路客服】')
except:
    print('您输入的车次有误')
