# flask默认支持的转换器有限，可以自定义一个正则的转换器
#首先需要继承werkzeug.routing中的BaseConverter转换器
from flask import Flask
from werkzeug.routing import BaseConverter

class RegexConverter(BaseConverter):

    def __init__(self, map):
        self.map = map

    def to_python(self, value):
        return value

    def to_url(self, value):
        if isinstance(value, (bytes, bytearray)):
            pass

#因为flask不知道有这个转换器所以需要手动加入
app = Flask(__name__)
app.url_map.converters["regex"] = RegexConverter
