# -*- coding:utf-8 -*-
# file=open('c.txt', 'w+')
# file.write('python\nhhhhh sadas\n dasa')
# a=file.read()
# print(a)
# file.close()


file=open('c.txt', 'r+')
file.write('pyn\n')
file.writelines(['121','wqqd'])
file.close()

file=open('c.txt', 'r+')
b=file.read()
print(b)
file.close()

# file=open('c.txt', 'w+')
# file.write('python\nhhhhh sadas\n dasa')
# file.flush()
# file.close()
