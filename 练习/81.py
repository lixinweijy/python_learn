# -*- coding:utf-8 -*-
for i in range(1,10):
    print(('*' * (2 * i - 1)).center(9)) if i<=5 else print(('*'*(2*(9-i)-1)).center(9))