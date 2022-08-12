# -*- coding:utf-8 -*-
"用户提交有恶意的数据与SQL语句进行字符串方式的拼接，从而影响SQL的语句，最终产生数据泄漏或数据的篡改现象"
# 例如输入test’ or 1=1 #  后面的这个#会破坏sql中代码的意思

#为了防止这种情况发生，要让sql语句参数化
# 1.导入PyMySQL包
from pymysql import *
# 2.创建connection
conn=connect(host="localhost",port=3306,user='root',password="root",db="mytestdb",charset='utf8')
print(conn)
# 3.获取Cursor
cur=conn.cursor()
# 4.执行查询，执行命令，获取数据，处理数据
# 让用户输入用户名，密码
sname=input("请输入用户名:")
passwd=input("请输入密码:")

#编写sql语句
sql="select * from t_student where sname=%s and passwd=%s"
params=(sname,passwd)
#编写sql语句，返回查询到的记录条数rowcount，如果rowcount不为0.则登陆成功，否则反之
rowcount= cur.execute(sql,params)

if rowcount!=0:
    print("登陆成功")
else:
    print("登录失败")
# 5.关闭Cursor
cur.close()
# 6.关闭connection
conn.close()