# -*- coding:utf-8 -*-
from flask import Flask

app=Flask(__name__,static_url_path='/lxw',static_folder='static')# 初始化Flask项目的服务

@app.route('/')
def hello_world():
    return 'hello world!'

if __name__ == '__main__':
    #0.0.0.0代表当前系统中所有的ip地址,端口号默认5000,flask的debug模式：把错误的信息显示到网页中
    app.run(host='0.0.0.0',port=8080,debug=False)