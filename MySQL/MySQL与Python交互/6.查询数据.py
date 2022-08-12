
from pymysql import *
conn=connect(host="localhost",port=3306,user="root",password="root",db="mytestdb",charset='utf8')
print(conn)
cur=conn.cursor()
sql="select sno,sname,sex,age,enterdate,classname from t_student_1 where age>=%s"
params=(19)
a=cur.execute(sql,params)
result=cur.fetchone()
print(result)
result=cur.fetchall()
print(result)
conn.commit()
cur.close()
conn.close()

