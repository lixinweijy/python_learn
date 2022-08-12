# -*- coding:utf-8 -*-
from flask import Flask,make_response,request

app=Flask(__name__)

#设置cookie
@app.route('/set')
def hello_world():
    resp=make_response('Hello world!')
    #默认cookie的有效时间:浏览器关闭，自动失效
    resp.set_cookie('user_id','aaaabbbb',max_age=1800)
    return resp

#读取cookie
@app.route('/get')
def get_cookie():
    u_id=request.cookies.get("user_id")
    print(u_id)
    return "获得cookie的内容"

#删除cookie
@app.route('/delete_cookie')
def delete_cookie():
    response=make_response("hello world")
    response.delete_cookie("username")
    return response

if __name__ == '__main__':
    app.run()
