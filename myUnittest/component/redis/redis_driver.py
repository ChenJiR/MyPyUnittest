from ...env_config import get_redis_config
import os

try:
    import redis
except BaseException as e:
    print(e)
    print('检测到未安装redis模块,现在开始安装......')
    try:
        os.system('pip install redis')
        import MySQLdb
    except BaseException as e:
        print(e)
        print('redis模块安装失败')
        exit()


class redis_driver:
    __env = 'dev'
    __db = 0
    __redis = None

    def __init__(self, env='dev'):
        self.set_env(env)

    # 设置环境
    def set_env(self, env):
        self.__env = env
        return self

    # 设置Redis DB
    def set_db(self, db):
        self.__db = db
        return self

    # 链接redis
    def __redis_connect(self, db=None):
        redis_config = get_redis_config(self.__env)
        pool = redis.ConnectionPool(
            host=redis_config['hostname'],
            port=redis_config['port'],
            password=redis_config['password'],
            decode_responses=True,
            db=db if db is not None else self.__db
        )
        self.__redis = redis.Redis(connection_pool=pool)
        return self.__redis

    # 封装redis set方法
    def redis_set(self, key, value, db=None):
        return self.__redis_connect(db).set(key, value)

    # 封装redis setex方法
    def redis_setex(self, key, time, value, db=None):
        return self.__redis_connect(db).setex(key, time, value)

    # 封装redis get方法
    def redis_get(self, key, db=None):
        return self.__redis_connect(db).get(key)

    # 获取redis连接实例
    def get_redis(self, db=0):
        return self.__redis if self.__redis is not None and db == self.__db else self.__redis_connect(db)
