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


assert_map = {'assertTitle': assert_title}
