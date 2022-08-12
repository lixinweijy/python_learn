# 千年虫问题
year=[82,89,88,86,85,00,99]
print('原列表:',year)
for index,value in enumerate(year):#enumerate将所在位置上的索引与值一一对应
    if str(value)!='0':
        year[index]=int('19'+str(value))
    else:
        year[index]=int('200'+str(value))

print('修改之后的列表',year)
year.sort()
print('排序之后的列表为',year)