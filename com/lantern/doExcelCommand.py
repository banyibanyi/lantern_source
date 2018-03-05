from readExcelCommand import read_excel


def foo(var):
    return {
            'a': 1,
            'b': 2,
            'c': 3,
    }.get(var, 'error')    # 'error'为默认返回值，可自设置


def do_by_selenium():

    actions = read_excel()

    for action in actions:
        print(action)

    print(actions)


if __name__ == '__main__':
    do_by_selenium()
