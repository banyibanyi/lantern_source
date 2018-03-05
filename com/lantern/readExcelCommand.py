import xlrd


def read_excel():
    # 文件位置
    excel_file = xlrd.open_workbook(r'C:\Users\ONE\PycharmProjects\lantern_source\excels\excel4selenium.xlsx')

    # 获取功能模板内容
    sheet_command = excel_file.sheet_by_name('功能模板')

    # 获取模板头信息
    rows = sheet_command.row_values(0)
    all_rows = len(rows)

    # 创建二维数组将excel中的信息写入
    commands = [[] for i in range(all_rows)]
    for rowNum in range(all_rows):
        commands[rowNum].append(sheet_command.col_values(rowNum))

    # 返回二维数组作为后续处理的数据
    return commands


if __name__ == '__main__':
    read_excel()
