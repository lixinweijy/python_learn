# -*- coding:utf-8 -*-
class Person_property():
    # age 属性的值限制的范围是0~88
    @property  #age  属性暴露出去
    def age(self):
        return self._age

    @age.setter  # 当前age属性可以允许赋值
    def age(self,value):
        if value>=0 and value<=88:
            self._age=value
        else:
            raise ValueError("age的值必须在0~88")

    @property   #不允许赋值
    def name(self):
        self._name="张三"
        return self._name
"""
property  可以读
setter  可以写
两者都有又可以读又可以写
"""

if __name__ == '__main__':
    p=Person_property()
    p.age=100
    print(p.age)
    # p.name="lxw"   报错
