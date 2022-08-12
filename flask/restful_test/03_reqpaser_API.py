# -*- coding:utf-8 -*-
from flask import Flask,Blueprint,request
from flask_restful import Resource,Api,reqparse,inputs

app=Flask(__name__)

api=Api(app)


class HelloResource(Resource):

    def get(self):
        return {"hello":"world"}

    def put(self):
        return {"hello":"lxw"}

    def post(self):
        # 步骤一: 创建请求参数校验的对象
        rq=reqparse.RequestParser()
        # 步骤二: 定义参数的校验声明
        rq.add_argument('a',type=int,required=True,help="救命，参数a错误")  #后面的required参数强制需要，如果使用help，所有的报错都是一样的 type=int,参数必须是整数
        rq.add_argument('b',type=str,required=True,action="append")  # 追加，可以写几个b
        rq.add_argument('c', type=str, choices=['男','女'])   # 选一
        rq.add_argument('d',type=inputs.regex('^\d{2}$'))  #只允许两位数的整数
        rq.add_argument('e', type=inputs.int_range(1,100))  # 只允许指定范围的整数，前闭后闭
        rq.add_argument('f', type=inputs.boolean)  # 只允许布尔类型
        # and so on

        # 还可以通过location指定提交的位置，可以是header，cookie等等


        # 步骤三: 启动校验
        req=rq.parse_args()
        # 步骤四: 校验完成之后得到参数的值+
        a=req.a
        b=req.b
        c=req.c
        d=req.d
        e = req.e
        f = req.f
        return {"post":"lxw",'a':a,'b':b,'c':c,'d':d,'e':e,'f':f}

api.add_resource(HelloResource,'/hello')

# http://127.0.0.1:5000/hello?a=323&b=sa&b=ds&c=男&d=33&e=23&f=1