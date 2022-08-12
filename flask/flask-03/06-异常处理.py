# -*- coding:utf-8 -*-
from flask import Flask,request,abort,render_template

app=Flask(__name__)

@app.route('/')
def hello_world():
    a=1/0
    #接受一个请求参数
    name=request.args.get('name')
    if name:
        print(name)
    else:
        abort(500)
    print("后面的代码不执行")
    return "hello world!"

@app.errorhandler(400)
def page_not_found(error):
    print(error)
    return render_template("404.html"),404

@app.errorhandler(501)
def page_not_found(error):
    print(error)
    return render_template("500.html"),501

@app.errorhandler(ZeroDivisionError)
def operate_error(e):
    print(e)
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run()