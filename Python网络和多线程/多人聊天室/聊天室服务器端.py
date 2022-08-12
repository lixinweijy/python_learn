# -*- coding:utf-8 -*-
import wx,threading
from socket import *
import time
#服务器继承wx.Frame,就拥有窗口界面
class HServer(wx.Frame):
    def __init__(self):
        #调用父类的初始化函数
        wx.Frame.__init__(self,None,id=102,title="lxw的服务器界面",pos=wx.DefaultPosition,size=(400,470))
        p1=wx.Panel(self)  #在窗口中初始化与一个面板
        #在面板里面会放入一些按钮，文本框，文本输入框等，把这些对象统一放入一个盒子里面
        box=wx.BoxSizer(wx.VERTICAL) #在盒子里面垂直方向自动排版

        g1=wx.FlexGridSizer(wx.HORIZONTAL) #可伸缩的水平网格布局
        #创建两个按钮
        start_buntton=wx.Button(p1,size=(133,40),label="启动")
        record_save_buntton=wx.Button(p1,size=(133,40),label="聊天记录保存")
        stop_buntton = wx.Button(p1, size=(133, 40), label="停止")
        g1.Add(start_buntton,1,wx.TOP)
        g1.Add(record_save_buntton,1,wx.TOP )
        g1.Add(stop_buntton, 1, wx.TOP)

        box.Add(g1,1,wx.ALIGN_CENTER) #ALIGN_CENTER联合居中

        #创建聊天内容的文本框，不能写消息
        self.read_text=wx.TextCtrl(p1,size=(400,400),style=wx.TE_MULTILINE | wx.TE_READONLY)
        box.Add(self.read_text,1,wx.ALIGN_CENTER)
        p1.SetSizer(box)#把盒子放入面板中

        """以上代码完成了服务器界面（窗口）"""

        """服务器准备执行的一些属性"""
        self.isOn=False  #服务器没有启动
        self.host_port=('',8888)
        self.server_socket=socket(AF_INET,SOCK_STREAM)  #TCP协议的服务器端套接字
        self.server_socket.bind(self.host_port)
        self.server_socket.listen(5)
        self.session_thread_map={}  #存放所有的服务器会话线程  字典：客户端名字为key ，会话线程为value


        '''给所有的按钮绑定相应的动作'''
        self.Bind(wx.EVT_BUTTON,self.start_server,start_buntton)  #会启动按钮，绑定一个按钮事件，事件触发的时候会自动调用一个函数
        self.Bind(wx.EVT_BUTTON,self.save_record,record_save_buntton)  #会启动按钮，绑定一个按钮事件，事件触发的时候会自动调用一个函数

    # 服务器开始启动函数
    def start_server(self,event):
        print("服务器开始启动")
        if not self.isOn:
            #启动服务器主线程
            self.isOn=True
            main_thread=threading.Thread(target=self.do_work)
            main_thread.setDaemon(True) #设置为守护线程
            main_thread.start()

    #服务器运行之后的函数
    def do_work(self):
        print("服务器开始工作")
        while self.isOn:
            session_socket,client_addr=self.server_socket.accept()
            # 服务器首先接收客户端发过来的第一条数据,我们规定第一条消息为客户端的名字
            username=session_socket.recv(1024).decode('utf-8')
            #创建一个会话线程
            session_thread=SessionThread(session_socket,username,self)
            self.session_thread_map[username]=session_thread
            session_thread.start()
            #表示有客户端进入到聊天室
            self.show_info_and_send_client("服务器通知","欢迎%s进入聊天室!"%username,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
        self.server_socket.close()

    #在文本中显示聊天信息，同时发送信息给所有客户端,source:信息源  data就是信息
    def show_info_and_send_client(self,source,data,time):
        send_data="%s\n%s: %s\n"%(time,source,data)
        self.read_text.AppendText("----------------------------\n%s"%send_data)
        for client in self.session_thread_map.values():
            if client.isOn:#当前客户端是活着的
                client.user_socket.send(send_data.encode("utf-8"))

    #服务器保存聊天记录
    def save_record(self,event):
        record=self.read_text.GetValue()
        with open("record.log",'w+')as f:
            f.write(record)

#服务器端会话线程的类
class SessionThread(threading.Thread):
    def __init__(self,user_socket,username,server):
        threading.Thread.__init__(self)
        self.user_socket=user_socket
        self.username=username
        self.server=server
        self.isOn=True  #会话线程是否启动
    def run(self):  #会话线程的运行
        print("客户端%s,已经和服务器连接成功，服务器启动一个会话线程"%self.username)
        while self.isOn:
            data=self.user_socket.recv(1024).decode("utf-8")  #接收客户端聊天信息
            if data=="A^disconnect^B": #如果客户端点击断开按钮，先发一条信息给服务器，信息的内容我规定:A^disconnect^B
                self.isOn=False
                #有用户离开，需要再聊天室通知其他人
                self.server.show_info_and_send_client("服务器通知","%s离开聊天室"%self.username,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
            else:
                #其他聊天信息，我们应该显示给所有客户端，包括服务器
                self.server.show_info_and_send_client(self.username,data,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
        self.user_socket.close() #保持和客户端会话的socket关掉

if __name__ == '__main__':
    app=wx.App()
    HServer().Show()
    app.MainLoop() #循环刷新显示