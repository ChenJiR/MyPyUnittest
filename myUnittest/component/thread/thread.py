import threading
import requests
import json
from ...env_config import *


class thread:
    __env = ENV_DEV
    __modules = MODULES_MARKET

    def __init__(self, env=__env, modules=__modules):
        self.__env = env
        self.__modules = modules

    @staticmethod
    def thread(thread_num, target, args=()):
        thread_array = {}
        for i in range(thread_num):
            t = threading.Thread(target=target, args=args)
            t.start()
            thread_array[i] = t
        for i in range(thread_num):
            thread_array[i].join()

    @staticmethod
    def __thread_post_target(url, params=None, headers=None):
        print(requests.post(url=url, data=params, headers=headers).text)

    def thread_post(self, go_num, api, params=None, headers=None):
        url = get_full_url(api, self.__modules, self.__env)
        thread_array = {}
        for i in range(go_num):
            t = threading.Thread(target=self.__thread_post_target, args=(str(url), params, headers,))
            t.start()
            thread_array[i] = t
        for i in range(go_num):
            thread_array[i].join()

    @staticmethod
    def __thread_get_target(url, params=None, headers=None):
        print(requests.get(url=url, params=params, headers=headers).text)

    def thread_get(self, go_num, api, params=None, headers=None):
        url = get_full_url(api, self.__modules, self.__env)
        thread_array = {}
        for i in range(go_num):
            t = threading.Thread(target=self.__thread_get_target, args=(str(url), params, headers,))
            t.start()
            thread_array[i] = t
        for i in range(go_num):
            thread_array[i].join()

    @staticmethod
    def __json_post_target(url, params=None, headers=None):
        headers['Content-Type'] = 'application/json'
        payload = json.dumps(params)
        print(requests.post(url=url, data=payload, headers=headers).text)

    def thread_json_post(self, go_num, api, params=None, headers=None):
        url = get_full_url(api, self.__modules, self.__env)
        thread_array = {}
        for i in range(go_num):
            t = threading.Thread(target=self.__json_post_target, args=(str(url), params, headers,))
            t.start()
            thread_array[i] = t
        for i in range(go_num):
            thread_array[i].join()
