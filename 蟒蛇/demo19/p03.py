# 新知识点3：字符串操作
# https://www.runoob.com/python/python-strings.html

# 综合应用讲题（2021年计算机等级考试二级原题）
#
# 已有数据文件out.txt，其中有一些数据库操作功能的执行时间信息，如下所示:
# 操作,操作所花费的时间(单位是秒),操作时间占全部过程的百分比
# starting,0.000037,2.102
# After opening tables,0.000008,0.455
# System lock,0.000004,0.227
# 从out.txt文件中统计所有操作所花费的时间总和，并输出操作时间百分比最多的三个操作所占百分比的值，显示要求：
# the total execute time is  0.001724
# the top 0 percentage time is 46.023, spent in "Filling schema table" operation
# the top 1 percentage time is 36.932, spent in "Sending data" operation
# the top 2 percentage time is 2.784, spent in "removing tmp table" operation
