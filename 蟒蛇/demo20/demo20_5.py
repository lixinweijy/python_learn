# -*- coding:utf-8 -*-
#新知识点：学习获取网页的源代码（google浏览器ctrl+u），并作简单分析
#任务：从www.icourse163.org/university/view/all.htm网站上提取大学列表，并统计大学与学院数量
#提取时，学会分析并处理文本，去掉相似内容
import urllib.request
import re
url="https://www.icourse163.org/university/view/all.htm#/"
#发送请求
resp=urllib.request.urlopen(url)
html=resp.read().decode("utf-8")
xueyuan=set()
daxue=set()
with open("mook.txt",'w+',encoding="utf-8") as w:
    w.write(html)
    w.seek(0)
    all=w.read()
    all_new=re.findall(r"alt=\W.*\W",all)
    for i in all_new:
        # print(i)
        if "大学生" in i:
            continue
        elif "大学" in i and "学院" in i:
            if i.index("大学")>i.index("学院"):
                daxue.add(i[5:-3])
            else:
                xueyuan.add(i[5:-3])
        elif "大学" in i:
            daxue.add(i[5:-3])
        elif "学院" in i:
            xueyuan.add(i[5:-3])
for i in daxue:
    print(i)
for i in xueyuan:
    print(i)
print(f"大学有{len(daxue)}所\n学院有{len(xueyuan)}所")