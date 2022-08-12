from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,TEXT,BOOLEAN,Enum,DATE,DECIMAL,Table
from sqlalchemy.ext.declarative import declarative_base
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

    def __repr__(self):
        return "<Student:name=%s>"%self.name
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
    s1=Student(name='zs',age=22)
    s2=Student(name="lisi",age=33)
    c1=Course(c_name="数学")
    c2=Course(c_name="英语")

    s1.course_list.append(c1)
    s1.course_list.append(c2)

    s2.course_list.append(c1)
    s2.course_list.append(c2)

    session.add(s1)
    session.add(s2)

    session.commit()
def query():
    student=session.query(Student).first()
    print(student)
    print(student.course_list)

    c1=session.query(Course).first()
    print(c1)
    print(c1.student_list)
def update():
    pass
if __name__ == '__main__':
    query()