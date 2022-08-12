# -*- coding:utf-8 -*-
from MysqlHelper import *

mysqlhelper=MysqlHelper(MysqlHelper.conn_paramsl)
sql="select sno,sname,sex,age,enterdate,classname from t_student_1 where age>=%s"
params=(19)
result=mysqlhelper.get_all(sql,params)

for i in result:
    print(i)

# # 插入数据
# mysqlhelper=MysqlHelper(MysqlHelper.conn_paramsl)
# sql="insert into t_student_1 values (%s,%s,%s,%s,%s,%s,%s)"
# params=(None,'李f伟',"男",20,"2022-03-16","python全栈","l1wx@python.com")
# rowcount=mysqlhelper.insert(sql,params)
# print("已增加"+str(rowcount)+"条数据")

# # 删除数据
# mysqlhelper=MysqlHelper(MysqlHelper.conn_paramsl)
# sql="delete from t_student_1 where sno=%s"
# params=(17)
# rowcount=mysqlhelper.delete(sql,params)
# print("已删除"+str(rowcount)+"条数据")

# 修改数据
# mysqlhelper=MysqlHelper(MysqlHelper.conn_paramsl)
# sql="update t_student_1 set sname=%s where sno=%s"
# params=("李军",'20')
# rowcount=mysqlhelper.update(sql,params)
# print("已修改"+str(rowcount)+"条数据")

mysqlhelper=MysqlHelper(MysqlHelper.conn_paramsl)
sql="create table shop(goods char(%s),jgh int(%s));"
params=(5,5)
rowcount=mysqlhelper.create_table(sql,params)
# print("已修改"+str(rowcount)+"条数据")