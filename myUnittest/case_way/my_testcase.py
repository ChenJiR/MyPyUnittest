from ..component.request.request import request
from ..env_config import *


class my_testcase:
    DB_DRIVER_TYPE = 'mysqlclient'
    # DB_DRIVER_TYPE = 'pymysql'

    __env = ENV_DEV
    __modules = MODULES_MARKET

    case_name = None
    method = None
    url = None
    data = None
    assertResult = None
    sql = None
    header = None

    __db_driver = None
    __redis_driver = None
    __request_driver = None

    def __init__(self, env=__env, modules=__modules):
        self.set_env(env, modules)

    def set_env(self, env, modules):
        self.__env = env
        self.__modules = modules
        return self

    def __get_db_driver(self):
        if self.__db_driver is None:
            if self.DB_DRIVER_TYPE == 'mysqlclient':
                from ..component.database.mysqlclient_driver import mysqldb_driver
                self.__db_driver = mysqldb_driver(self.__env, self.__modules)
            elif self.DB_DRIVER_TYPE == 'pymysql':
                from ..component.database.pymysql_driver import pymysql_driver
                self.__db_driver = pymysql_driver(self.__env, self.__modules)
            else:
                from ..component.database.mysqlclient_driver import mysqldb_driver
                self.__db_driver = mysqldb_driver(self.__env, self.__modules)

        else:
            self.__db_driver.set_env(self.__env, self.__modules)

        return self.__db_driver

    def db_select(self, db_name=None):
        return self.__get_db_driver().db_select(self.sql, db_name)

    def db_execute(self, db_name=None):
        return self.__get_db_driver().db_execute(self.sql, db_name)

    def __get_redis_driver(self):
        from ..component.redis.redis_driver import redis_driver
        self.__redis_driver = redis_driver(self.__env) \
            if self.__redis_driver is None else self.__redis_driver.set_env(self.__env)

        return self.__redis_driver

    def redis(self, db=0):
        return self.__get_redis_driver().get_redis(db)

    def __init_request(self):
        self.__request_driver = request(env=self.__env, modules=self.__modules) \
            if self.__request_driver is None else self.__request_driver.set_env(env=self.__env, modules=self.__modules)

        return self.__request_driver

    def request(self):
        return self.__init_request().post(self.url, params=self.data, headers=self.header) \
            if self.method is 'post' else \
            self.__init_request().get(self.url, params=self.data, headers=self.header)\
            if self.method is 'get' else \
            self.__init_request().json_post(self.url, params=self.data, headers=self.header)

    def thread_request(self, go_num):
        from ..component.thread.thread import thread
        thread = thread(self.__env, self.__modules)
        thread.thread_post(go_num, self.url, params=self.data, headers=self.header) \
            if self.method is 'post' else \
            thread.thread_get(go_num, self.url, params=self.data, headers=self.header)

    @staticmethod
    def thread(thread_num, target, args=()):
        from ..component.thread.thread import thread
        thread.thread(thread_num, target, args)
