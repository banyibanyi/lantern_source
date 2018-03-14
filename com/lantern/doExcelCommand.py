# -*- coding: utf-8 -*-
from readExcelCommand import read_excel
from doSearch import *
from doDriver import *
from assertInfo import *
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import Select


# 浏览器打开事件
def open_driver(type, path, text, assert_oral, assert_type, assert_goal, wait_time):
    driver_switch(type, path)
    # 断言判断
    if assert_type != '':
        print(assert_switch(assert_type, assert_goal))


# 点击事件
def single_click(type, path, text, assert_oral, assert_type, assert_goal, wait_time):
    # 如果设置了等待元素出现
    if wait_time != '' and int(wait_time) > 0:
        ui.WebDriverWait(CommonClass().get_driver(), int(wait_time)) \
            .until(ec.visibility_of_element_located((type, path)))
    try:
        search_switch(type, path).click()
    except Exception as err:
        print(err)
        CommonClass.get_driver().navigate.refresh()
        search_switch(type, path).click()


# 输入事件
def textbox_input(type, path, text, assert_oral, assert_type, assert_goal, wait_time):
    # 如果设置了等待元素出现
    if wait_time != '' and int(wait_time) > 0:
        ui.WebDriverWait(CommonClass().get_driver(), int(wait_time))\
            .until(ec.visibility_of_element_located((type, path)))
    try:
        search_switch(type, path).send_keys(text)
    except Exception as err:
        print(err)
        CommonClass.get_driver().navigate.refresh()
        search_switch(type, path).send_keys(text)


# 地址跳转事件
def browser_get(type, path, text, assert_oral, assert_type, assert_goal, wait_time):
    CommonClass().get_driver().get(path)
    # 断言判断
    if assert_type != '':
        print(assert_switch(assert_type, assert_goal))


# 列表框事件
def select_action(type, path, text, assert_oral, assert_type, assert_goal, wait_time):
    temp = text.split(':')
    if temp[0] == 'index':
        Select(search_switch(type, path)).select_by_index(temp[1])
    elif temp[0] == 'value':
        Select(search_switch(type, path)).select_by_value(temp[1])
    elif temp[0] == 'text':
        Select(search_switch(type, path)).select_by_visible_text(temp[1])


# 事件映射
def action_switch(action, action_type, path, text, assert_oral, assert_type, assert_goal, wait_time):
    return action_map.get(action)(action_type, path, text, assert_oral, assert_type, assert_goal, wait_time)


# 相等断言
def assert_equal(assert_oral, assert_goal):
    assert_info = assertInfo()
    assert_info.assert_result = (assert_oral == assert_goal)
    assert_info.assert_message = 'Target value is ' + assert_goal + 'Actual value is ' + assert_oral
    return assert_info


# 断言映射
def assert_switch(assert_type, assert_goal):
    return assert_map.get(assert_type)(assert_goal)


# 关闭当前页
def do_close():
    CommonClass().get_driver().close()


# 退出浏览器
def do_quit():
    CommonClass().get_driver().quit()


# 执行指令
def do_excel_actions():
    actions = read_excel()
    # 获取动作标志 用于后续动作处理
    # action_title = actions[0]

    # 获取指令
    for action in actions[2:]:
        # action, type, path, text
        print(action)
        action_switch(action[4], action[5], action[6], action[7], action[8], action[9], action[10], action[11])


# 事件关键字-方法映射表
action_map = {'open': open_driver,
              'click': single_click,
              'input': textbox_input,
              'get': browser_get,
              'select': select_action}


if __name__ == '__main__':
    do_excel_actions()
