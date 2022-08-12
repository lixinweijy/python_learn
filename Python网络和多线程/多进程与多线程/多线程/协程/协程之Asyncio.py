# -*- coding:utf-8 -*-
import asyncio

async def func1():  #定义一个协程
    for i in range(5):
        print("协程a！！！")
        await asyncio.sleep(0)  #人为模拟IO阻塞

async def func2():
    for i in range(5):
        print("协程b！！！")
        await asyncio.sleep(0)

#获取循环事件
loop = asyncio.get_event_loop()

#启动多个协程并行执行
loop.run_until_complete(asyncio.gather(func1(),func2()))

loop.close()