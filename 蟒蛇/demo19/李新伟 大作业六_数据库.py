# -*- coding:utf-8 -*-
from MysqlHelper import *
import time
init_time=time.time()
shoper = MysqlHelper(MysqlHelper.conn_paramsl)

# # 创建商品库
# sql="create table shop(商品号 bigint(%s) not null primary key,商品名 varchar(10) not null,售价 decimal(10,2) not null,进价 decimal(10,2));"
# shoper.create_table(sql,14)

# # 创建数量库
# sql="create table nums(商品号 bigint(%s) not null primary key,进货数量 int(6) not null,卖出数量 int(6) not null,库存数量 int(6) not null);"
# shoper.create_table(sql,14)

# # 创建利润库
# sql="create table money_pure(商品号 bigint(%s) not null primary key,利润 decimal(10,2));"
# shoper.create_table(sql,14))

def v(num):
    def c():
        try:
            return int(input("请输入你需要进货的数量:\n"))
        except:
            print("请输入数字")
            c()
    a = c()
    sql = "select 进货数量,库存数量 from nums where 商品号=%s;"
    params = (num)
    n = shoper.get_one(sql, params)
    b, d = n[0], n[1]
    sql = "update nums set 进货数量=%s,库存数量=%s where 商品号=%s;"
    params = (b + a, d + a, num)
    shoper.update(sql, params)
    print("进货成功")

def z(s, ss):
    try:
        a = int(input(f"请输入需要{s}的商品的{ss}(输入0则退出)\n"))
        if a==0:
            return a
        if s == "进货":
            if a > 10 ** 13 or a<10**10:
                print("请输入合理商品号")
                return z(s, ss)
        else:
            if a > 10 ** 6 or a<0:
                print("请输入合理价格")
                return z(s, ss)
        return a
    except:
        print("请输入数字")
        return z(s, ss)
# 1、进货
def plus():
    num = z("进货", "商品号")
    while num:
        sql = "select * from shop where 进价>%s"
        a = shoper.get_all(sql, 0)
        for i in a:
            if num in i:
                v(num)
                break
        else:
            select = input("未找到该商品,是否添加商品并进货(输入y则添加)\n")
            if select == "y":
                name = input("请输入商品名\n")
                price_out = z("添加", "售价")
                price_in = z("添加", "进价")
                sql = "insert into shop values (%s,%s,%s,%s);"
                params = (num, name, price_out, price_in)
                shoper.insert(sql, params)
                sql = "insert into nums values (%s,0,0,0);"
                shoper.insert(sql, num)
                sql = "insert into money_pure values (%s,0);"
                shoper.insert(sql, num)
                print("添加成功")
                v(num)
        num = z("进货", "商品号")
    print("退出进货")

#----------------------------------------------------------------------------------------------------------------------------------------------------
def k(goods):
    def c():
        try:
            return int(input("请输入你需要售卖的数量:\n"))
        except:
            print("请输入数字")
            c()
    a = c()
    sql = "select 卖出数量,库存数量 from nums where 商品号=%s;"
    num = shoper.get_one(sql, goods)
    num_1, num_2 = num[0], num[1]
    if a>num_2:
        select=input("库存不够,是否购买全部库存(输入y则购买全部库存)\n")
        if select=="y":
            a=num_2
        else:
            k(goods)
            return 0
    sql = "update nums set 卖出数量=%s,库存数量=%s where 商品号=%s;"
    params = (num_1 + a, num_2 - a, goods)
    shoper.update(sql, params)
    sql = "select 售价,进价 from shop where 商品号=%s"
    price = shoper.get_one(sql, goods)
    price_1, price_2 = price[0], price[1]
    sql = "select 利润 from money_pure where 商品号=%s"
    profit = shoper.get_one(sql, goods)[0]
    sql = "update money_pure set 利润=%s where 商品号=%s;"
    params = (profit+(price_1 - price_2) * a, goods)
    shoper.update(sql, params)
    print("已卖出")
