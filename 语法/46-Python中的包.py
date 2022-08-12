# 一个python程序有N多个包，一个包中有N多个模块
# 在此模块中导入package包
import package.module1 as A
print(A.a)
# 导入带有包的模块时注意事项
import package
# 使用import方式进行导入时，只能跟包名或模块名
from package import  module1
from package.module1 import a
# 使用from...import可以导入包，模块，函数，变量等等