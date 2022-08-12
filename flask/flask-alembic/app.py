from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
import config
app = Flask(__name__)
# 把配置加载到Flask项目
app.config.from_object(config)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__='t_user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    uname = db.Column(db.String(50))
    pwd = db.Column(db.String(50))
    age = db.Column(db.Integer)
    address = db.Column(db.String(50))

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
