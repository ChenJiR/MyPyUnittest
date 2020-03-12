from ...env_config import *


class token:
    __env = ENV_DEV
    __modules = MODULES_MARKET

    def __init__(self, env=__env, modules=__modules):
        self.__env = env
        self.__modules = modules

    def get_token(self):
        if self.__modules == MODULES_MARKET:
            return self.get_market_token()
        elif self.__modules == MODULES_MUQY:
            return self.get_muqy_token()
        elif self.__modules == MODULES_APP:
            return self.get_app_token()
        elif self.__modules == MODULES_MALL:
            return self.get_mall_token()
        elif self.__modules == MODULES_ARK:
            return self.get_ark_token()

    def get_market_token(self):
        pass

    def get_muqy_token(self):
        pass

    def get_app_token(self):
        pass

    def get_mall_token(self):
        pass

    def get_ark_token(self):
        pass
