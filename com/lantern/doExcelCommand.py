from readExcelCommand import read_excel
from doSearch import *
from doDriver import *


# 浏览器打开事件
def open_driver(type, path, text):
    driver_switch(type, path)


# 点击事件
def single_click(type, path, text):
    search_switch(type, path).click()


# 输入事件
def textbox_input(type, path, text):
    search_switch(type, path).send_keys(text)


# 地址跳转事件
def browser_get(type, path, text):
    CommonClass().get_driver().get(path)


def action_switch(action, type, path, text):
    return action_map.get(action)(type, path, text)


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
    for action in actions[1:]:
        # action, type, path, text
        action_switch(action[4], action[5], action[6], action[7])


action_map = {'open': open_driver,
              'click': single_click,
              'input': textbox_input,
              'get': browser_get}


if __name__ == '__main__':
    do_excel_actions()
