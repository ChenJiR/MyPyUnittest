from .db_to_case import db_to_case
from .excel_to_case import excel_to_case
from .case_drive_config import *
import functools


def db_allcase(env=None, modules=None):
    def wrap(func):
        @functools.wraps(func)
        def _wrap(self):
            case = db_to_case(env=env if env is not None else self.ENV,
                              modules=modules if modules is not None else self.MODULES).get_all_case()
            return func(self, case)

        return _wrap

    return wrap


def dbcase_by_index(index, env=None, modules=None):
    def wrap(func):
        @functools.wraps(func)
        def _wrap(self):
            case = db_to_case(env=env if env is not None else self.ENV,
                              modules=modules if modules is not None else self.MODULES).get_case_by_index(index)
            return func(self, case)

        return _wrap

    return wrap


def dbcase_by_casename(casename, env=None, modules=None):
    def wrap(func):
        @functools.wraps(func)
        def _wrap(self):
            case = db_to_case(env=env if env is not None else self.ENV,
                              modules=modules if modules is not None else self.MODULES).get_case_by_casename(casename)
            return func(self, case)

        return _wrap

    return wrap


def excelcase_allcase(excel_path=None, excel_file=None, excel_sheet=None, env=None, modules=None):
    def wrap(func):
        @functools.wraps(func)
        def _wrap(self):
            path = excel_path if excel_path is not None \
                else getattr(self, 'excelcase_path', None) if getattr(self, 'excelcase_path', None) is not None \
                else excel_case_config['path']

            file = excel_file if excel_file is not None \
                else getattr(self, 'excelcase_file', None) if getattr(self, 'excelcase_file', None) is not None \
                else excel_case_config['default_file_name']

            sheet = excel_sheet if excel_sheet is not None \
                else getattr(self, 'excelcase_sheet', None) if getattr(self, 'excelcase_sheet', None) is not None \
                else excel_case_config['default_excel_sheet']

            case = excel_to_case(excel_path=path, excel_name=file, excel_sheet=sheet,
                                 env=env if env is not None else self.ENV,
                                 modules=modules if modules is not None else self.MODULES).get_all_case()
            return func(self, case)

        return _wrap

    return wrap


def excelcase_by_index(index, excel_path=None, excel_file=None, excel_sheet=None, env=None, modules=None):
    def wrap(func):
        @functools.wraps(func)
        def _wrap(self):
            path = excel_path if excel_path is not None \
                else getattr(self, 'excelcase_path', None) if getattr(self, 'excelcase_path', None) is not None \
                else excel_case_config['path']

            file = excel_file if excel_file is not None \
                else getattr(self, 'excelcase_file', None) if getattr(self, 'excelcase_file', None) is not None \
                else excel_case_config['default_file_name']

            sheet = excel_sheet if excel_sheet is not None \
                else getattr(self, 'excelcase_sheet', None) if getattr(self, 'excelcase_sheet', None) is not None \
                else excel_case_config['default_excel_sheet']

            case = excel_to_case(excel_path=path, excel_name=file, excel_sheet=sheet,
                                 env=env if env is not None else self.ENV,
                                 modules=modules if modules is not None else self.MODULES).get_case_by_index(index)
            return func(self, case)

        return _wrap

    return wrap


def excelcase_by_casename(casename, excel_path=None, excel_file=None, excel_sheet=None, env=None, modules=None):
    def wrap(func):
        @functools.wraps(func)
        def _wrap(self):
            path = excel_path if excel_path is not None \
                else getattr(self, 'excelcase_path', None) if getattr(self, 'excelcase_path', None) is not None \
                else excel_case_config['path']

            file = excel_file if excel_file is not None \
                else getattr(self, 'excelcase_file', None) if getattr(self, 'excelcase_file', None) is not None \
                else excel_case_config['default_file_name']

            sheet = excel_sheet if excel_sheet is not None \
                else getattr(self, 'excelcase_sheet', None) if getattr(self, 'excelcase_sheet', None) is not None \
                else excel_case_config['default_excel_sheet']

            case = excel_to_case(excel_path=path, excel_name=file, excel_sheet=sheet,
                                 env=env if env is not None else self.ENV,
                                 modules=modules if modules is not None else self.MODULES).get_case_by_casename(
                casename)
            return func(self, case)

        return _wrap

    return wrap

