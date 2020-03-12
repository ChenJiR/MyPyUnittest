from ...env_config import get_db_config, MODULES_MARKET
from .db_driver import db_driver
import os

try:
    import MySQLdb
except BaseException as e:
    print(e)
    print('检测到未安装MySQLdb模块,现在开始安装......')
    try:
        os.system('pip install MySQLdb')
        import MySQLdb
    except BaseException as e:
        print(e)
        print('pymysql模块安装失败')
        exit()


class mysqldb_driver(db_driver):
    __env = None
    __db = None
    __db_name = None

    def __init__(self, env, modules):
        self.set_env(env, modules)

    def set_env(self, env, modules=None):
        # 设置环境
        self.__env = env
        if self.__db_name is None:
            # 若db_name为空 则根据modules 找默认db_name
            modules = modules if modules is not None else MODULES_MARKET
            self.__db_name = get_db_config(modules, env)['default_db']
        elif modules is not None:
            # 若db_name不为空，则判断modules是否传入，传入的话按照传入的modules寻找，否则不进行任何操作
            self.__db_name = get_db_config(modules, env)['default_db']

        return self

    def __db_connect(self, db_name):
        if self.__db_name is None and db_name is None:
            raise RuntimeError('数据库名称未设置')
        db_config = get_db_config(env=self.__env)
        self.__db = MySQLdb.connect(
            host=db_config['host'], port=db_config['port'],
            user=db_config['username'], passwd=db_config['password'],
            db=db_name if db_name is not None else self.__db_name,
        )

    # 执行数据库查询
    def db_select(self, sql, db_name=None):
        self.__db_connect(db_name)

        cursor = self.__db.cursor()
        try:
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as ex:
            print(ex)
            print("Error: unable to fetch data")
            self.__db.close()
            exit()

    # 执行数据库语句（update insert）
    def db_execute(self, sql, db_name=None):
        self.__db_connect(db_name)

        cursor = self.__db.cursor()
        try:
            cursor.execute(sql)
            self.__db.commit()
        except Exception as ex:
            print(ex)
            print("Error: unable to execute data")
            self.__db.rollback()
            self.__db.close()
            exit()
