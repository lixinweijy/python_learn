# -*- coding:utf-8 -*-
from flask import Blueprint

#创建蓝图
order_bp=Blueprint("order",__name__,static_folder='html',template_folder='temp')

from . import order_func