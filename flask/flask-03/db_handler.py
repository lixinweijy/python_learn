# -*- coding:utf-8 -*-
from flask import g

def find_items():
    print('从数据库中查询数据的，通过多个不确定的条件')
    print(g.item_id)
    print(g.item_name)