# -*- coding:utf-8 -*-
import os
import time
import datetime
"""
st_size         文件体积大小(bytes)
st_atime        文件最近的访问时间
st_mtime        文件最近的修改时间
st_ctime        windows下表示创建时间
st_birthtime    只在Mac，Liux下可用，表示创建时间
"""
for i in os.scandir():
    print(i.stat())

print(time.ctime(time.time()))
that_time=datetime.datetime.fromtimestamp(time.time())
print(that_time)

#查询文件信息
print(os.stat('3.查询文件信息.py'))

#在指定路径下找到今天下午14点之前创建的python文件
for file in os.scandir():
    that=file.stat()
    start_time=that.st_ctime
    user_time=datetime.datetime.fromtimestamp(start_time)
    hour=user_time.hour
    if hour<14:
        print(file)