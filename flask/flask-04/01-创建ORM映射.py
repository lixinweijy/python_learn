from sqlalchemy import create_engine,Column,Integer,String,TEXT,BOOLEAN,Enum
from sqlalchemy.ext.declarative import declarative_base

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

# 第三步：创建表
# print(Base.metadata)
Base.metadata.drop_all() # 删除表结构
Base.metadata.create_all()