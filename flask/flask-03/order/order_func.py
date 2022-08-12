# -*- coding:utf-8 -*-
from . import order_bp  #从当前目录里面导入

@order_bp.route('/co')
def create_order():
    return "create order"