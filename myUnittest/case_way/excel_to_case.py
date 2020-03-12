import json
from .case_drive import case_drive
from .case_drive_config import *
from .my_testcase import my_testcase
from ..env_config import *
from ..helper import *

try:
    import xlrd
except BaseException as e:
    print(e)
    print('检测到未安装xlrd模块,现在开始安装......')
    try:
        os.system('pip install xlrd')
        import xlrd
    except BaseException as e:
        print(e)
        print('xlrd模块安装失败')
        exit()


class excel_to_case(case_drive):
    __excel_path = excel_case_config['path']
    __excel_name = excel_case_config['default_file_name']
    __excel_sheet = excel_case_config['default_excel_sheet']
    __case_dict = {}
    __case_ary = []

    __case_env = ENV_DEV
    __case_modules = MODULES_MARKET

    def __init__(self, excel_path=__excel_path, excel_name=__excel_name, excel_sheet=__excel_sheet, env=__case_env,
                 modules=__case_modules):
        self.__excel_path = excel_path
        self.__excel_name = excel_name
        self.__excel_sheet = excel_sheet
        self.__case_env = env
        self.__case_modules = modules

    def __sheet_to_case(self, sheet):
        self.__case_ary = []
        self.__case_dict = {}
        nrows = sheet.nrows
        for i in range(nrows):
            if sheet.row_values(i)[0] != u'casename':
                my_case = my_testcase(self.__case_env, self.__case_modules)
                case_name = handle_excel_params(sheet.row_values(i)[0])
                my_case.case_name = case_name
                my_case.method = handle_excel_params(sheet.row_values(i)[1])
                my_case.url = handle_excel_params(sheet.row_values(i)[2])
                my_case.header = json.loads(str(sheet.row_values(i)[3]) if sheet.row_values(i)[3] != '' else '{}')
                my_case.data = json.loads(str(sheet.row_values(i)[4]) if sheet.row_values(i)[4] != '' else '{}')
                my_case.assertResult = sheet.row_values(i)[5]
                my_case.sql = sheet.row_values(i)[6]
                self.__case_dict[case_name] = my_case
                self.__case_ary.append(my_case)

        return self.__case_dict, self.__case_ary

    def get_all_case(self):
        sheet = xlrd.open_workbook(self.__excel_path + self.__excel_name).sheet_by_name(self.__excel_sheet)
        return self.__sheet_to_case(sheet)[1]

    def get_case_by_index(self, index_id):
        sheet = xlrd.open_workbook(self.__excel_path + self.__excel_name).sheet_by_name(self.__excel_sheet)
        return self.__sheet_to_case(sheet)[1][int(index_id)]

    def get_case_by_casename(self, casename):
        sheet = xlrd.open_workbook(self.__excel_path + self.__excel_name).sheet_by_name(self.__excel_sheet)
        return self.__sheet_to_case(sheet)[0][str(casename)]
