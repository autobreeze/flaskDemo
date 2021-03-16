class BasicConfig:
    DEBUG = True
    SECRECT_KEY = "HKDHSHF41535"


class TestingConfig:
    DEBUG = True


class OnlineConfig:
    DEBUG = True

# 原理：通过dir（）判断属性是否在类中，然后通过大写的属性名称获取属性的值