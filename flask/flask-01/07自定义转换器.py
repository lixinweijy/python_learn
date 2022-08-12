# -*- coding:utf-8 -*-
from flask import Flask,url_for,redirect
from werkzeug.routing import BaseConverter

"""我们自定义的转换器必须要继承当前的BaseConverter父类"""
class MobieConverter(BaseConverter):
    """
    定义一个匹配手机号码的正则表达式,注意：regex的名字不能改变
    """
    regex=r'1[3-9]\d{9}'


app=Flask(__name__,static_url_path='/lxw',static_folder='static')# 初始化Flask项目的服务

#讲自定义的转换器添加到转换器的列表中
app.url_map.converters['phone']=MobieConverter  #phone是转换器对的名字


@app.route('/')
def hello_world():
    # print(url_for('phone_number',mob_num='13177003506',page=2))
    return redirect(url_for('phone_number',mob_num='13177003506',page=2))


@app.route('/phone/<phone:mob_num>')
def phone_number(mob_num):
    return "当前你访问的手机号码是:{}".format(mob_num)


if __name__ == '__main__':
    #0.0.0.0代表当前系统中所有的ip地址,端口号默认5000,flask的debug模式：把错误的信息显示到网页中
    app.run(host='0.0.0.0',port=8080,debug=False)
