# -*- coding:utf-8 -*-

HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'alembic'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
# 把链接数据库的参数设置到app中
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
