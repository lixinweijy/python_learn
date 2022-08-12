# -*- coding:utf-8 -*-
from flask import Flask,render_template

app= Flask(__name__)

student={"name":"zhangsan","age":33,"gender":"女"}

@app.route('/str')
def test1():
    return render_template('04-字符串的过滤器.html')  #为了方便在模板中使用，可以把字典打散

@app.route('/number')
def test2():
    return render_template('05-数字的过滤器.html')

@app.route('/list')
def test3():
    return render_template('06-列表的过滤器.html')

@app.route('/dict')
def test4():
    return render_template('07-字典的过滤器.html')

def get_top_3(lst): #取列表的前三个元素
    return lst[:3]

#第一种方式：注册一个过滤器
app.jinja_env.filters['get_top']=get_top_3

# 第二种
@app.template_filter("get_qu")
def get_qu(lst):   #计算列表中每个元素的平方
    return list(map(lambda  x:x*x,lst))

@app.route('/my_filter')
def test5():
    return render_template("08-自定义的过滤器.html")

if __name__ == '__main__':
    app.run()