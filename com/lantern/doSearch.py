# -*- coding: utf-8 -*-
from driverCommon import CommonClass
from selenium.webdriver.common.by import By


def search_switch(type, path):
    return search_map.get(type)(path)


# 根据ID查询控件
def search_by_id(path):
    return CommonClass().get_driver().find_element_by_id(path)


# 根据name查询控件
def search_by_name(path):
    return CommonClass().get_driver().find_element_by_name(path)


# 根据class查询控件
def search_by_class(path):
    return CommonClass().get_driver().find_element_by_class_name(path)


# 根据tag查询控件
def search_by_tag(path):
    return CommonClass().get_driver().find_element_by_tag_name(path)


# 根据link查询控件
def search_by_link(path):
    return CommonClass().get_driver().find_element_by_link_text(path)


# 根据partial查询控件
def search_by_partial(path):
    return CommonClass().get_driver().find_element_by_partial_link_text(path)


# 根据partial查询控件
def search_by_xpath(path):
    return CommonClass().get_driver().find_element_by_xpath(path)


# 根据partial查询控件
def search_by_css(path):
    return CommonClass().get_driver().find_element_by_css_selector(path)


search_map = {By.ID: search_by_id,
              By.NAME: search_by_name,
              By.CLASS_NAME: search_by_class,
              By.TAG_NAME: search_by_tag,
              By.LINK_TEXT: search_by_link,
              By.PARTIAL_LINK_TEXT: search_by_partial,
              By.XPATH: search_by_xpath,
              By.CSS_SELECTOR: search_by_css}
