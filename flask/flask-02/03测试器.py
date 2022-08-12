# -*- coding:utf-8 -*-
from flask import Flask,render_template
import re
app= Flask(__name__)

"""自定义测试器，首先创建函数,然后注册"""
def test_phone(phone):#手机号是否合法
    phone_re=r"1[3-9]\d{9}"
    return re.match(phone_re,phone)

@app.template_test("start_with")
def start_with(my_str,suffix):
    return my_str.lower().startswith(suffix.lower())

#两种注册测试器的方法
app.jinja_env.tests['is_phone']=test_phone

@app.route('/test_demo1')
def test1():
    return render_template('09-测试器.html')

if __name__ == '__main__':
    app.run()