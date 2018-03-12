# -*- coding: utf-8 -*-


# browser WebDriver单例
class CommonClass:
    driver = None

    @classmethod
    def get_driver(cls):
        return cls.driver

    @classmethod
    def set_driver(cls, driver):
        cls.driver = driver
