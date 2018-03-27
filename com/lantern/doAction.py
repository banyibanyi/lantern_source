from doDriver import *
from assertInfo import *
from doSearch import *
from selenium.webdriver.support.ui import Select
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui


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
    # 如果有需要input输入内容进行内容录入
    if len(text) > 0:
        try:
            search_switch(type, path).send_keys(text)
        # 遇到错误动作进行重试 该部分需要根据异常细化
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


# 事件关键字-方法映射表
action_map = {'open': open_driver,
              'click': single_click,
              'input': textbox_input,
              'get': browser_get,
              'select': select_action}
