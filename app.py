from flask import Flask, render_template, request, redirect, session

#首先创建一个web应用的实例，name可以自定义，同时可以指定模板和静态资源的路径等
app = Flask(__name__)
app.secret_key = "qwer165165"   # 加密session
USERINFO_DIC = {"1": {"name": "刘某", "age": 35, "country": "China"},
               "2": {"name": "MARA", "age": 45, "country": "America"},
               "3": {"name": "ERT", "age": 25, "country": "Japan"},
               "4": {"name": "JOJF", "age": 55, "country": "India"}}


#处理请求，route代表的是路由，methods代表处理的接收数据的传输方法，默认是get，如果前段使用post传输则要使用post
@app.route("/")
def index():
    user_info = session.get("user_info")
    if not user_info:
        return render_template("Login.html")
    return render_template("Index.html", info=USERINFO_DIC)
#可以直接用 “return 数据”的方式去返回数据，也可以使用render_template去返回网页模板
#在render_template中外加参数去返回多个数据，在html中使用for循环使用即可
#服务端处理接收的参数，post使用request.form.get("key"),get使用request.args.get("key")

@app.route("/login", methods=['POST', 'GET'])    # methods可以是多个方法的列表['get','post']
def login():
    username = request.form.get("username")
    passward = request.form.get("pwd")
    if "admin" == username and passward == "admin123":
        session["user_info"] = username    # 设置session并将其放入cookie中
        return redirect("/")    # 重定向到登录首页
    else:
        return render_template("Login.html", fail="用户名或者密码错误") #或者用**{fail:登录失败}

@app.route("/logout", methods=["POST", "GET"])
def logout():
    del session['user_info']
    return redirect("/")

@app.route("/detail")
def detail():
    user_info = session.get("user_info")
    if not user_info:
        return redirect("/")
    uid = request.args.get("uid")   # 通过get去获取参数
    print(uid)
    info = USERINFO_DIC.get(uid)
    return render_template("Detail.html", info=info)

if __name__ == '__main__':
    #运行app，使用debug模式可以实时运行更新的代码，同时可以定义访问的地址和端口
    app.run(debug=True, host='localhost', port='80')