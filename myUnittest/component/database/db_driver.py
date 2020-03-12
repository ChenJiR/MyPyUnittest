import abc


class db_driver(metaclass=abc.ABCMeta):
    __env = None
    __db = None
    __db_name = None

    @abc.abstractmethod
    def set_env(self, env, modules=None):
        pass

    @abc.abstractmethod
    def db_select(self, sql, db_name=None):
        pass

    @abc.abstractmethod
    def db_execute(self, sql, db_name=None):
        pass
