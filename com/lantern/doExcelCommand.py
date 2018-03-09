from readExcelCommand import read_excel
from doSearch import *
from doDriver import *


# 浏览器打开事件
def l_open_driver(path, text):
    driver_switch(path)


# 点击事件
def l_click(path, text):
    search_switch(path).click()


# 输入事件
def l_input(path, text):
    search_switch(path).send_keys(text)


def action_switch(action, path, text):
    return action_map.get(action)(path, text)


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
        action_switch(action[3], action[4], action[5])


action_map = {'open': l_open_driver,
              'click': l_click,
              'input': l_input}


if __name__ == '__main__':
    do_excel_actions()
