# -*- coding:utf-8 -*-
#初始化数据
goods={"9787564182946":["西游记",'36'],"9787115503381":["红楼梦",'27'],"9787302526896":["三国演义",'54'],'456':["水浒传",'65']}
#数量库
nums={}
#初始化商品库
with open("商品基本库.txt",'w+') as stock:
    stock.write("序号\t\t\t\t商品号\t\t\t\t商品名称\t\t\t\t商品价格\t\t\t\t商品数量\n")
#工具
def tool(num,a):
    with open("商品基本库.txt", 'r+') as stock:
        repete = stock.readlines()
    with open("商品基本库.txt", 'r+') as stock:
        stock.seek(0)
        if nums[num] > 1 or a==0:
            for i in range(1, len(repete)):
                stock.readline()
                if num in repete[i]:
                    break
        elif a==1:
            stock.write(" "+str(len(stock.readlines())) + "\t\t\t" + num + "\t\t\t " + goods[num][0] + "\t\t\t\t " + goods[num][1] + "元\t\t\t\t   " + str(nums[num]) + "\n")
            print(stock.tell())
#1、进货
def plus():
    q=1
    while(q!="0"):
        num=input("请输入你需要进货的商品的商品号:\n")
        try:
            name=goods.get(num,0)[0]
            price=goods.get(num,0)[1]
        except:
            flag=input("未找到改商品，是否添加数据并进货(添加请输入y):\n")
            if flag=="y":
                name = input("请输入商品名称:\n")
                def c():
                    try:
                        a=int(input("请输入商品价格:\n"))
                        if a>0:
                            return a
                        print("价格要大于0哦")
                        c()
                    except:
                        print("输入的为非法数字，请重新输入")
                        c()
                price=str(c())
                goods[num] = [name, price]
            else:
                print("再来一次吧")
                continue
        nums[num]=nums.get(num,0)+1
        tool(num,1)
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
                num=int(input("请输入你要售卖的数量:\n"))
                try:
                    nums[sale]-=num
                    if nums[sale]<0:
                        need=input(f"库存不够了，只有{nums[sale]+num}件啦，全部都要售卖吗?(要则输入y)\n")
                        if need=="y":
                            nums[sale]=0
                        else:
                            print("那就重新输吧")
                            c()
                except:
                    print("要输入合法数字哦，再来一次吧")
                    c()
            c()
            print("售卖成功")
            tool(sale,0)
        else:
            print("没货了哦，要及时进货")
        q = input("是否需要继续售卖，退出售卖按0\n")
    print("退出售卖")

#3、修改
def modify():
    q=1
    while q!="0":
        modfy=input("请输入你要修改的商品的商品号:\n")
        select=input("请选择你需要修改的项目:\n[a]名字\t\t[b]价格\n")
        if select=='a':
            name=input("请输入新名字:\n")
            goods[modfy][0]=name
        elif select=='b':
            price=input("请输入新价格:\n")
            goods[modfy][1]=price
        else:
            print("请输入a或b")
            modify()
            break
        tool(modfy, 0)
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
    name=input("请输入你要建立的备份库的名称:\n")
    with open("商品基本库.txt",'r') as copied_file:
        a=copied_file.read()
        with open(name+".txt","w") as copy_file:
            copy_file.write(a)
    print("备份完成")
#6、菜单
def menu():
    print("""******************************************************
*******      a.进货      b.售卖      c.修改      ********
*******      d.查询      e.备份      q.退出      ********
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
    else:
        print("输入错误，请重试:\n")
        menu()
while bool(menu())==False:
    pass