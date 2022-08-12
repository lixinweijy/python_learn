# -*- coding:utf-8 -*-
from flask import Flask

#Web项目的常量配置对象
class DefaultConfig(object):
    """默认Web项目的配置"""
    USER="laoxiao"
    PWD="123123"

app=Flask(__name__)

app.config.from_object(DefaultConfig)

@app.route('/')
def index():
    print(app.config["USER"])
    print(app.config["PWD"])
    return "Hello World"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)