import os
import json
from ...env_config import *

try:
    import requests
except BaseException as e:
    print(e)
    print('检测到未安装requests模块,现在开始安装......')
    try:
        os.system('pip install requests')
        import MySQLdb
    except BaseException as e:
        print(e)
        print('requests模块安装失败')
        exit()


class request:
    __env = ENV_DEV
    __modules = MODULES_MARKET
    __host = None
    __requests = None

    def __init__(self, env=__env, modules=__modules):
        self.__env = env
        self.__modules = modules
        self.__host = get_host(self.__modules, self.__env)
        self.__requests = requests

    def set_env(self, env=__env, modules=__modules):
        self.__env = env
        self.__modules = modules
        self.__host = get_host(self.__modules, self.__env)
        return self

    def post(self, api, params=None, headers=None):
        return self.__requests.post(url=get_full_url(api, self.__modules, self.__env), data=params, headers=headers)

    def get(self, api, params=None, headers=None):
        return self.__requests.get(url=get_full_url(api, self.__modules, self.__env), params=params, headers=headers)

    def json_post(self, api, params=None, headers=None):
        headers = {} if headers is None else headers
        headers['Content-Type'] = 'application/json'
        payload = json.dumps(params)
        return self.__requests.post(url=get_full_url(api, self.__modules, self.__env), data=payload, headers=headers)

    def requests(self):
        return self.__requests
