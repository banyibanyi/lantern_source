# -*- coding: utf-8 -*-
from readExcelCommand import read_excel
from doAction import *


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
        CommonClass.get_logger().debug(action)
        action_switch(action[4], action[5], action[6], action[7], action[8], action[9], action[10], action[11])
    CommonClass.get_driver().quit()


if __name__ == '__main__':
    CommonClass.get_logger().info("stat")
    do_excel_actions()
    CommonClass.get_logger().info("end")
    CommonClass.stop_log_listing()
