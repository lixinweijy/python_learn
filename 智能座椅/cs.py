#多线程和随机数库
import random,threading
#导入库文件
from MysqlHelper import *
from paho.mqtt import client as mqtt_client
#引入flask框架
from flask import Flask,render_template
app=Flask(__name__)# 初始化Flask项目的服务
#与数据库建立连接
shoper = MysqlHelper(MysqlHelper.conn_paramsl)

broker = 'test.ranye-iot.net'
port = 1883
topic = "shd"
# generate client ID with pub prefix randomly

client_id = f'python-mqtt-{random.randint(0, 100)}'


"""
编写 MQTT 连接函数
编写连接回调函数on_connect，该函数将在客户端连接后被调用，在该函数中可以依据rc来判断客户端
是否连接成功。同时我们将创建一个MQTT客户端，该客户端将连接到test.ranye-iot.net
"""

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

"""
订阅消息
编写消息回调函数on_message，该函数将在客户端从MQTT Broker收到消息后被调用，在该函数中我们将
打印出订阅的topic名称以及接收到的消息内容，并将数据写入数据库。
"""
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{int(msg.payload.decode())}` from `{msg.topic}` topic")
        #把数据写入数据库
        sql = "insert into test values (%s);"
        params = (msg.payload.decode())
        shoper.insert(sql, params)
        # render_template("haihaihai.html", my_num=msg.payload.decode())
    client.subscribe(topic)
    client.on_message = on_message

#网页部分显示数据
@app.route('/')
def hello_world():
    #获取最新数据
    sql = "select datas from test where num=(select max(num) from test) and num>%s;"
    num = shoper.get_one(sql,0)[0]
    return render_template("haihaihai.html",my_num=num)

def run():
    t=threading.Thread(target=app.run)
    t.start()
    client = connect_mqtt()
    subscribe(client)
    m=threading.Thread(target=client.loop_forever)
    m.start()

if __name__ == '__main__':
    run()
