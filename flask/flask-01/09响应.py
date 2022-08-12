# -*- coding:utf-8 -*-
from flask import Flask,redirect,jsonify,make_response,render_template

app=Flask(__name__,static_url_path='/lxw',static_folder='static')# 初始化Flask项目的服务

@app.route('/')
def hello_world():
    return 'hello world!'

@app.route('/demo1')
def demo1():
    return redirect("http://112.74.99.20/")

@app.route('/demo2')
def demo2():# 响应一个json数据
    json_data={
        "id":11,
        "name":"zhangsan"
    }
    return jsonify(json_data)

@app.route('/demo3')
def demo3(): #自定义一个响应，响应有三部分:response,status,headers
    return ("自定义响应的内容",600,{"my_parm":"Python-3.9"})

@app.route('/demo4')
def demo4(): #自定义一个元祖(make_response函数)
    resp=make_response("make response 响应内容")  #响应内容
    resp.status="404 not found" #响应状态
    resp.headers['my_parm']='python-3.8'  #响应头
    return resp

@app.route('/demo5')
def demo5(): #自定义一个响应，响应有三部分:response,status,headers
    return render_template('index.html',name="张三",age=33)
if __name__ == '__main__':
    #0.0.0.0代表当前系统中所有的ip地址,端口号默认5000,flask的debug模式：把错误的信息显示到网页中
    app.run(host='0.0.0.0',port=8080,debug=False)