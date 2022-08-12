# -*- coding:utf-8 -*-
from flask import Flask

app=Flask(__name__)

app.config.from_envvar("SETTING_PATH",silent=True)#在企业正式运行的情况下，silent选择True

@app.route('/')
def index():
    print(app.config["USER"])
    print(app.config["PWD"])
    return "Hello World"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)