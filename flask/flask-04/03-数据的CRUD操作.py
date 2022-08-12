from sqlalchemy import create_engine,Column,Integer,String,TEXT,BOOLEAN,Enum,func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 't_movies'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)


# 创建数据库引擎
engine = create_engine(DB_URI)

# 测试数据库连接
# with engine.connect() as conn:
#     res = conn.execute('select 1')
#     print(res.fetchone())

# 第一步:创建一个基类（所有ORM中的O，对象模型的超级父类）
Base = declarative_base(engine)

#第二步：定义Python类和表的映射
class Person(Base):
    __tablename__ = 't_person'
    id = Column(name='id',type_=Integer,primary_key=True,autoincrement=True)
    name = Column(name='name',type_=String(255))
    age = Column(name='age',type_=Integer)
    address = Column(String(255))
    country = Column(String(50)) # 创建表之后新加的
    city = Column(String(50))
    def __str__(self):
        return "Person[id:{},name:{},age:{}]".format(self.id,self.name,self.age)

#创建session
session=sessionmaker(engine)()  #注意sessionmaker返回一个函数

def save():
    #讲这个对象添加到session会话中
    p1=Person(name="张三",age=18,address="海定区",city='北京市',country='中国')
    session.add(p1)

    #将session中的对象做commit操作(提交)
    session.commit()

    #一次性添加多条数据需要将多个对象添加到一个列表中，然后再用add_all函数全部添加进去

    p2=Person(name="李四",age=28,address="荆州市",city='湖北',country='中国')
    p3=Person(name="王五",age=38,address="长沙",city='湖南',country='中国')
    p4=Person(name="赵刘",age=48,address="绍兴",city='浙江',country='中国')
    session.add_all([p2,p3,p4])
    session.commit()

def query():
    p=session.query(Person).first()  #第一个
    print(p)
    p_list=session.query(Person).all()  #全部
    print(p_list)
    print(p_list[1])  #第二个

    #查询年龄在18岁以上的
    list=session.query(Person).filter(Person.age>18)  #打印sql语句，只有加上first，all的函数才会返回具体的数据
    list=list.all()
    print(list[0])
    #年龄在18岁以上，38岁以下
    list = session.query(Person).filter(Person.age)
    print(list.all()[1])
    #查询所有年龄大于18岁的人数
    list=session.query(func.count(Person.id)).filter(Person.age>18).first()
    print(list[0])

def update():
    p=session.query(Person).filter(Person.id==1).first()
    p.age=60
    session.commit()

def delete_person():
    p = session.query(Person).filter(Person.id == 1).first()
    session.delete(p)
    session.commit()


if __name__ == '__main__':
    # query()
    # update()
    delete_person()