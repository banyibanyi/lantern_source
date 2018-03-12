# -*- coding: utf-8 -*-
from driverCommon import CommonClass


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


search_map = {'id': search_by_id,
              'name': search_by_name,
              'class': search_by_class,
              'tag': search_by_tag,
              'link': search_by_link,
              'partial': search_by_partial,
              'xpath': search_by_xpath,
              'css': search_by_css}
