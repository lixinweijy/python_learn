sumtime = 0
percls = []
ts = {}
with open('out.txt', 'r') as f:                         # with打开不用关闭
    for line in f:                                      # f的元素分界为一行
        percls.append(line.strip('\n').split(","))      # strip去空去字符，split字符串切片
# print(percls)

n=[x[1] for x in percls]                                # 遍历元素
# print(n)
for i in range(len(n)):
    sumtime+=eval(n[i])

ts={x[0]:x[2] for x in percls}                          # 不是添加元素，是重新赋值
# print(ts)
print('the total execute time is ', sumtime)

tns = list(ts.items())                                  # 将字典列表化，生成列表元素为元组类型
# print(tns)
tns.sort(key=lambda x: x[1], reverse=True)              # 只有列表才可使用sort函数,匿名函数lambda
# print(tns)
for i in range(3):
    print('the top {} percentage time is {}, spent in "{}" operation'.format(i, tns[i][1],tns[i][0]))
