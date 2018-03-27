# -*- coding: utf-8 -*-
import logging
import logging.config


# browser WebDriver单例
class CommonClass:
    driver = None
    # 加载log配置文件
    logging.config.fileConfig("logging.conf")
    # create logger
    logger = logging.getLogger("example")

    @classmethod
    def get_driver(cls):
        return cls.driver

    @classmethod
    def set_driver(cls, driver):
        cls.driver = driver

    @classmethod
    def get_logger(cls):
        return cls.logger

    @classmethod
    def stop_log_listing(cls):
        logging.config.stopListening()

