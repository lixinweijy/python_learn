# -*- coding:utf-8 -*-
from flask import Flask

app = Flask(__name__)


app.laoxiao = 'hello laoxiao' # 往app中设置任意的一个参数

from item import item_bp
app.register_blueprint(item_bp,url_prefix='/item')
@app.route('/')
def hello():
    return "hello world！"


if __name__ == '__main__':
    app.run()
