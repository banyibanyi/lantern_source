from readExcelCommand import read_excel


def open_chrome(y):
    print('i open', y)


def click(y):
    print('i click', y)


action_map = {'open chrome': open_chrome, 'click': click}


def switch(x, y):
    return action_map.get(x)(y)


def do_by_selenium():

    actions = read_excel()
    # 获取动作标志 用于后续动作处理
    action_title = actions[0]

    # 获取指令
    for action in actions[1:]:
        switch(action[3], action[4])


if __name__ == '__main__':
    do_by_selenium()
