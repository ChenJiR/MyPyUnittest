import os

DRIVER_DB = 'db_to_case'
DRIVER_EXCEL = 'excel_to_case'
DRIVER_TXT = 'txt_to_case'

db_case_config = {
    'host': '127.0.0.1',
    'username': 'root',
    'password': 'root',
    'port': 3306,
    'db': 'test',
}

excel_case_config = {
    'path': os.path.dirname(__file__) + str('/excel_case/'),
    'default_file_name': 'case.xlsx',
    'default_excel_sheet': 'Sheet1'
}

txt_case_config = {
    'path': os.path.dirname(__file__) + str('/txt_case/'),
    'default_file_name': 'case.txt',
}


def get_db_config():
    return db_case_config


def get_excel_config():
    return excel_case_config


def get_txt_config():
    return txt_case_config
