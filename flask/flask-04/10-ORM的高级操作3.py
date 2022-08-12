from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,TEXT,BOOLEAN,Enum,DATE,DECIMAL,func
from sqlalchemy.ext.declarative import declarative_base
from datetime import date
from sqlalchemy.orm import sessionmaker,relationship,backref
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
    emps=relationship("Detp",overlaps="emps",backref=backref('emps',lazy="dynamic"))  #lazy默认值是select

    def __str__(self):
        return "EMP:<员工编号:{},员工姓名:{}>".format(self.emp_no,self.e_name)

#创建表
# Base.metadata.create_all()

session=sessionmaker(engine)()

def test_group():
    #统计每个工资级别下有多少员工(数量),只统计薪资大于3000
    result=session.query(Emp.sal,func.count(Emp.emp_no)).group_by(Emp.sal).having(Emp.sal > 3000).all()
    print(result)

def test_subQuery():
    #查询和张三这个员工的职位，入职时间都相同的其他员工
    #第一步：写子查询
    stmt=session.query(Emp.hire_date.label('h_d'),Emp.job.label('job')).filter(Emp.e_name=="张三").subquery()
    #写父查询
    result=session.query(Emp).filter(Emp.hire_date==stmt.c.h_d, Emp.job==stmt.c.job).all()
    print(result[0])
if __name__ == '__main__':
    test_subQuery()