from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,TEXT,BOOLEAN,Enum,DATE,DECIMAL
from sqlalchemy.ext.declarative import declarative_base
import time
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


# person 人 和 身份证是一对一的关联关系
#第一种写法: 把uselist=false加在没有外键的对象中,其他和前面的一对多关联是一样的
#第二种写法:在主表中不需要维护关联关系（不需要加关联属性），只要在从表对象中加上关联属性，并且加backref
class Person(Base):
    __tablename__ = 't_person'
    id = Column(name='id',type_=Integer,primary_key=True,autoincrement=True)
    name = Column(name='name',type_=String(255))
    age = Column(name='age',type_=Integer)
    address = Column(String(255))
    country = Column(String(50)) # 创建表之后新加的
    city = Column(String(50))

    #人对应的身份证
    # id_card=relationship("Id_Card",uselist=False)
    def __str__(self):
        return "Person:<人的编号:{},人名:{}>".format(self.id,self.name)

#身份证
class Id_Card(Base):
    __tablename__="t_id_card"
    card_number=Column(String(18),primary_key=True)
    p_id=Column(Integer,ForeignKey("t_person.id"))

    #该身份证对于的人
    # person=relationship("Person",overlaps="id_card")

    person=relationship("Person",backref=backref("id_card",uselist=False))

    def __str__(self):
        return "Id_Card:<序号:{},身份证号:{}>".format(self.p_id,self.card_number)

session=sessionmaker(engine)()
#删除表
# Base.metadata.drop_all()
#创建表
# Base.metadata.create_all()
def save():
    c1=Id_Card(card_number="1122323213",p_id=1)
    c2=Id_Card(card_number="5642342213",p_id=2)
    c3=Id_Card(card_number="6722342123",p_id=3)
    session.add_all([c1,c2,c3])
    session.commit()

def query():
    # p=session.query(Person).filter(Person.id==1).first()
    # print(p)
    # print(p.id_card.card_number)

    card=session.query(Id_Card).filter(Id_Card.card_number=='1122323213').first()
    print(card)
    print(card.person.name)
    print(card.person.age)

def update():
    #把身份证为1122323213的改成是赵六的身份证
    card=session.query(Id_Card).filter(Id_Card.card_number=="1122323213").first()
    p=session.query(Person).filter(Person.id=="5").first()
    # card.p_id=5
    card.person=p
    session.commit()
if __name__ == '__main__':
    # query()
    update()