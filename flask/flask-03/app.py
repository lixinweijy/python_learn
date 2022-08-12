# -*- coding:utf-8 -*-
from flask import Flask

app=Flask(__name__)

#注册一个蓝图
from users import *
app.register_blueprint(user_bp,url_prefix='/users')  #前缀为/users

#再注册一个新的蓝图
from order import *
app.register_blueprint(order_bp)  #可以省略前缀

@app.route('/')
def hello_world():
    return 'Hello world!'

if __name__ == '__main__':
    app.run()
