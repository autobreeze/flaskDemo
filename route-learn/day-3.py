from flask import Flask, redirect, render_template, url_for
"""
url常用的路由系统有5种
Default_Converter{
default:   UnicodeConverter
string:     UnicodeConverter
any:        AnyConverter
path:       PathConverter
int:        IntegerConverter
float:      FloatConverter
uuid:       UUIDConverter}
"""
#todo:uuid是根据当前时间的当前主板去生成的唯一标识 jdj-jlfjdl-jsdlfjl-nlfjsldk-jlfjld
app1 = Flask(__name__)

# @app1.route("/index/<float:number>")
# @app1.route("/index/<username>")
# @app1.route("/index/<path:path>")
@app1.route("/index/<int:number>")
def index(number):
    if isinstance(number, int):
        return "hello number 1"
#整型或者其他类型定义之后由对应的转换器进行转换，转换的值会传递给对应的参数

@app1.route("/str/<str1>")
def teststr(str1):
    if isinstance(str1, str):
        return str1

if __name__== "__main__":
    app1.run(debug=True)