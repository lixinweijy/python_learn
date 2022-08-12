# -*- coding:utf-8 -*-
from flask import Flask,request

app=Flask(__name__,static_url_path='/lxw',static_folder='static')# 初始化Flask项目的服务

@app.route('/')
def hello_world():
    return 'hello world!'

@app.route('/test1',methods=['GET'])
def test1():
    id=request.args.get("user_id")
    print("用户id是:{}".format(id))
    name = request.args.get("name")
    print("用户名字是:{}".format(name))
    return '请求成功'
"""该函数处理post请求"""
@app.route('/test2',methods=["POST"])
def test2():
    name=request.form.get("user_name")
    age=request.form.get("user_age")
    print("name的值是:{},类型是{}".format(name,type(name)))
    print("age的值是:{},类型是{}".format(age,type(age)))
    #文件上传时，注意：需要再表单页面中加属性  enctype="multipart/form-data"
    f=request.files['image']
    f.save('./static/demo.jpg')
    return "post请求成功"
if __name__ == '__main__':
    #0.0.0.0代表当前系统中所有的ip地址,端口号默认5000,flask的debug模式：把错误的信息显示到网页中
    app.run(host='0.0.0.0',port=8080,debug=False)