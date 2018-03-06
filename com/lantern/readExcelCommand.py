import xlrd


def read_excel():
    # 文件位置
    excel_file = xlrd.open_workbook(r'../../excels/excel4selenium.xlsx')

    # 获取功能模板内容
    sheet_command = excel_file.sheet_by_name('功能模板')

    # 获取模板头信息
    col_num = sheet_command.nrows

    # 创建数组将excel中的信息写入
    commands = []
    for rowNum in range(col_num):
        commands.append(sheet_command.row_values(rowNum))

    # 返回二维数组作为后续处理的数据
    return commands


if __name__ == '__main__':
    read_excel()
