# -*- coding:utf-8 -*-

#XPath
"""
XML Path Language  是一种小型的查询语言
是一门在XML文档中查找信息的语言

"""

"""
nodename        选取此节点的所有子节点
/               从根节点选择
//              从匹配选择的当前节点选择文档中的节点
.               选取当前节点
..              选取当前节点的父节点
/text()         获取当前路径下的文本内容
/@xxx           提取当前路径下标签的属性值
|               可选符，相当于或，两者都可以选

xpath("/body/div[1]")                   选取body下的第一个div节点     
xpath("/body/div[last()]")              选取body下的最后一个div节点
xpath("/body/div[last()-1]")            选取body下的倒数第二个div节点
xpath("/body/div[position()<3]")        选取body下的前两个div节点
xpath("/body/div[@class]")              选取body下的带有class属性的div节点
xpath("/body/div[@class='main']")       选取body下的class属性为main的div节点
xpath("/body/div[price>35]")            选取body下price元素大于35的div节点
"""
