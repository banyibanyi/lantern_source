from readExcelCommand import read_excel


def do_by_selenium():

    actions = read_excel()
    print(actions)


if __name__ == '__main__':
    do_by_selenium()
