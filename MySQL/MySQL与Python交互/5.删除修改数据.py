# -*- coding:utf-8 -*-

from pymysql import *
conn=connect(host="localhost",port=3306,user="root",password="root",db="mytestdb",charset='utf8')
print(conn)
cur=conn.cursor()
sql="delete from t_student_1 where sno=%s"
params=(4)
a=cur.execute(sql,params)
conn.commit()
print("已删除"+str(a)+"条数据")
cur.close()
conn.close()


# 修改也一样
