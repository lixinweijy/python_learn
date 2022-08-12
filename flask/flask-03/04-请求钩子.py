from flask import Flask,make_response,request,render_template

app = Flask(__name__)


@app.before_first_request
def before_first_request():
    print("服务器第一次接受请求的时候执行")


@app.before_request
def before_request():
    print("每次视图函数执行之前执行")
    # 如果有return，后面的视图函数就不执行了
    # return "提前结束"

@app.after_request
def after_request(resp):
    print('每次视图函数执行之后 执行')
    return resp

@app.teardown_request
def teardown_request(resp):
    print("请求结束的时候执行")

@app.route('/set')
def hello_world():
    resp = make_response('Hello World!')
    a=100/0
    return resp


@app.route('/get')
def get_cookie():
    a='abc'+100
    return "请求钩子结束"


# 当任何一个视图函数出现错误的时候直接调用
@app.errorhandler(500)
def server_error(error):
    print(error)
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run()
"""
context_processor:当项目中的所有模板中都需要一个参数的时候，
可以在context_processor钩子函数定义，并且自动传给所有的模板，
该函数一点要返回字典
"""