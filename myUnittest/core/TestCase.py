import os
import unittest
import gzip
from .UnittestMeta import UnittestMeta
from ..setting import setting
from ..env_config import *
import re
from ..component.request.request import request

__all__ = ["_TestCase", "stop_patch", "run_case"]


class _TestCase(unittest.TestCase, metaclass=UnittestMeta):
    ENV = ENV_DEV
    MODULES = MODULES_MARKET

    DB_DRIVER_TYPE = 'mysqlclient'
    # DB_DRIVER_TYPE = 'pymysql'

    db_driver = None
    redis_driver = None
    request_driver = None

    def shortDescription(self):
        """覆盖父类的方法，获取函数的注释"""

        doc = self._testMethodDoc
        doc = doc and doc.split()[0].strip() or None
        return doc

    def setENV(self, env=ENV, modules=MODULES):
        self.ENV = env
        self.MODULES = modules
        return self

    def __get_db_driver(self):
        if self.db_driver is None:
            if self.DB_DRIVER_TYPE == 'mysqlclient':
                from ..component.database.mysqlclient_driver import mysqldb_driver
                self.db_driver = mysqldb_driver(self.ENV, self.MODULES)
            elif self.DB_DRIVER_TYPE == 'pymysql':
                from ..component.database.pymysql_driver import pymysql_driver
                self.db_driver = pymysql_driver(self.ENV, self.MODULES)
            else:
                from ..component.database.mysqlclient_driver import mysqldb_driver
                self.db_driver = mysqldb_driver(self.ENV, self.MODULES)

        return self.db_driver

    def db_select(self, sql, db_name=None):
        return self.__get_db_driver().db_select(sql, db_name)

    def db_execute(self, sql, db_name=None):
        return self.__get_db_driver().db_execute(sql, db_name)

    def __get_redis_driver(self):
        if self.redis_driver is None:
            from ..component.redis.redis_driver import redis_driver
            self.redis_driver = redis_driver(self.ENV)
        return self.redis_driver

    def redis(self, db=0):
        return self.__get_redis_driver().get_redis(db)

    def __init_request(self):
        self.redis_driver = request(env=self.ENV, modules=self.MODULES) \
            if self.redis_driver is None else self.redis_driver.set_env(env=self.ENV, modules=self.MODULES)

        return self.redis_driver

    def requests(self):
        return self.__init_request().requests()

    def post(self, api, params=None, headers=None):
        return self.__init_request().post(api=api, params=params, headers=headers)

    def get(self, api, params=None, headers=None):
        return self.__init_request().get(api=api, params=params, headers=headers)

    def json_post(self, api, params=None, headers=None):
        return self.__init_request().json_post(api=api, params=params, headers=headers)

    @staticmethod
    def thread(thread_num, target, args=()):
        from ..component.thread.thread import thread
        thread.thread(thread_num, target, args)

    def thread_post(self, go_num, api, params=None, headers=None):
        from ..component.thread.thread import thread
        thread = thread(self.ENV, self.MODULES)
        thread.thread_post(go_num, api, params=params, headers=headers)

    def thread_get(self, go_num, api, params=None, headers=None):
        from ..component.thread.thread import thread
        thread = thread(self.ENV, self.MODULES)
        thread.thread_get(go_num, api, params=params, headers=headers)

    def thread_json_post(self, go_num, api, params=None, headers=None):
        from ..component.thread.thread import thread
        thread = thread(self.ENV, self.MODULES)
        thread.thread_json_post(go_num, api, params=params, headers=headers)

    def gzip_decompress(self,content):
        return gzip.decompress(content).decode("utf-8")


TestCaseBackup = unittest.TestCase
unittest.TestCase = _TestCase


def stop_patch():
    unittest.TestCase = TestCaseBackup


def run_case(case_class, case_name: str):
    setting.execute_interval = 0.3
    r = re.compile(case_name.replace("test_", "test(_\d+)?"))
    suite = unittest.TestSuite()
    for i in unittest.TestLoader().loadTestsFromTestCase(case_class):
        if r.match(getattr(i, "_testMethodName")):
            suite.addTest(i)
    unittest.TextTestRunner(verbosity=0).run(suite)
