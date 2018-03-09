from selenium import webdriver


def driver_switch(path):
    return CommonClass().set_driver(search_map.get(path.split('=')[0]))


def driver_by_chrome():
    print('chrome')
    return webdriver.Chrome()


def driver_by_firefox():
    return webdriver.Firefox()


def driver_by_ie():
    return webdriver.Ie()


def driver_by_edge():
    return webdriver.Edge()


search_map = {'chrome': driver_by_chrome,
              'firefox': driver_by_firefox,
              'ie': driver_by_ie,
              'edge': driver_by_edge}


class CommonClass:
    @classmethod
    def set_driver(cls, driver):
        cls.driver = driver

    @classmethod
    def get_driver(cls):
        return cls.driver
