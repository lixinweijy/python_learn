# -*- coding:utf-8 -*-
import re
with open("三国演义（原）.txt","r",encoding="utf-8") as r:
    all=r.read()
    print(len(all))
    all_1=all.replace("！","。")
    all_2 = all_1.replace("？", "。")
    a_space=re.findall("\n第.*\n",all)
    for i in a_space:
        all_2=all_2.replace(i,"\n")
    all_3 = all_2.replace("\n", "")
    while all_3.find("\"") != -1:
        if all_3[all_3.find("\"") - 1] != "：" and all_3[all_3.find("\"") - 1] != "。":
            all_3 = all_3[:all_3.find("\"") - 1] + "。" + all_3[all_3.find("\""):]
        all_3 = all_3[:all_3.find("\"")] + "1" + all_3[all_3.find("\"") + 1:]
    all_3 = all_3.replace("1", "\"")
    print(len(all_3))

all_speak = re.findall(r'[^。]+：".*?"', all_3)
for i in range(len(all_speak)):
    a = all_speak[i].replace("\"", " ").split()
    if len(a) > 2:
        # print(all_speak[i])
        c = all_speak[i].find("副将")
        d = all_speak[i].find("也：")
        e = all_speak[i].find("人")
        f = all_speak[i].find("雄，")
        if e != -1:
            all_speak[i] = all_speak[i][:e - 1] + "'" + all_speak[i][e:]
        if f != -1:
            all_speak[i] = all_speak[i][:f + 1] + all_speak[i][f + 2:f + 5] + "'" + all_speak[i][f + 5:]
        if c != -1:
            all_speak[i] = all_speak[i][:c + 2] + "。" + all_speak[i][c + 3:]
        if d != -1:
            all_speak[i] = all_speak[i][:d + 1] + "。" + all_speak[i][d + 2:]
        # print(all_speak[i])

with open("三国演义_1.txt", "w", encoding="utf-8") as w:
    for i in all_speak:
        i = re.findall(r'[^。]+：".*?"',i)
        for j in i:
            w.write(j + "\n")

