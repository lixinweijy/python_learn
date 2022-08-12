# -*- coding:utf-8 -*-
import time,datetime
init_time=time.strftime("%Y-%m-%d %H:%M:%S")
#初始化数据
goods={"9787564182946":["西游记",'49','36'],"9787115503381":["红楼梦",'39','27'],"9787302526896":["三国演义",'75','54'],'9787521316964':["水浒传",'82','65']}
#数量库
nums={}
#日报信息
rb={}
#净收入
money_pure= {}
#初始化商品库
with open("商品基本库.txt",'w+') as stock:
    stock.write("序号\t\t\t\t商品号\t\t\t\t商品名称\t\t\t\t商品价格\t\t\t\t商品数量\n")
#工具
def tool(num,a):
    with open("商品基本库.txt", 'r+') as stock:
        repete = stock.readlines()
        stock.seek(0)
        if nums[num] > 1 or a==0:
            for i in range(1, len(repete)):
                #!!!
                stock.readline()
                if num in repete[i]:
                    # print(stock.tell())
                    stock.seek(stock.tell())
                    # print(stock.tell())
                    stock.write(" " + str(i) + "\t\t\t" + num + "\t\t\t " + goods[num][0] + "\t\t\t\t " + goods[num][1] + "元\t\t\t\t   " + str(nums[num])+"\n")
                    break
        elif a==1:
            stock.write(" " + str(len(stock.readlines())) + "\t\t\t" + num + "\t\t\t " + goods[num][0] + "\t\t\t\t " + goods[num][1] + "元\t\t\t\t   " + str(nums[num]) + "\n")


#1、进货
def plus():
    q=1
    while(q!="0"):
        num=input("请输入你需要进货的商品的商品号:\n")
        try:
            a=goods.get(num,0)[0]
        except:
            flag=input("未找到改商品，是否添加数据并进货(添加请输入y):\n")
            if flag=="y":
                name = input("请输入商品名称:\n")
                def c(f):
                    try:
                        a=int(input("请输入"+f+":\n"))
                        if a>0:
                            return a
                        print("价格要大于0哦")
                        c(f)
                    except:
                        print("输入的为非法数字，请重新输入")
                        c(f)
                price1=str(c("进价"))
                price2=str(c("售价"))
                goods[num] = [name, price2,price1]
            else:
                print("再来一次吧")
                continue
        nums[num]=nums.get(num,0)+1
        tool(num,1)
        goods[num].append(1)
        rb[num]=rb.get(num,0)-int(goods[num][2])
        q=input("是否需要继续进货，退出进货按0\n")
    print("退出进货")


#2、售卖
def delete():
    q=1
    while q!="0":
        sale=input("请选择你需要售卖的商品的商品号:\n")
        nums[sale] = nums.get(sale, 0)
        if nums[sale]:
            def c():
                try:
                    num = int(input("请输入你要售卖的数量:\n"))
                    if num<=0:
                        raise 11
                    nums[sale]-=num
                    if nums[sale]<0:
                        need=input(f"库存不够了，只有{nums[sale]+num}件啦，全部都要售卖吗?(要则输入y)\n")
                        if need=="y":
                            nums[sale]=0
                            num=nums[sale]+num
                        else:
                            print("那就重新输吧")
                            c()
                    return num
                except:
                    print("要输入合法数字哦，再来一次吧")
                    c()
            num=c()
            print("售卖成功")
            tool(sale,0)
            rb[sale] = rb.get(sale, 0) + int(goods[sale][1])*num
            money_pure[sale]=(int(goods[sale][1])-int(goods[sale][2]))*num
        else:
            print("没货了哦，要及时进货")
        q = input("是否需要继续售卖，退出售卖按0\n")
    print("退出售卖")


#3、修改
def modify():
    q=1
    while q!="0":
        def c():
            try:
                modfy=input("请输入你要修改价格的商品的商品号:\n")
                price=input("请输入新价格:\n")
                goods[modfy][1]=price
                if int(price)<0:
                    raise 11
                return modfy
            except:
                print("商品号或者价格输入有误,再来一次吧")
                c()
        tool(c(), 0)
        print("修改成功")
        q = input("是否需要继续修改，退出修改按0\n")


#4、查找
def search():
    q=1
    while q!="0":
        choice=input("请选择你要查询的项目:\n[a]显示所有商品信息\t\t[b]按商品号查找商品信息\n")
        if choice=="b":
            select=input("请输入你需要查找的商品号:\n")
            a=goods.get(select,0)
            print("名称:"+a[0]+"\t"+"价格"+a[1]+"元"+"\t\t"+"库存:"+str(nums.get(select,0))) if a else print("未找到该商品")
        elif choice=='a':
            with open("商品基本库.txt", 'r') as search_file:
                print(search_file.read())
        else:
            print("请输入a或者b")
            search()
            break
        q=input("是否退出查找，退出请按0\n")

#5、备份
def copy():
    name=input("请输入你要建立的备份库的名称(不用加后缀):\n")
    with open("商品基本库.txt",'r') as copied_file:
        a=copied_file.read()
        with open(name+".txt","w") as copy_file:
            copy_file.write(a)
    print("备份完成")

#6、日报
def daily_report():
    last_time = str(datetime.datetime.today())[:19]
    lt = list(rb.items())
    print("********************* 日   报 *************************")
    print(f"{init_time}----{last_time}")
    #单次的收入
    money=0
    #总净收入
    money_pure1=0
    #卖出数量z[数量,收入,名字]
    z=[]
    for i in range(len(lt)):
        money_pure[lt[i][0]]=money_pure.get(lt[i][0],0)
        print("商品"+goods[lt[i][0]][0]+f"卖出{len(goods[lt[i][0]])-3-nums[lt[i][0]]}件，"+f"买入{len(goods[lt[i][0]])-3}件"+f"收入{lt[i][1]}元")
        z.append([len(goods[lt[i][0]])-3-nums[lt[i][0]],money_pure[lt[i][0]],goods[lt[i][0]][0]])
        money+=lt[i][1]
        money_pure1+=money_pure[lt[i][0]]
    print(f"总收入为 {money}")
    print(f"净收入为 {money_pure1}")
    try:
        z.sort(key=lambda x:x[0],reverse=True)
        print(f"卖的最好的是{z[0][2]},可以多多进货") if z[0][0]>0 else print("商店无人问津")
        z.sort(key=lambda x: x[1], reverse=True)
        if z[0][1]>0:
            print(f"获益最高的是{z[0][2]},值得进货")
        if money_pure1>200:
            print("收入较大")
        elif money_pure1>100:
            print("收入一般")
        else:
            print("收入微薄")
    except:
        print("不行么，一点收支也没有")
    print("******************************************************\n")
#7、菜单
def menu():
    try:
        print("""******************************************************
*******      a.进货      b.售卖      c.修改      ********
*******  d.查询     e.备份     f.日报     q.退出  ********
******************************************************""")
        select=input("请选择你需要执行的任务:\n")
        if select=="a":
            plus()
        elif select=="b":
            delete()
        elif select=="c":
            modify()
            print("退出修改")
        elif select=="d":
            search()
            print("退出查找")
        elif select=="e":
            copy()
        elif select=="q":
            print("谢谢使用")
            return 1
        elif select=="f":
            daily_report()
        else:
            print("输入错误，请重试:\n")
            menu()
    except:
        print("操作有误，再来吧")
        menu()
while bool(menu())==False:
    pass