import json
from .case_drive import case_drive
from .case_drive_config import *
from .my_testcase import my_testcase


class txt_to_case(case_drive):
    __txt_path = txt_case_config['path']
    __txt_name = txt_case_config['default_file_name']
    __case_dict = {}
    __case_ary = []

    def __init__(self):
        f = open(self.__txt_path + self.__txt_name, 'r')
        txt_content = []
        for line in f.readlines():
            txt_content.append(line.strip())

    def get_all_case(self):
        pass

    def get_case_by_index(self, index_id):
        pass

    def get_case_by_casename(self, casename):
        pass

    def get_txt(file_name):
        dict_temp = {}
        # 打开文本文件
        f = open('D:/read_file/' + str(file_name) + '.txt', 'r')
        # 遍历文本文件的每一行，strip可以移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
        for line in f.readlines():
            line = line.strip()
            k = line.split(':')[0]
            v = line.split(':')[1]
            dict_temp[k] = v
        # 依旧是关闭文件
        f.close()

        return dict_temp


