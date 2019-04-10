import redis


class Config(object):
    """工程配置信息"""
    DEBUG = True

    """sqlalchemy配置信息"""
    DEBUG = True
    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:20110923@127.0.0.1:3306/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    """redis配置信息"""
    ...
    # redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    """session配置信息"""
    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
    ...
    # flask_session的配置信息
    SESSION_TYPE = "redis" # 指定 session 保存到 redis 中
    SESSION_USE_SIGNER = True # 让 cookie 中的 session_id 被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT) # 使用 redis 的实例
    PERMANENT_SESSION_LIFETIME = 86400 # session 的有效期，单位是秒