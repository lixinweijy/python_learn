# -*- coding:utf-8 -*-

# connection参数
"""
host:连接MySQL主机，如果是本机则为'localhost'
port:连接MySQL的主机端口，默认3306
database:数据库的名称
user:连接的用户名
password:连接的密码
charset:通信采用的编码格式，推荐使用utf8
"""
# connection API
"""
connect():创建一个数据库连接实例
close():发送一个退出消息，并关闭连接
commit():提交修改至数据库
cursor():创建一个cursor(游标)实例
ping():检测服务器是否在运行
rollback():回滚当前事务
select_db(db):设置当前db
show_warnings():显示警告信息
"""

# Cursor API
"""
close() 关闭当前cursor
execute() 执行一个sql语句
executemany() 批量执行sql语句
fetchall() 取所有数据
fetchallmany() 取多条数据，指定取数据条数
fetchone() 取一条数据
"""

# 1.导入PyMySQL包
from pymysql import *
# 2.创建connection
conn=connect(host="localhost",port=3306,user="root",password="root",db="mysql",charset='utf8')
print(conn)
# 3.获取Cursor
cur=conn.cursor()
# 4.执行查询，执行命令，获取数据，处理数据
# 让用户输入用户名，密码
sname=input("请输入用户名:")
passwd=input("请输入密码:")

#编写sql语句
sql="select * from t_student where sname='%s' and passwd='%s'"%(sname,passwd)

#编写sql语句，返回查询到的记录条数rowcount，如果rowcount不为0.则登陆成功，否则反之
rowcount= cur.execute(sql)

if rowcount!=0:
    print("登陆成功")
else:
    print("登录失败")
# 5.关闭Cursor
cur.close()
# 6.关闭connection
conn.close()


