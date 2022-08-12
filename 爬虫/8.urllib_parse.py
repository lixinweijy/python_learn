# -*- coding:utf-8 -*-
"""
通常用于爬虫开发，API（引用程序编程接口）数据获取和测试
urllib四大模块:
1.urllib.request:打开和获取URL
2.urllib.error:包含提出的例外(异常)urllib.request
3.urllib.parse:用于解析URL
4.urllib.robotparser:用于解析robots.txt文件
"""

import urllib.parse
kw={"wd":"李新伟"}
result=urllib.parse.urlencode(kw)
print(result)

#解码
res=urllib.parse.unquote(result)
print(res)

