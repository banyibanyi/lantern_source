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

    # 创建数组将excel中的信息写入
    commands = []

    # 如果dict不为空说明有循环标记，需要将指令循环添加到指令队列中
    if loop_dict:
        row_num = 0
        while row_num < col_num:
            # 如果loop标志信息为系统关键字loop 跳过
            if sheet_command.cell(row_num, 1).value == 'loop':
                pass
            # 在遇到第一个循环标志前没有标志的指令直接追加到指令数组中
            elif sheet_command.cell(row_num, 1).value == '':
                commands.append(sheet_command.row_values(row_num))
            else:
                # 获取循环标志
                loop_begin_mark = sheet_command.cell(row_num, 1).value
                # 获取该循环标志个数（只处理1，2次，其余为异常不支持）
                mul_marks = loop_dict.get(loop_begin_mark)
                # 获取循环次数
                loop_times = sheet_command.cell(row_num, 2).value
                # 如果只有一行指令需要循环执行 直接按照循环次数追加指令
                if mul_marks == 1:
                    while loop_times:
                        loop_times = loop_times - 1
                        commands.append(sheet_command.row_values(row_num))
                # 将两个循环标志中间命令进行循环写入临时数组
                elif mul_marks == 2:
                    loop_flag = True
                    temp_commands = [sheet_command.row_values(row_num)]
                    while loop_flag:
                        row_num = row_num + 1
                        loop_end_mark = sheet_command.cell(row_num, 1).value
                        temp_commands.append(sheet_command.row_values(row_num))
                        if loop_end_mark == loop_begin_mark:
                            loop_flag = False
                    # 将需要重复执行的指令循环loop_times次写入指令数组
                    while loop_times:
                        loop_times = loop_times - 1
                        for action in temp_commands:
                            commands.append(action)
                else:
                    print("error, too many parameters")
            row_num = row_num + 1

    # 如果excel中没有循环标志 直接将所有内容转换到数组中
    else:
        for row_num in range(col_num):
            commands.append(sheet_command.row_values(row_num))

    # 返回二维数组作为后续处理的数据
    return commands


if __name__ == '__main__':
    print(read_excel())
