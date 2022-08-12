class Cpu:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

# (1)变量的赋值
cpu1=Cpu()
cpu2=cpu1
print(cpu2,id(cpu2))
print(cpu1,id(cpu1))

# (2)类的浅拷贝
print('------------------------------------------------------')
disk=Disk() # 创建一个硬盘类的对象
computer=Computer(cpu1,disk) #创建一个计算机类的对象

# 浅拷贝--拷贝对象，但对象的子对象不拷贝，所以原对象和拷贝对象都会引用同一个子对象
import copy
print(disk)
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)

print('----------------------------------------------------')
# 深拷贝--对源对象和子对象都拷贝，id改变
computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)