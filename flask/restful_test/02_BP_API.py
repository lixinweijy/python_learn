# -*- coding:utf-8 -*-
from flask import Flask,Blueprint,request
from flask_restful import Resource,Api

bp=Blueprint("user",__name__) #创建蓝图
app=Flask(__name__)

#需求，对外提供一个api接口，可以访问某个资源，一共有三个步骤
# 步骤一:创建restful的API
api=Api(bp)


# 步骤二:定义资源resource
class HelloResource(Resource):

    #定义各种操作(函数)
    def get(self):
        id=request.args.get('id')
        return {"hello":"world"+id}

    def put(self):
        id = request.args.get('id')
        return {"hello":"lxw"+id}

    def post(self):
        id = request.args.get('id')
        return {"post":"lxw"+id}

# 步骤三:把资源加载到API中，才能对外发布
api.add_resource(HelloResource,'/hello')

#在加载资源之后实现
app.register_blueprint(bp,url_prefix="/user")  # 注册蓝图
# 注意：当前情况下的接口访问地址=蓝图的url_prefix  + 资源的请求路径

# app.run可以省略
