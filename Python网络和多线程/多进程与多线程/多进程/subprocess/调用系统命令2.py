#coding=gbk
import subprocess
# ͨ���ļ��䱾��ʽ����----��Ҫ���Ĳ�������һ���ļ�����,Ȼ��

#ͨ���ļ��䱾���θ�ϵͳ���PIPE�ǲ��ܴ��θ�ϵͳ����ģ�subprocess�нӿ�Popen���Դ��θ�ϵͳ����

f=open("/Python����Ͷ��߳�/���������߳�")

return_cmd=subprocess.run('python',stdin=f,stdout=subprocess.PIPE,shell=True)

# return_cmd.stdin='print("hello hhh")'

print(return_cmd.stdout)
# �����ַ�����ϵͳ����,һ�����ļ��䱾�ķ�ʽ,һ����Popen�ķ�ʽ,���߷���ܶ