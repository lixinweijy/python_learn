# -*- coding:utf-8 -*-
from flask import Flask,Blueprint

"""
使用蓝图三步骤
1.创建一个蓝图对象
2.在这个蓝图对象上进行操作，注册路由，指定静态文件夹，注册模板过滤板
3.在应用对象上注册这个蓝图对象
"""

#创建一个蓝图
user_bp=Blueprint("user",__name__)

#在蓝图中定义一个视图函数
@user_bp.route('/say')
def sya_user():
    return 'hello lxw'