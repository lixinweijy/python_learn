for item in 'python':# item从python中依次取值
    print(item)
# range()产生一个整数序列——》也是一个可迭代对象
for i in range(10):
    print(i)
# 如果循环体中不需要自定义变量，可将自定义变量改为‘_‘
for _ in  range(5):# 此时5为循环次数
    print('人生苦短，我用python')
print('使用for循环计算1到100的偶数和')
'''
a=0
sum=0
while a<=100:
    sum+=a
    a+=2
print(sum)
'''
sum=0
for item in range(1,101):
    if item %2==0:
        sum+=item
print('1到一百之间的偶数和为sum:',sum)
'''
输出100到999之间的水仙花数
举例：
153=1**3+5**3+3**3
'''
for item in range(100,1000):
    ge=item%10       #个位
    shi=item//10%10  #十位
    bai=item//100    #百位
    if ge**3+shi**3+bai**3==item:
      print(item)