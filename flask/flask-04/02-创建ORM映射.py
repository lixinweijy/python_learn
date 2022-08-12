from sqlalchemy import create_engine,Column,Integer,String,TEXT,BOOLEAN,Enum
from sqlalchemy.ext.automap import automap_base

# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 't_movies'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)


# 创建数据库引擎
engine = create_engine(DB_URI)

#自动映射
Base=automap_base()
Base.prepare(engine,reflect=True)

#获取所有表的映射类,注意：自动映射的话表名和类名字一样
tables=Base.classes.keys()
print(tables)

#可以重新定义类的名字
Person=Base.classes.t_person

#得到当前类中所有的属性
keys=Person.__table__.columns.keys()
print(keys)