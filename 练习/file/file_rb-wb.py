# -*- coding:utf-8 -*-
with open('0.jpg', 'rb') as r_file:
    with open('1.jpg','wb') as w_file:
        w_file.write(r_file.read())

# with open('0.jpg', 'rb') as r_file:
#     a=r_file.read()
#     print(a)