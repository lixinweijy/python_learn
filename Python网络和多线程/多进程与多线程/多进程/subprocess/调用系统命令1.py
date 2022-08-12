#-*- coding=utf-8 -*-


import subprocess
# 开启一个子进程执行系统命令，args,encoding,shell三个参数
runcmd=subprocess.run('dir C:',encoding='utf-8',shell=True) #如果shell为True，则该命令由操作系统执行
print(runcmd)

print('----------------------------------')
#定义一个函数调用系统的所有命令
def run_cmd(command):
    #初始化一个子进程执行系统命令
    #subprocess.PIPE接受子进程的返回信息，一定需要解码，指定编码GBK
    return_cmd=subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding='gbk',shell=True)#PIPE建立通道，把命令里面的执行结果通过解码传回来，也可以把执行命令需要的参数传过去
    # return_cmd = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='gbk', #意思是将stderr转入stdout中一起建立通道传过去
    #                             shell=True)  # PIPE建立通道，把命令里面的执行结果通过解码传回来，也可以把执行命令需要的参数传过去
    if return_cmd.returncode==0:    #returncode  检查返回结果码，为0则没出错
        print('success:')
        print(return_cmd.stdout)
    else:
        print('命令执行错误:')
        print(return_cmd.stderr)

run_cmd('ipconfig') #正确
run_cmd("ds") #错误
