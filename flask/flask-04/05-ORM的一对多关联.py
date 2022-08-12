from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,TEXT,BOOLEAN,Enum,DATE,DECIMAL
from sqlalchemy.ext.declarative import declarative_base
import time
from sqlalchemy.orm import sessionmaker,relationship
# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 't_movies'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)


# 创建数据库引擎
engine = create_engine(DB_URI)

# 第一步:创建一个基类（所有ORM中的O，对象模型的超级父类）
Base = declarative_base(engine)

#部门和员工之间，是一种典型的一（主）对多（从）

class Detp(Base):
    __tablename__="t_dept"
    dept_no=Column(Integer,primary_key=True)
    d_name=Column(String(255)) #部门名字
    city=Column(String(50))
    #代表当前目录下所有的员工列表,这种写法不是最好的，最优的写法只要在其中一个对象中关联就可以
    # emps=relationship("Emp")#参数必须是另外一个相关联的类名
    def __str__(self):
        return "DEPT:<部门编号:{},部门名:{}>".format(self.dept_no,self.d_name)


class Emp(Base):
    __tablename__="t_emp"
    emp_no=Column(Integer,primary_key=True)
    e_name=Column(String(50))
    job=Column(String(50))
    hire_date=Column(DATE)  #入职时间
    sal=Column(DECIMAL(10,2))
    dept_no=Column(Integer,ForeignKey("t_dept.dept_no",ondelete="NO ACTION"))
    emps=relationship("Detp",overlaps="emps",backref='emps')

    def __str__(self):
        return "EMP:<员工编号:{},员工姓名:{}>".format(self.emp_no,self.e_name)

#删除表
# Base.metadata.drop_all()
#创建表
# Base.metadata.create_all()


# d1=Detp(d_name="行政部",city="北京")
# e1=Emp(e_name="张三",job="manager",hire_date="2020-11-10",sal=5555,dept_no=1)
# 添加数据
session=sessionmaker(engine)()
# session.add(e1)
# session.add(d1)

# 删除
# dept=session.query(Detp).first()
# session.delete(dept)  #restrict情况下不能直接删除父表

# 提交
# session.commit()

d=session.query(Detp).first()
for i in d.emps:
    print(i)
print(d)