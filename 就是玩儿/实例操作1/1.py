# 使用print方式进行输出（目的地是文件）
a=open('lalala.txt', 'a+', encoding='utf-8')
print('奋斗成就更好的你',file=a)
a.close()

# 第二种方式，使用文件读写操作
with open('hhh.txt', 'w', encoding='utf-8') as file:
    file.write('奋斗成就更好的你')

