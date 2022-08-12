# 保留字有特定意义，不能用来命名
import keyword
print(keyword.kwlist)  #用来显示所有的保留字
# 命名的字符就是标识符，标识符不能以数字开头，不能是保留字，区分大小写
# 变量  变量由id，type，value组成
lxw='乖ba'
print(lxw)
print('标识',id(lxw))
print('类型',type(lxw))
print('值',lxw)
# name进行多次赋值之后，变量名将会指向新的空间，原本的赋值内容将会变成内存垃圾
lxw='憨b'
print(lxw)

# ok