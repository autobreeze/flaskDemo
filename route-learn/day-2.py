from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)

@app.route("/",methods=["GET", "POST"], endpoint="main")
def index():
    v1 = url_for("in")
    v2 = url_for("main")
    print(v1, v2)
    return "hello world"

# 使用app对象的route方法对函数进行装饰，，route(self, rule, **options)，route中含有装饰函数decorator
# 实质上是调用的add_url_rule函数去添加的路由，所以也可以直接调用该函数去添加路由
# rule为路由，entrypoint（别名）默认为函数名

#todo:反向生成的作用
@app.route("/login",endpoint="in")
def login():
    return "欢迎光临"



if __name__=="__main__":
    app.run(debug=True)