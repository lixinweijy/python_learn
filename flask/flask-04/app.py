from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 't_movies'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
# 把链接数据库的参数设置到app中
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 1、创建数据库连接
db = SQLAlchemy(app)

# 2、创建模型类，User
class User(db.Model):
    __tablename__='t_user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    uname = db.Column(db.String(50))
    pwd = db.Column(db.String(50))
    age = db.Column(db.Integer)

    def __repr__(self):
        return "<User: uname=%s,pwd=%s,id=%s>"%(self.uname,self.pwd,self.id)

# 创建数据库的表
# db.drop_all()
# db.create_all()

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/create')
def create():
    name = request.args.get('name')
    pwd=request.args.get('pwd')
    #插入到数据库t_user表
    user=User(uname=name,pwd=pwd)
    db.session.add(user)
    db.session.commit()
    return "添加数据成功"

@app.route('/query')
def query():
    id=request.args.get('id')
    user=db.session.query(User).filter(User.id==id).first()
    print(user)
    return "查询成功，查到的用户是：%s"%user.uname

@app.route('/delete')
def delete_user():
    name=request.args.get('name')
    user=User.query.filter(User.uname==name).first()
    if user:
        db.session.delete(user)
        db.session.commit()
    return "删除成功！"

@app.route('/modify')
def modify_user():
    name=request.args.get('name')
    user=User.query.filter(User.uname==name).first()
    if user:
        user.uname='liss'
        user.pwd=1111
        db.session.commit()
    return "修改成功！"


if __name__ == '__main__':
    app.run()