# 2、售卖
def sale():
    try:
        goods=int(input("请输入你需要售卖的商品的商品号(按0退出):\n"))
        if goods!=0:
            if goods > 10 ** 13 or goods < 10 ** 10:
                print("商品号不合理")
                goods=0
        while goods:
            sql = "select * from shop where 进价>%s"
            a = shoper.get_all(sql, 0)
            for i in a:
                if goods in i:
                    k(goods)
                    break
            else:
                print("本店没有该商品")
            goods=int(input("请输入你需要售卖的商品的商品号(按0退出):\n"))
    except:
        print("输入有误")

#----------------------------------------------------------------------------------------------------------------------------------------------------

def price(z):
    if z > 10 ** 6 or z < 0:
        z=int(input("请输入合理价格\n"))
        price(z)
    return z

def xiugai(a,b):
    q={"商品名":1,"售价":2,"进价":3}
    sql = "select * from shop where 进价>%s"
    c = shoper.get_all(sql, 0)
    for i in c:
        if a in i:
            print(f"该商品的{b}为:" + str(i[q[b]]))
            if b=="商品名":
                z= input("请输入修改后的商品名:\n")
            elif b=="进价":
                z=int(input("请输入修改后的进价:\n"))
                z=price(z)
            else:
                z=int(input("请输入修改后的售价:\n"))
                z=price(z)
            sql = f"update shop set {b}=%s where 商品号=%s"
            shoper.update(sql, (z, a))
            print("修改成功")
            break
    else:
        print("没有找到该商品")
# 3、修改
def modify():
    q=1
    while q!="n":
        try:
            a = int(input("请输入需要修改的商品的商品号:\n"))
            if a > 10 ** 13 or a < 10 ** 10:
                print("商品号不合理")
                continue
            select=input("请选择你需要修改的数据\n【a】商品名\t\t【b】售价\t\t【c】进价\n")
            if select=='a':
                xiugai(a,"商品名")
            elif select=='b':
                xiugai(a, "售价")
            elif select=='c':
                xiugai(a,"进价")
            else:
                print("请按规则输入")
                continue
        except:
            print("请输入数字")
            continue
        q=input("是否退出修改(退出请输入n)\n")

#-------------------------------------------------------------------------------------------------------------------------------------------------------
def c():
    a = input("请选择:\n【a】查看所有商品信息\t\t【b】查看指定商品信息\n")
    if a!="a" and a!="b":
        print("请按规则输入")
        c()
    return a

def d():
    try:
        a = int(input("请输入商品号\n"))
        sql = "select * from shop where 进价>%s"
        b = shoper.get_all(sql, 0)
        for i in b:
            if a in i:
                break
        else:
            q=input("没有您需要查询的商品(输入y则重新输入，否则退出查找)\n")
            if q!="y":
                return 0
            return d()
        if a > 10 ** 13 or a < 10 ** 10:
            print("请输入合理商品号")
            return d()
        return a
    except:
        print("请输入数字")
        return d()

def cha(s):
    if c() == "a":
        sql = f"select * from {s} where 商品号>=%s"
        k=0
    else:
        sql = f"select * from {s} where 商品号=%s"
        k=d()
        if k==0:
            return 1
    z = shoper.get_all(sql, k)
    if s=="money_pure":
        print("商品号".center(13)+"\t\t\t"+"利润".center(15))
    elif s=="nums":
        print("商品号".center(13)+"\t\t\t"+"   进货数量".center(17)+"\t\t\t"+"卖出数量".center(13)+"\t\t\t"+"库存数量".center(13))
    else:
        print("商品号".center(13)+"\t\t\t "+"    商品名".center(17)+"\t\t\t "+"售价           ".center(13)+"\t\t\t "+"进价           ".center(13))
    for i in z:
        for z in i:
            print(str(z).rjust(13)+"\t\t\t",end="")
        print("")

# 4、查找
def search():
    select = input("请选择你需要查询的表单:\n【a】利润表\t\t【b】数量表\t\t【c】信息表\n")
    if select=="a":
        cha("money_pure")
    elif select=="b":
        cha("nums")
    elif select=="c":
        cha('shop')
    else:
        print("请按规则输入")
        search()
