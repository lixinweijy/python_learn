# -*- coding:utf-8 -*-
from flask import Flask

app=Flask(__name__)

app.config.from_pyfile("setting.py")

@app.route('/')
def index():
    print(app.config["USER"])
    print(app.config["PWD"])
    return "Hello World"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)