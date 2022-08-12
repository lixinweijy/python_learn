import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
def ceshi():
    a=input("请输入你的出生年月日(xxxx xx xx):\n").split()
    b=input("请输入你要测试年月日(xxxx xx xx):\n").split()
    last=dt.datetime(int(a[0]),int(a[1]),int(a[2]))
    ce=dt.datetime(int(b[0]),int(b[1]),int(b[2]))
    day=(ce-last).days
    x_itl=np.arange(day-10,day+10,0.01)
    x_mood=np.arange(day-10,day+10,0.01)
    x_stg=np.arange(day-10,day+10,0.01)
    y_itl=np.sin(2*np.pi*x_itl/33)
    y_mood=np.sin(2*np.pi*x_mood/28)
    y_stg=np.sin(2*np.pi*x_stg/23)
    plt.xlabel("date")
    plt.ylabel("status")
    plt.xticks([day,day-5,day-10,day+5,day+10],[b[1]+"."+b[2],"last five","last ten","after five","after ten"])
    plt.yticks([0,0.5,1,-0.5,-1],["$normal$","$good$","$very\ good$","$bad$","$very\ bad$"])
    plt.plot(x_itl,y_itl,label="intelligence")
    plt.plot(x_mood,y_mood,label="mood")
    plt.plot(x_stg,y_stg,label="strenght")
    plt.legend()
    plt.show()
def ceshi_1():
    try:
        ceshi()
    except:
        print("输入错误，请重新输入")
        ceshi_1()
while(1):
    ceshi_1()