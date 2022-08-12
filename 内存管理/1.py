# -*- coding:utf-8 -*-
import sys
a,b=1,2
c=3
g=5
d="李"
e="新"
f="伟"
print(sys.getsizeof(d),sys.getsizeof(a))
print(id(a)-id(b),id(b)-id(c),id(c)-id(g),id(d)-id(e),id(e)-id(f))

k=444
kk=444
print(id(k)-id(kk))