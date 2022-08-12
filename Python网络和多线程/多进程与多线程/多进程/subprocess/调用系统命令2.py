#coding=gbk
import subprocess
# 通过文件句本方式传参----把要传的参数放在一个文件里面,然后传

#通过文件句本传参给系统命令，PIPE是不能传参给系统命令的，subprocess有接口Popen可以传参给系统命令

f=open("/Python网络和多线程/多进程与多线程")

return_cmd=subprocess.run('python',stdin=f,stdout=subprocess.PIPE,shell=True)

# return_cmd.stdin='print("hello hhh")'

print(return_cmd.stdout)
# 有两种方法给系统传参,一种是文件句本的方式,一种是Popen的方式,后者方便很多