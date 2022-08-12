# -*- coding:utf-8 -*-
"""
我们自己开发的Web服务器
"""
import socket
import threading
import MyFramework
# 开发自己的Web服务器主类
class MyHttpWebServer():
    def __init__(self,port):
        #创建Http服务器的套接字
        server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #设置端口号复用，程序退出后不需要等待几分钟，直接释放
        server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
        server_socket.bind(("www.baidu.com",port))
        server_socket.listen(128)
        self.server_socket=server_socket

    #处理请求的函数
    @staticmethod
    def handle_browser_request(new_socket):
        #接收客户端发送过来的数据
        recv_data=new_socket.recv(4096)
        #如果没有接收到数据，那么请求无效，关闭套接字，直接退出
        if len(recv_data)==0:
            new_socket.close()
            return

        #对接收到的字节数据，转换成字符
        request_data=recv_data.decode("utf-8")
        print("浏览器请求的数据:",request_data)
        request_array=request_data.split(" ",maxsplit=2)
        #得到请求路径
        request_path=request_array[1]
        print("请求路径是:",request_array)
        if request_path=='/':#如果请求路径为根目录，自动设置为/index.html
            request_path="/index.html"
        #根据请求路径来判断是动态资源还是静态资源
        if request_path.endswith('.html'):
            """动态资源的请求"""
            #动态资源的处理交给Web框架来处理，需要把请求参数传给web框架，可能会有多个参数，所以用字典结构
            params={
                'request_path':request_path,
            }
            #Web框架处理动态资源请求之后，返回一个响应
            response=MyFramework.handle_request(params)
            new_socket.send(response)
            new_socket.close()
        else:
            """静态资源请求"""
            #其实就是:根据请求路径读取/static目录中静态的文件数据，响应给客户端
            response_body=None  #响应主体
            response_header=None    #响应头
            response_first_line=None    #响应的第一行
            try:
                # 读取static目录中对于的文件数据
                with open("static"+request_path,"rb") as f:
                    response_body=f.read()
                response_first_line='HTTP/1.1 200 OK\r\n'
                response_header='Server: lxw_server\r\n'
            except Exception as e:  #浏览器想读取的数据可能不存在
                with open('static/404.html','rb') as f:
                    response_body=f.read() #响应的主题页面内容
                #响应头
                response_first_line='HTTP/1.1 404 Not Found\r\n'
                response_header='Server: lxw_server\r\n'
            finally:# 组成响应数据，发送给客户端(浏览器)
                response=(response_first_line+response_header+"\r\n").encode("utf-8")+response_body
                new_socket.send(response)
                new_socket.close()

    #启动服务器，并且接收客户端的请求
    def start(self):
        #循环并且多线程来接收客户端请求
        while True:
            new_socket,ip_port=self.server_socket.accept()
            print("客户端的ip和端口",ip_port)
            #一个客户端请求交给一个线程来处理
            sub_thread=threading.Thread(target=MyHttpWebServer.handle_browser_request,args=(new_socket,))
            #设置当前线程为守护线程
            sub_thread.setDaemon(True)
            sub_thread.start()

#web服务器程序的入口
def main():
    web_server=MyHttpWebServer(8080)
    web_server.start()

if __name__ == '__main__':
    main()
