# -*- coding:utf-8 -*-

from pymysql import *
conn=connect(host="localhost",port=3306,user="root",password="root",db="mytestdb",charset='utf8')
print(conn)
cur=conn.cursor()
sql="insert into t_student_1 values (%s,%s,%s,%s,%s,%s,%s)"
params=[(None,'李新伟',"男",20,"2022-03-16","python全栈","xw@python.com"),
            (None,'李',"男",20,"2022-03-16","python全栈","l@python.com"),
            (None,'李新',"男",20,"2022-03-16","python全栈","lx@python.com"),
            (None,'李伟',"男",20,"2022-03-16","python全栈","lw@python.com")]
cur.executemany(sql,params)
conn.commit()
print("数据输入成功")
cur.close()
conn.close()


