# -*- coding:utf-8 -*-
from flask import Flask
from flask_restful import Resource,Api

app=Flask(__name__)

#需求，对外提供一个api接口，可以访问某个资源，一共有三个步骤
# 步骤一:创建restful的API
api=Api(app)


# 步骤二:定义资源resource
class HelloResource(Resource):

    #定义各种操作(函数)
    def get(self):
        return {"hello":"world"}

    def put(self):
        return {"hello":"lxw"}

    def post(self):
        return {"post":"lxw"}

# 步骤三:把资源加载到API中，才能对外发布
api.add_resource(HelloResource,'/hello')

if __name__ == '__main__':
    app.run()