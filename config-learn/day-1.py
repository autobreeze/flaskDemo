from flask import Flask

app = Flask(__name__)
app.secret_key("djkfkdk")
app.config.from_object("settins.TestingConfig")   # 从配置环境去读取。文件名.类名

#配置文件可以用两种方式:
#1、直接使用哪个实例调用属性方式设置
#2、使用配置文件.类方式进行调用，将需要设置的属性写入对应的类属性
    #一般可以分为线上环境，测试环境，预发布环境，
    #可以设置的属性如setting