#coding=gbk
import subprocess

# print(dir(subprocess))
# popen=subprocess.Popen("dir D://",encoding="utf-8",shell=True)
#
# print(popen)
# print(popen.stdout)#���У�����ʾ��
#����һ���ӽ���
popen=subprocess.Popen("python",stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE,shell=True)
#��python��������������
popen.stdin.write('print("hello")\n'.encode("utf-8"))
popen.stdin.write('import os\n'.encode("utf-8"))
popen.stdin.write('print(os.environ)'.encode("utf-8"))

#�ر�����
popen.stdin.close()

out=popen.stdout.read().decode("gbk")
# communicate�ܹ������ӽ���ִ�еĽ���ʹ������Ϣ���
# out,err=popen.communicate()
popen.stdout.close()
print(out)

"""
poll():�������Ƿ���ֹ�������ֹ����returncode�����򷵻�None
wait(timeout):�ȴ��ӽ�����ֹ
communicate(input,timeout):���ӽ��̽�������ȡ�ͷ�������
send_signal(signal):�����źŵ��ӽ���
terminate():��ֹ�ӽ��̣�Ҳ���Ƿ���sigterm�źŵ��ӽ���
kill():ɱ���ӽ��̣�����sigkill�źŵ��ӽ���
"""