#--------------------------------------------------------------------------------------------------------------------------------------------------------
# 5、备份
def copy():
    def cp(a):
        time_1 =a+str(time.strftime("%Y_%m_%d_%H_%M_%S"))
        if a=="shop":
            sql=f"create table {time_1}(商品号 bigint(%s) not null primary key,商品名 varchar(10) not null,售价 decimal(10,2) not null,进价 decimal(10,2));"
        elif a=="money_pure":
            sql = f"create table {time_1}(商品号 bigint(%s) not null primary key,利润 decimal(10,2));"
        else:
            sql=f"create table {time_1}(商品号 bigint(%s) not null primary key,进货数量 int(6) not null,卖出数量 int(6) not null,库存数量 int(6) not null);"
        shoper.create_table(sql,14)
        sql =f"select * from {a} where 商品号>%s"
        b = shoper.get_all(sql, 0)
        for i in b:
            if a == "money_pure":
                sql=f"insert into {time_1} values (%s,%s)"
            else:
                sql = f"insert into {time_1} values (%s,%s,%s,%s)"
            shoper.insert(sql,i)
    cp("shop")
    cp("nums")
    cp("money_pure")
    print("备份完成")
#----------------------------------------------------------------------------------------------------------------------------------------------------
# 6、日报
def daily_report():
    sql = "select datetime from time where datetime>%s"
    print(f"""*********************商  店  日  报*********************
**********************{str(shoper.get_one(sql,0)[0].today())}**********************
****************00:00:00------{str(time.strftime("%H:%M:%S"))}****************""")
    sql="select * from nums where 商品号>%s"
    num=shoper.get_all(sql,0)
    flag=0
    for i in num:
        flag=1
        sql = "select 商品名 from shop where 商品号=%s"
        name = shoper.get_one(sql, i[0])[0]
        sql = "select 利润 from money_pure where 商品号=%s"
        profit =shoper.get_one(sql,i[0])[0]
        if i[1]!=0 or i[2]!=0 or profit!=0:
            print(f"商品{name}共进货{i[1]}件，卖出去{i[2]}件，得到利润{profit}元")
    if flag:
        sql = "select max(利润),商品号 from money_pure where 商品号>%s"
        max_profit = shoper.get_one(sql, 0)
        sql = "select 商品名 from shop where 商品号=%s"
        name = shoper.get_one(sql, max_profit[1])[0]
        if max_profit[0]!=0:
            print(f"其中利润最高的是{name},获得利润{max_profit[0]}元,为较大的一笔经济来源")
        sql= "select max(卖出数量),商品号 from nums where 商品号>%s"
        max_num=shoper.get_one(sql,0)
        sql = "select 商品名 from shop where 商品号=%s"
        name = shoper.get_one(sql, max_num[1])[0]
        if max_num[0]!=0:
            print(f"卖出数量最多的是{name},共卖出{max_num[0]}件,是大众喜欢购买的商品，可以多多进货")
        else:
            print("真是可惜，还没有卖出商品")
    else:
        print("暂时没有商品信息")
    print("******************************************************\n")

#----------------------------------------------------------------------------------------------------------------------------------------------------
# 7、菜单
def menu():
    try:
        print("""***************************************** *************
*******      a.进货      b.售卖      c.修改      ********
*******  d.查询     e.备份     f.日报     q.退出  ********
******************************************************""")
        select = input("请选择你需要执行的任务:\n")
        if select == "a":
            plus()
        elif select == "b":
            sale()
        elif select == "c":
            modify()
            print("退出修改")
        elif select == "d":
            search()
            print("退出查找")
        elif select == "e":
            copy()
        elif select == "q":
            print("谢谢使用")
            return 1
        elif select == "f":
            daily_report()
        else:
            print("输入错误，请重试")
            menu()
    except:
        print("操作有误，再来吧")
        menu()

while bool(menu()) == False:
    now_time=time.time()
    if now_time-init_time>300:
        sql="select datetime from time where datetime>%s"
        time_init_day=str(shoper.get_one(sql,0)[0])[8:]
        time_now_day= str(time.strftime("%d"))
        if time_now_day!=time_init_day:
            time_init_day=str(time.strftime("%Y-%m-%d"))
            sql="update time set datetime=%s"
            shoper.insert(sql,time_init_day)
            copy()
            sql="update nums set 进货数量=%s,卖出数量=%s"
            shoper.update(sql,(0,0))
            sql = "update money_pure set 利润=%s"
            shoper.update(sql, 0)
        init_time=now_time