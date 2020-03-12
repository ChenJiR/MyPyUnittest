import json
from .case_drive import case_drive
from .case_drive_config import *
from .my_testcase import my_testcase
from ..env_config import *

try:
    import pymysql
except BaseException as e:
    print(e)
    print('检测到未安装pymysql模块,现在开始安装......')
    try:
        os.system('pip install pymysql')
        import pymysql
    except BaseException as e:
        print(e)
        print('pymysql模块安装失败')
        exit()


class db_to_case(case_drive):
    TABLE_NAME = 'testcase'

    __db = None
    __case_ary = []

    __case_env = ENV_DEV
    __case_modules = MODULES_MARKET

    def __init__(self, env=__case_env, modules=__case_modules):
        self.__db_connect()
        self.__case_env = env
        self.__case_modules = modules

    def __db_connect(self):
        db_config = get_db_config()
        self.__db = pymysql.connect(
            host=db_config['host'], port=db_config['port'],
            user=db_config['username'], passwd=db_config['password'],
            db=db_config['db'],
        )

    def __sql_to_case(self, sql):
        cursor = self.__db.cursor()
        result = []
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception as ex:
            print(ex)
            print("Error: unable to fetch data")
            self.__db.close()
            exit()

        self.__case_ary = []

        for item in result:
            my_case = my_testcase(self.__case_env, self.__case_modules)
            my_case.case_name = item[1]
            my_case.method = item[2]
            my_case.url = item[3]
            my_case.header = None if item[4] is None or item[4] == '' else json.loads(item[4])
            my_case.data = None if item[5] is None or item[5] == '' else json.loads(item[5])
            my_case.assertResult = item[5]
            my_case.sql = item[6]
            self.__case_ary.append(my_case)

        return self.__case_ary

    def get_all_case(self):
        return self.__sql_to_case("select * from " + str(self.TABLE_NAME))

    def get_case_by_index(self, index_id):
        return self.__sql_to_case("select * from " + str(self.TABLE_NAME) + " where id = " + str(index_id))

    def get_case_by_casename(self, casename):
        return self.__sql_to_case("select * from " + str(self.TABLE_NAME) + " where casename = " + str(casename))
