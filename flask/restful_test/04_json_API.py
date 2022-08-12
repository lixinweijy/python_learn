# -*- coding:utf-8 -*-
from flask import Flask,Blueprint,request
from flask_restful import Resource,Api,fields,marshal_with,marshal
from flask import make_response, current_app
from flask_restful.utils import PY3
from json import dumps

bp=Blueprint("user",__name__) #创建蓝图
app=Flask(__name__)

#需求，对外提供一个api接口，可以访问某个资源，一共有三个步骤
# 步骤一:创建restful的API
api=Api(bp)

@api.representation('application/json')
def output_json(data, code, headers=None):
    """Makes a Flask response with a JSON encoded body"""

    #此处添加自己定义的JSON格式规则
    if 'message' not in data:
        data={
            'message':"ok",
            'data':data
        }

    settings = current_app.config.get('RESTFUL_JSON', {})

    # If we're in debug mode, and the indent is not set, we set it to a
    # reasonable value here.  Note that this won't override any existing value
    # that was set.  We also set the "sort_keys" value.
    if current_app.debug:
        settings.setdefault('indent', 4)
        settings.setdefault('sort_keys', not PY3)

    # always end the json dumps with a new line
    # see https://github.com/mitsuhiko/flask/pull/1262
    dumped = dumps(data, **settings) + "\n"

    resp = make_response(dumped, code)
    resp.headers.extend(headers or {})
    return resp

# 步骤二:定义资源resource
class User():
    def __init__(self,username,password,user_id):
        self.uname=username
        self.pwd=password
        self.uid=user_id

# 为了把模型对象转换成字典，在marshal里面必须定义一个属性字典
property_fileds={
    'pwd':fields.String,
    'uname':fields.String
}

class HelloResource(Resource):
    # @marshal_with(property_fileds)
    def get(self):
        u=User("zhangsan",'123123','111')
        return marshal(u,property_fileds,envelope="data1")  #envelope用来封装一下

    def put(self):
        u=User("lisi",'123123','112')
        return u

    def post(self):
        u=User("wangwu",'123123','113')
        return u

# 步骤三:把资源加载到API中，才能对外发布
api.add_resource(HelloResource,'/hello')

#在加载资源之后实现
app.register_blueprint(bp,url_prefix="/user")  # 注册蓝图
# 注意：当前情况下的接口访问地址=蓝图的url_prefix  + 资源的请求路径

# app.run可以省略
if __name__ == '__main__':
    app.run()