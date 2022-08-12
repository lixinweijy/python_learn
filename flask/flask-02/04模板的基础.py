# -*- coding:utf-8 -*-
from flask import Flask,render_template

app= Flask(__name__)

@app.route('/extends')
def hello_world():
    return render_template('child.html')

@app.route('/include')
def to_include():
    return render_template('10-include标签.html')

if __name__ == '__main__':
    app.run()