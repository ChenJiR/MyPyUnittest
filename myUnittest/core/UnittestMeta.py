from ..setting import setting
from . import log
from ..tag import Tag
from .Tool import *


class UnittestMeta(type):
    def __new__(cls, clsname, bases, attrs):
        funcs, cases = Tool.filter_test_case(attrs)
        for test_case in cases.values():
            if not hasattr(test_case, CASE_TAG_FLAG):
                setattr(test_case, CASE_TAG_FLAG, {Tag.ALL})  # 没有指定tag的用例，默认带有tag：ALL

            # 注入用例信息
            case_info = "{}.{}".format(test_case.__module__, test_case.__name__)
            setattr(test_case, CASE_INFO_FLAG, case_info)

            # 检查用例描述
            if setting.check_case_doc and not test_case.__doc__:
                log.warn("{}没有用例描述".format(case_info))

            # 过滤不执行的用例
            if not getattr(test_case, CASE_TAG_FLAG) & set(setting.run_case):
                continue

            # 注入测试数据
            if hasattr(test_case, CASE_DATA_FLAG):
                funcs.update(Tool.create_case_with_case_data(test_case))
            else:
                funcs.update(Tool.create_case_without_case_data(test_case))

        return super(UnittestMeta, cls).__new__(cls, clsname, bases, funcs)
