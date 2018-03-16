# -*- coding: utf-8 -*-
from driverCommon import CommonClass


class assertInfo:
    assert_result = False
    assert_message = ''

    def get_assert_info(self):
        return self

    def set_assert_info(self, assert_result, assert_message):
        self.assert_message = assert_message
        self.assert_result = assert_result


# 匹配不同种类断言
def assert_switch(type, text):
    assert_map.get(type)(text)


def assert_title(assert_text):
    return CommonClass.get_driver().title == assert_text


# 相等断言
def assert_equal(assert_oral, assert_goal):
    assert_info = assertInfo()
    assert_info.assert_result = (assert_oral == assert_goal)
    assert_info.assert_message = 'Target value is ' + assert_goal + 'Actual value is ' + assert_oral
    return assert_info


# 断言映射
def assert_switch(assert_type, assert_goal):
    return assert_map.get(assert_type)(assert_goal)


assert_map = {'assertTitle': assert_title}
