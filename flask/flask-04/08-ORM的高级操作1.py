from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,TEXT,BOOLEAN,Enum,DATE,DECIMAL,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,backref
import random

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

#学生和课程之间就是多对多的关系
#第一步：定义中间表
temp_tab=Table(
    't_temp_tab',
    Base.metadata,
    #第三步，定义中间表的两个外键字段作为联合主键
    Column("s_id",Integer,ForeignKey("t_student.id"),primary_key=True),
    Column("c_id",Integer,ForeignKey("t_course.id"),primary_key=True)
)

#第二步：定义两个多对多的模型对象
class Student(Base):
    __tablename__='t_student'
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(30))
    age=Column(Integer)

    #第四步:定义关联关系,secondary=中间表的变量名字
    course_list=relationship("Course",backref='student_list',secondary=temp_tab)

    # __mapper_args__={
    #     #新的映射参数，用于排序
    #     "order_by":age.desc()
    # }
    def __repr__(self):
        return "<Student:name=%s,age=%s>"%(self.name,self.age)
class Course(Base):
    __tablename__="t_course"
    id = Column(Integer, primary_key=True, autoincrement=True)
    c_name = Column(String(30))
    def __repr__(self):
        return "<Course:name=%s>"%self.c_name


session=sessionmaker(engine)()

#创建表
# Base.metadata.create_all()
def save():
    students=[]
    for x in range(10):
        s=Student(name="name-%s"%x,age=random.randint(18,100))
        students.append(s)
    session.add_all(students)
    session.commit()


def query():
    #第一种排序，直接在query查询的时候加入order_by函数
    students=session.query(Student).order_by(Student.age.desc()).all()
    print(students)

    #第二种排序
    # students=session.query(Student).all()
    # print(students)

def page_query():
    # lst=session.query(Student).offset(2).limit(10).all()  #offset(n)从n条后面开始差
    lst = session.query(Student).slice(2,8).all() #slice前开后闭
    print(lst)


def update():
    pass

if __name__ == '__main__':
    # save()
    # query()
    page_query()
