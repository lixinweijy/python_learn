# -*- coding:utf-8 -*-

#文件的复制

import shutil
#复制一个文件
shutil.copy("7.copy文件夹.py","mkdir创建的文件夹")
shutil.copy("7.copy文件夹.py",'mkdir创建的文件夹/改名了')

#复制多个文件
shutil.copytree("mkdir创建的文件夹","第一层文件夹/第二次文件夹/第三层文件夹")