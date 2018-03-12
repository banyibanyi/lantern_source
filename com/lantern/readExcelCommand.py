# -*- coding: utf-8 -*-
import xlrd
from collections import Counter


def read_excel():
    # 文件位置
    excel_file = xlrd.open_workbook(r'../../excels/excel4selenium.xlsx')

    # 获取功能模板内容
    sheet_command = excel_file.sheet_by_name('功能模板')

    # 获取模板头信息
    col_num = sheet_command.nrows

    # 去除loop中的标题以及空项 获取真正的循环标志
    # 循环标志可能为1个或2个一对，但不能大于2，可以有多对不同的loop
    loop_dict = Counter(sheet_command.col_values(1))
    loop_dict.pop('')
    loop_dict.pop('loop')

    # 如果dict不为空说明有循环标记，需要将指令循环添加到指令队列中
    if loop_dict:
        print('需要循环')

    # 创建数组将excel中的信息写入
    commands = []
    for rowNum in range(col_num):
        commands.append(sheet_command.row_values(rowNum))

    # 返回二维数组作为后续处理的数据
    return commands


if __name__ == '__main__':
    read_excel()
