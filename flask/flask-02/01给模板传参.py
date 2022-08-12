# -*- coding:utf-8 -*-
from flask import Flask,render_template

app= Flask(__name__)

"""
在jinja2中，存在三种语法:
1.控制结构(逻辑代码){% %}
2.变量取值{{  }}
3.注释{# #}
"""

student={"name":"zhangsan","age":33,"gender":"女"}

student_list=[
    {"name":"zhangsan","age":3,"gender":"女"},
    {"name":"lisi","age":44,"gender":"男"},
    {"name":"wangwu","age":65,"gender":"女"}
]

student_dict={
    'a':{"name":"zhangsan","age":33,"gender":"女"},
    'b':{"name":"lisi","age":44,"gender":"男"},
    'c':{"name":"wangwu","age":55,"gender":"女"}
}

@app.route('/test1')
def test1():
    return render_template('01.html',**student)  #为了方便在模板中使用，可以把字典打散

@app.route('/test2')
def test2():
    return render_template('02.html',stu_list=student_list)

@app.route('/test3')
def test3():
    return render_template('03.html',stu_list=student_dict)



if __name__ == '__main__':
    app.run()