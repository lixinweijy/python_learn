# -*- coding:utf-8 -*-

from pymysql import *
conn=connect(host="localhost",port=3306,user="root",password="root",db="mytestdb",charset='utf8')
print(conn)
cur=conn.cursor()
try:
    sql="insert into t_student_1 values (%s,%s,%s,%s,%s,%s,%s)"
    params=(None,'李新伟',"男",20,"2022-03-16","python全栈","lxw@python.com")
    cur.execute(sql,params)

    conn.commit()
except:
    conn.rollback()
print("数据输入成功")
cur.close()
conn.close()


