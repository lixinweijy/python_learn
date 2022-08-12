#coding=gbk
import subprocess

# print(dir(subprocess))
# popen=subprocess.Popen("dir D://",encoding="utf-8",shell=True)
#
# print(popen)
# print(popen.stdout)#不行，错误示范
#创建一个子进程
popen=subprocess.Popen("python",stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE,shell=True)
#向python中输入三条参数
popen.stdin.write('print("hello")\n'.encode("utf-8"))
popen.stdin.write('import os\n'.encode("utf-8"))
popen.stdin.write('print(os.environ)'.encode("utf-8"))

#关闭输入
popen.stdin.close()

out=popen.stdout.read().decode("gbk")
# communicate能够返回子进程执行的结果和错误的信息结果
# out,err=popen.communicate()
popen.stdout.close()
print(out)

"""
poll():检查进程是否终止，如果终止返回returncode，否则返回None
wait(timeout):等待子进程终止
communicate(input,timeout):和子进程交互，读取和发送数据
send_signal(signal):发送信号到子进程
terminate():终止子进程，也就是发送sigterm信号到子进程
kill():杀死子进程，发送sigkill信号到子进程
"""