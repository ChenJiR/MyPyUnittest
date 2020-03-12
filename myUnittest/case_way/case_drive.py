import abc


class case_drive(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_all_case(self):
        pass

    @abc.abstractmethod
    def get_case_by_index(self, index_id):
        pass

    @abc.abstractmethod
    def get_case_by_casename(self, casename):
        pass
