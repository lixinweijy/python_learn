# -*- coding:utf-8 -*-
import os
from flask import Flask,session
from flask.json import JSONEncoder #JSONEncoder默认不支持把自定义对象变成JSON格式
from datetime import timedelta

app=Flask(__name__)
#自定义一个JSONEncoder
class My_JSONEncoder(JSONEncoder):
    def default(self,obj):
        if isinstance(obj,User):
            return {
                'username':obj.username,
                'password':obj.password
            }
        else:  #其他不是User类型的数据还是交给默认的JSONEncoder处理
            JSONEncoder.default(obj)

#设置当前的jsonencoder
app.json_encoder=My_JSONEncoder

#设置SECRET_KEY
class DefaultConfig(object):
    SECRET_KEY=os.urandom(24)  #随机生成一个24位的字符串
    #设置session的有效时间为30分钟
    PERMANENT_SESSION_LIFETIME=timedelta(minutes=30)


#把参数导进来，否则不生效
app.config.from_object(DefaultConfig)

#普通类
class User():
    def __init__(self,xun,xpwd):
        self.username=xun
        self.password=xpwd

@app.route('/set')
def hello_world():
    #设置session
    session.permanent = True  # 设置session的有效时间为31天，
    # 这两行设置时间的代码都得写，否则上面设置的30分钟会失效
    print(app.config.get("SECRET_KEY"))
    session['un']='lxw'
    session['pwd']='123123'
    session['user']=User("zhangsan",'123')
    return 'hello lxw'

#读取session
@app.route('/get')
def get_cookie():
    un=session.get('un')
    pwd=session.get('pwd')
    user_obj=session.get('user')
    print(un,pwd,user_obj)
    return "获取session的值"
#直接获取session是获取不到的，要先set

"""


"""
if __name__ == '__main__':
    app.run()