# -*- coding:utf-8 -*-
"""
透明代理:目标网站知道你的源IP
匿名代理:知道你使用了代理，但是不知道源IP
髙匿代理:不知道你使用了代理
"""

from urllib.request import build_opener

from urllib.request import ProxyHandler

proxy=ProxyHandler({'http':'1121.13.252.58:41564'})

opener=build_opener(proxy)

url="https://www.mashibing.com/"
resp=opener.open(url)
print(resp.read().decode("utf-8"))