# -*- coding:utf-8 -*-
from flask import Blueprint,current_app,g
import db_handler
item_bp = Blueprint('item',__name__)

@item_bp.route("/get")
def hello_item():
    print(current_app.laoxiao)
    g.item_id = '123'
    g.item_name = 'abc'
    db_handler.find_items()
    return "产品模块的页面"