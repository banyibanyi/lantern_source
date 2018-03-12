# encoding: utf-8


class assertInfo:
    assert_result = False
    assert_message = ''

    def get_assert_info(self):
        return self;

    def set_assert_info(self, assert_result, assert_message):
        self.assert_message = assert_message
        self.assert_result = assert_result
