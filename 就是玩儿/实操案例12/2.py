

class Student():
    def __init__(self,name,age,sex,score):
        self.name=name
        self.age=age
        self.sex=sex
        self.score=score

    def show(self):
        print(self.name,self.age,self.sex,self.score)

if __name__ == '__main__':
    print('请输入5位学员的信息:  (姓名#年龄#性别#成绩)')
    lst=[]
    for i in range(5):
        a=input((f'请输入第{i+1}位学员的信息和成绩:'))
        a_lst=a.split('#')
        b=Student(a_lst[0],a_lst[1],a_lst[2],a_lst[3])
        lst.append(b)
    for item in lst:
        item.show()


