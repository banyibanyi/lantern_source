# encoding: utf-8
from selenium import webdriver
from driverCommon import CommonClass


# 匹配不同种类的浏览器
def driver_switch(type, path):
    driver_map.get(type)(path)


def driver_by_chrome(path):
    driver = webdriver.Chrome()
    driver.get(path)
    CommonClass().set_driver(driver)


def driver_by_firefox(path):
    driver = webdriver.Firefox()
    driver.get(path)
    CommonClass().set_driver(driver)


def driver_by_ie(path):
    driver = webdriver.Ie()
    driver.get(path)
    CommonClass().set_driver(driver)


def driver_by_edge(path):
    driver = webdriver.Edge()
    driver.get(path)
    CommonClass().set_driver(driver)


driver_map = {'chrome': driver_by_chrome,
              'firefox': driver_by_firefox,
              'ie': driver_by_ie,
              'edge': driver_by_edge}
